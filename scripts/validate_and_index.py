import sys
import os
import json
import urllib.request
import zipfile
import hashlib

MAX_SIZE_MB = 50.0

def validate_and_append(proposal_file_path, index_file_path):
    # 1. Leer propuesta del PR
    with open(proposal_file_path, 'r', encoding='utf-8') as f:
        proposal = json.load(f)

    pack_id = proposal.get("id", "").strip()
    download_url = proposal.get("downloadUrl", "").strip()
    title = proposal.get("title", "").strip()
    author = proposal.get("author", "Comunidad").strip()
    version = proposal.get("version", "1.0.0").strip()
    description = proposal.get("description", "").strip()

    if not pack_id or not download_url:
        print("[ERROR] 'id' y 'downloadUrl' son campos obligatorios.")
        sys.exit(1)

    print(f"[INFO] Validando propuesta: {pack_id} ({download_url})...")

    # 2. Descargar zip temporal en memoria/runner
    temp_zip = "temp_pack.zip"
    try:
        urllib.request.urlretrieve(download_url, temp_zip)
    except Exception as e:
        print(f"[ERROR] No se pudo descargar el archivo desde {download_url}: {e}")
        sys.exit(1)

    # 3. Validar peso
    file_size_mb = os.path.getsize(temp_zip) / (1024 * 1024)
    if file_size_mb > MAX_SIZE_MB:
        print(f"[ERROR] El paquete supera el límite permitido ({file_size_mb:.2f} MB > {MAX_SIZE_MB} MB).")
        sys.exit(1)

    # 4. Validar integridad ZIP y schema interno
    try:
        with zipfile.ZipFile(temp_zip, 'r') as zf:
            namelist = zf.namelist()
            # Buscar manifest.json y database.json (en raíz o subcarpeta)
            manifest_name = next((n for n in namelist if n.endswith("manifest.json")), None)
            db_name = next((n for n in namelist if n.endswith("database.json")), None)

            if not manifest_name or not db_name:
                print("[ERROR] El ZIP debe contener 'manifest.json' y 'database.json'.")
                sys.exit(1)

            # Validar JSONs
            manifest_data = json.loads(zf.read(manifest_name).decode('utf-8'))
            db_data = json.loads(zf.read(db_name).decode('utf-8'))

            cards_count = len(db_data.get("cards", []))
            print(f"[INFO] Pack validado con éxito: {cards_count} cartas sustituidas.")
    except Exception as e:
        print(f"[ERROR] El archivo ZIP está corrupto o los JSON son inválidos: {e}")
        sys.exit(1)
    finally:
        if os.path.exists(temp_zip):
            os.remove(temp_zip)

    # 5. Cargar índice actual y añadir entrada neutra
    with open(index_file_path, 'r', encoding='utf-8') as f:
        index_data = json.load(f)

    packs = index_data.get("packs", [])
    # Reemplazar si ya existe la misma versión o ID, o añadir nuevo
    existing_idx = next((i for i, p in enumerate(packs) if p.get("id") == pack_id), None)
    
    new_entry = {
        "id": pack_id,
        "title": title if title else pack_id,
        "author": author,
        "version": version,
        "description": description,
        "downloadUrl": download_url,
        "sizeMb": f"{file_size_mb:.1f} MB",
        "cardsCount": cards_count,
        "isRecommended": False,
        "bannerColor": "#E8A820"
    }

    if existing_idx is not None:
        packs[existing_idx] = new_entry
        print(f"[INFO] Pack '{pack_id}' actualizado en el índice.")
    else:
        packs.append(new_entry)
        print(f"[INFO] Pack '{pack_id}' agregado al índice.")

    index_data["packs"] = packs

    with open(index_file_path, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

    print("[SUCCESS] datapacks_index.json actualizado correctamente.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python validate_and_index.py <proposal_json_path> <index_json_path>")
        sys.exit(1)
    validate_and_append(sys.argv[1], sys.argv[2])
