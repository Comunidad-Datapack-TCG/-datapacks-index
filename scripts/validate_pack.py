import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path

MAX_ZIP_MB = 50.0
MAX_UNPACKED_MB = 150.0

def fail(msg: str):
    print(f"[ERROR] {msg}", file=sys.stderr)
    sys.exit(1)

def load_json(path: Path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        fail(f"JSON inválido en {path}: {e}")

def check_metadata_neutral(proposal: dict, blocklist: list):
    text = " ".join(
        str(proposal.get(field, "")).lower()
        for field in ("title", "description", "author")
    )
    for term in blocklist:
        pattern = r"\b" + re.escape(term.lower()) + r"\b"
        if re.search(pattern, text):
            fail(f"El metadato contiene un término bloqueado ('{term}'). title/description/author deben ser genéricos.")

def safe_extract_and_validate(zip_path: str, valid_card_ids: set):
    total_unpacked = 0
    max_unpacked_bytes = int(MAX_UNPACKED_MB * 1024 * 1024)

    with zipfile.ZipFile(zip_path, 'r') as zf:
        namelist = zf.namelist()
        manifest_name = next((n for n in namelist if n.endswith("manifest.json")), None)
        db_name = next((n for n in namelist if n.endswith("database.json")), None)

        if not manifest_name or not db_name:
            fail("El archivo .zip debe contener 'manifest.json' y 'database.json'.")

        for info in zf.infolist():
            # Protección Zip Slip
            if os.path.isabs(info.filename) or ".." in info.filename:
                fail(f"Ruta maliciosa detectada en ZIP: {info.filename}")

            total_unpacked += info.file_size
            # Protección Bomba de Descompresión
            if total_unpacked > max_unpacked_bytes:
                fail(f"El ZIP descomprimido supera el límite de seguridad de {MAX_UNPACKED_MB} MB.")

        manifest_data = json.loads(zf.read(manifest_name).decode('utf-8'))
        db_data = json.loads(zf.read(db_name).decode('utf-8'))

        cards = db_data.get("cards", [])
        if not cards:
            fail("El archivo database.json no contiene ninguna carta en 'cards'.")

        # Validar contra catálogo oficial de card_ids
        for c in cards:
            cid = c.get("cardId")
            if cid not in valid_card_ids:
                fail(f"cardId no reconocido en tu juego: '{cid}'. Solo se permiten IDs del catálogo oficial.")

        return len(cards)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--proposal", required=True)
    parser.add_argument("--catalog", required=True)
    parser.add_argument("--blocklist", required=True)
    args = parser.parse_args()

    proposal = load_json(Path(args.proposal))
    catalog = set(load_json(Path(args.catalog)))
    blocklist = load_json(Path(args.blocklist))

    # 1. Validar campos de la propuesta
    pack_id = proposal.get("id", "").strip()
    download_url = proposal.get("downloadUrl", "").strip()
    if not pack_id or not download_url:
        fail("La propuesta debe contener 'id' y 'downloadUrl'.")

    if not download_url.startswith("https://"):
        fail("downloadUrl debe usar HTTPS.")

    # 2. Validar que no contenga marcas en title/desc/author
    check_metadata_neutral(proposal, blocklist)

    # 3. Descargar a archivo temporal
    temp_zip = "temp_download.zip"
    try:
        req = urllib.request.Request(
            download_url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        sha256 = hashlib.sha256()
        total_size = 0
        max_bytes = int(MAX_ZIP_MB * 1024 * 1024)

        with urllib.request.urlopen(req) as resp, open(temp_zip, "wb") as f:
            while True:
                chunk = resp.read(1024 * 1024)
                if not chunk:
                    break
                total_size += len(chunk)
                if total_size > max_bytes:
                    fail(f"El .zip supera el límite de {MAX_ZIP_MB} MB.")
                sha256.update(chunk)
                f.write(chunk)

        calculated_checksum = sha256.hexdigest()
        size_mb = f"{total_size / (1024 * 1024):.1f} MB"

        # 4. Validar contenido interno y IDs de cartas
        cards_count = safe_extract_and_validate(temp_zip, catalog)

        # 5. Imprimir resultado para merge_into_index en formato JSON de salida
        result = {
            "id": pack_id,
            "title": proposal.get("title", pack_id).strip(),
            "author": proposal.get("author", "Comunidad").strip(),
            "version": proposal.get("version", "1.0.0").strip(),
            "description": proposal.get("description", "").strip(),
            "downloadUrl": download_url,
            "checksumSha256": calculated_checksum,
            "sizeMb": size_mb,
            "cardsCount": cards_count,
            "isRecommended": False,
            "bannerColor": "#E8A820"
        }
        with open("validated_pack.json", "w", encoding="utf-8") as out:
            json.dump(result, out, indent=2, ensure_ascii=False)

        print(f"[SUCCESS] Pack validado: {pack_id} ({cards_count} cartas, Checksum={calculated_checksum[:8]}...)")
    finally:
        if os.path.exists(temp_zip):
            os.remove(temp_zip)

if __name__ == "__main__":
    main()
