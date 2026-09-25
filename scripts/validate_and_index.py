import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import zipfile
from pathlib import Path
from urllib.parse import urlparse
import requests

ALLOWED_ROOT_FILES = {"manifest.json", "database.json"}
ALLOWED_PHOTO_EXT = {".png"}
REQUIRED_MANIFEST_FIELDS = {
    "schemaVersion", "packId", "title", "author", "version",
    "totalCards", "hasPhotos"
}
REQUIRED_CARD_FIELDS = {"cardId", "playerName", "initials", "position"}

class ValidationError(Exception):
    pass

def fail(msg: str):
    print(f"::error::{msg}", file=sys.stderr)
    raise ValidationError(msg)

def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        fail(f"JSON inválido en {path}: {e}")

def check_url_is_https(url: str):
    parsed = urlparse(url)
    if parsed.scheme != "https":
        fail(f"downloadUrl debe ser HTTPS, recibido: {parsed.scheme!r}")

def check_metadata_neutral(proposal: dict, blocklist: list):
    text = " ".join(
        str(proposal.get(field, "")).lower()
        for field in ("title", "author")
    )
    for term in blocklist:
        pattern = r"\b" + re.escape(term.lower()) + r"\b"
        if re.search(pattern, text):
            fail(
                f"Metadato contiene un término bloqueado ('{term}'). "
                f"title/author deben ser genéricos (ver Principio 4 de CONTRIBUTING.md)."
            )

def download_to_temp(url: str, max_zip_mb: float, dest: Path):
    check_url_is_https(url)
    resp = requests.get(url, stream=True, timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
    if resp.status_code != 200:
        fail(f"downloadUrl respondió {resp.status_code}, se esperaba 200.")

    max_bytes = int(max_zip_mb * 1024 * 1024)
    written = 0
    with open(dest, "wb") as f:
        for chunk in resp.iter_content(chunk_size=1024 * 1024):
            written += len(chunk)
            if written > max_bytes:
                fail(f"El .zip supera el límite de {max_zip_mb} MB comprimido.")
            f.write(chunk)
    return written

def compute_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def safe_extract(zip_path: Path, extract_to: Path, max_unpacked_mb: float):
    max_unpacked_bytes = int(max_unpacked_mb * 1024 * 1024)
    total_uncompressed = 0

    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            name = info.filename
            normalized = Path(name)
            if normalized.is_absolute() or ".." in normalized.parts:
                fail(f"Ruta insegura dentro del ZIP (zip slip): {name!r}")

            total_uncompressed += info.file_size
            if total_uncompressed > max_unpacked_bytes:
                fail(f"El contenido descomprimido supera {max_unpacked_mb} MB (posible bomba de descompresión).")

            parts = normalized.parts
            if len(parts) == 1:
                if name not in ALLOWED_ROOT_FILES:
                    fail(f"Archivo no permitido en la raíz del ZIP: {name!r}")
            elif parts[0] == "photos":
                if Path(name).suffix.lower() not in ALLOWED_PHOTO_EXT:
                    fail(f"Archivo no permitido dentro de photos/: {name!r}")
            else:
                fail(f"Ruta o carpeta no reconocida dentro del ZIP: {name!r}")

        zf.extractall(extract_to)

def validate_manifest(extract_to: Path):
    manifest_path = extract_to / "manifest.json"
    if not manifest_path.exists():
        fail("Falta manifest.json en el paquete.")
    manifest = load_json(manifest_path)
    missing = REQUIRED_MANIFEST_FIELDS - manifest.keys()
    if missing:
        fail(f"manifest.json no cumple el schema, faltan campos: {missing}")
    return manifest

def validate_database(extract_to: Path, catalog_ids: set):
    db_path = extract_to / "database.json"
    if not db_path.exists():
        fail("Falta database.json en el paquete.")
    db = load_json(db_path)

    cards = db.get("cards")
    if not isinstance(cards, list) or not cards:
        fail("database.json debe tener un array 'cards' no vacío.")

    photos_dir = extract_to / "photos"
    for card in cards:
        missing = REQUIRED_CARD_FIELDS - card.keys()
        if missing:
            fail(f"Carta con campos faltantes {missing}: {card}")

        card_id = card["cardId"]
        if card_id not in catalog_ids:
            fail(f"cardId desconocido: {card_id!r} - no existe en catalog/card_ids.json.")

        expected_photo = photos_dir / f"{card_id}.png"
        if not expected_photo.exists():
            fail(f"Falta la foto correspondiente para {card_id}: {expected_photo.name}")

    return len(cards)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--proposal", required=True, type=Path)
    parser.add_argument("--catalog", required=True, type=Path)
    parser.add_argument("--blocklist", required=True, type=Path)
    parser.add_argument("--max-zip-mb", required=True, type=float)
    parser.add_argument("--max-unpacked-mb", required=True, type=float)
    parser.add_argument("--output", default="validated_pack.json", type=Path)
    args = parser.parse_args()

    proposal = load_json(args.proposal)
    catalog_ids = set(load_json(args.catalog))
    blocklist = load_json(args.blocklist)

    required_proposal_fields = {"id", "title", "author", "version", "downloadUrl"}
    missing = required_proposal_fields - proposal.keys()
    if missing:
        fail(f"Propuesta incompleta, faltan campos obligatorios: {missing}")

    check_metadata_neutral(proposal, blocklist)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        zip_path = tmp_path / "pack.zip"
        extract_to = tmp_path / "extracted"
        extract_to.mkdir()

        download_to_temp(proposal["downloadUrl"], args.max_zip_mb, zip_path)
        checksum = compute_sha256(zip_path)

        safe_extract(zip_path, extract_to, args.max_unpacked_mb)
        validate_manifest(extract_to)
        total_cards = validate_database(extract_to, catalog_ids)

        size_mb_float = round(zip_path.stat().st_size / (1024 * 1024), 1)

        # Objeto neutro blindado: SIN descripción abierta, con checksum auditado
        result = {
            "id": proposal["id"],
            "title": proposal["title"],
            "author": proposal["author"],
            "version": proposal["version"],
            "downloadUrl": proposal["downloadUrl"],
            "checksumSha256": checksum,
            "sizeMb": f"{size_mb_float} MB",
            "cardsCount": total_cards,
            "isRecommended": False,
            "bannerColor": "#E8A820"
        }

        with open(args.output, "w", encoding="utf-8") as out:
            json.dump(result, out, indent=2, ensure_ascii=False)

    print(f"[SUCCESS] Pack validado: {proposal['id']} ({total_cards} cartas)", file=sys.stderr)

if __name__ == "__main__":
    try:
        main()
    except ValidationError:
        sys.exit(1)
    except requests.RequestException as e:
        print(f"::error::No se pudo descargar el paquete: {e}", file=sys.stderr)
        sys.exit(1)
