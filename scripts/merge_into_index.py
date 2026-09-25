import json
import sys
from pathlib import Path

def merge(validated_path: str, index_path: str):
    with open(validated_path, "r", encoding="utf-8") as f:
        new_pack = json.load(f)

    with open(index_path, "r", encoding="utf-8") as f:
        index_data = json.load(f)

    packs = index_data.get("packs", [])
    pack_id = new_pack["id"]

    existing_idx = next((i for i, p in enumerate(packs) if p.get("id") == pack_id), None)
    if existing_idx is not None:
        packs[existing_idx] = new_pack
        print(f"[INFO] Pack '{pack_id}' actualizado en datapacks_index.json.")
    else:
        packs.append(new_pack)
        print(f"[INFO] Pack '{pack_id}' agregado a datapacks_index.json.")

    index_data["packs"] = packs

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

    print("[SUCCESS] Índice actualizado con éxito.")

if __name__ == "__main__":
    merge("validated_pack.json", "datapacks_index.json")
