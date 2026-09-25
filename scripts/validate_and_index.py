        from datetime import datetime, timezone

        # Objeto neutro blindado: sin descripción abierta, con checksum auditado y fecha
        result = {
            "id": proposal["id"],
            "title": proposal["title"],
            "author": proposal["author"],
            "version": proposal["version"],
            "downloadUrl": proposal["downloadUrl"],
            "checksumSha256": checksum,
            "checksum": f"sha256:{checksum}",
            "sizeMb": f"{size_mb_float} MB",
            "cardsCount": total_cards,
            "isRecommended": False,
            "bannerColor": "#E8A820",
            "submittedAt": datetime.now(timezone.utc).strftime("%Y-%m-%d")
        }
