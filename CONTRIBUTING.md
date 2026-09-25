# Guía de Contribución de Data Packs Comunitarios

Bienvenido al repositorio oficial del **Índice de Data Packs de la Comunidad**. Este repositorio es un catálogo público, descentralizado y de código abierto gestionado automáticamente para la comunidad de jugadores.

---

## ⚖️ Principios de Integridad y Fair Play

Para mantener el juego justo, consistente y legalmente sostenible para todos:

1. **Modificación Cosmética Exclusiva:** Los Data Packs únicamente sustituyen de forma visual nombres de jugadores, iniciales y fotografías.
2. **Sin Ventaja Competitiva:** Los Data Packs **no pueden** modificar estadísticas, atributos, clubes, rarezas ni el balance del juego.
3. **Alojamiento Externo:** Este repositorio **no aloja** archivos de imagen ni archivos `.zip`. Solo almacena los metadatos neutros (título, autor, versión, checksum y enlace de descarga externa directa proporcionado por el creador).
4. **Índice 100% Neutro — Regla Obligatoria:** El `title`, `description` y `author` de tu propuesta **no pueden contener nombres de clubes, ligas, federaciones ni jugadores reales**. Usa términos genéricos (época, temporada, estilo, edición). Ejemplos válidos: `"Temporada 2026"`, `"Época Dorada 2006"`, `"Edición Retro"`. Ejemplos que el bot **rechazará automáticamente**: `"Pack Real Madrid"`, `"Champions Edition"`, `"Nombres de la Premier League"`.
   - Los nombres reales de jugadores y clubes **solo pueden existir dentro de tu `database.json`**, empaquetado en tu propio `.zip`, en tu propio hosting — nunca en este repositorio.
5. **Contenido Verificado por Hash:** una vez aprobado tu pack, su `checksum` queda fijo en el índice. Si reemplazas el archivo en tu hosting después de la aprobación, el juego rechazará la descarga por no coincidir el hash — deberás enviar una nueva propuesta con la versión actualizada.

---

## 📦 Estructura Requerida del Paquete (.zip)

Tu paquete debe estar comprimido en un único archivo `.zip` (peso máximo: 50 MB comprimido, 150 MB descomprimido) con la siguiente estructura interna:

```
mi_pack.zip
├── manifest.json
├── database.json
└── photos/
    ├── campe_01.png
    ├── campe_02.png
    └── ...
```

**Reglas de seguridad del paquete** (validadas automáticamente, tu PR será rechazado si no las cumple):
- Ningún archivo dentro del ZIP puede usar rutas con `../` o rutas absolutas (protección anti *zip slip*).
- Solo se permiten archivos `.json` en la raíz y `.png` dentro de `photos/` — ningún ejecutable, script u otro tipo de archivo.
- El tamaño total descomprimido no puede superar 150 MB (protección anti *decompression bomb*).
- Cada imagen debe ser cuadrada, formato PNG, mínimo 256×256 px.

### 1. `manifest.json`
```json
{
  "schemaVersion": 2,
  "packId": "pack_temporada_2026",
  "title": "Temporada 2026",
  "author": "TuAlias",
  "version": "1.0.0",
  "description": "Sustituciones cosméticas de jugadores y fotos actualizadas.",
  "totalCards": 80,
  "hasPhotos": true
}
```
> Nota: incluso dentro de tu propio `manifest.json` (que va en tu hosting, no en este repo), evita usar aquí nombres de clubes/ligas reales en `title`/`description` — este archivo puede quedar indexado por buscadores si tu hosting es público. Los nombres reales van solo en `database.json`.

### 2. `database.json`
```json
{
  "cards": [
    {
      "cardId": "campe_01",
      "playerName": "Nombre Jugador",
      "initials": "NJ",
      "position": "DEL"
    }
  ]
}
```
Cada `cardId` debe existir en el catálogo oficial de cartas del juego (`catalog/card_ids.json` en este mismo repositorio) — cualquier ID desconocido hará que la propuesta falle.

### 3. Carpeta `photos/`
Contiene las imágenes de los futbolistas en formato PNG cuadrado (mínimo 256×256 px, recomendado 512×512 px). El nombre de cada archivo debe coincidir exactamente con el `cardId` (ejemplo: `campe_01.png`).

---

## 🌐 ¿Dónde alojar tu archivo .zip?

El enlace debe ser una **descarga directa** (direct download URL).
* **Recomendado:** En la sección **Releases** de tu propio repositorio público de GitHub personal (rápido, sin límites de tráfico y enlace permanente).
* **No recomendado:** Google Drive, Dropbox o Mega (suelen fallar o bloquearse cuando muchos usuarios descargan el archivo al mismo tiempo por límites de cuota, y no garantizan URLs estables a largo plazo).

---

## 🚀 Cómo enviar tu propuesta (Paso a Paso)

Todo el proceso de revisión e indexación es **100% automático** mediante GitHub Actions. Ningún humano de este repositorio aprueba, lee ni cura el contenido de tu paquete manualmente:

1. Haz un **Fork** de este repositorio a tu cuenta personal de GitHub (o usa el botón "Edit this file" de GitHub para que lo haga por ti).
2. Crea un archivo JSON dentro de la carpeta `proposals/` con el identificador de tu pack, por ejemplo `proposals/pack_temporada_2026.json`:
   ```json
   {
     "id": "pack_temporada_2026",
     "title": "Temporada 2026",
     "author": "TuAlias",
     "version": "1.0.0",
     "sizeMb": 8.4,
     "downloadUrl": "https://github.com/tu-usuario/tu-repo/releases/download/v1.0/mi_pack.zip"
   }
   ```
3. Haz commit y abre un **Pull Request** apuntando hacia la rama `main` de este repositorio.
4. El bot de GitHub Actions descarga tu `.zip` **temporalmente, solo en memoria del proceso de validación** (nunca lo guarda en este repositorio) y ejecuta las comprobaciones:
   - Que el enlace de descarga responda correctamente y sea HTTPS.
   - Que no supere los límites de peso comprimido/descomprimido.
   - Que no contenga rutas inseguras (*zip slip*) ni tipos de archivo no permitidos.
   - Que `manifest.json` y `database.json` cumplan el schema exacto.
   - Que todos los `cardId` existan en el catálogo oficial del juego.
   - Que `title`, `description` y `author` no contengan términos de la lista de marcas/nombres bloqueados (Principio 4).
5. Si todas las pruebas pasan en verde, el bot calcula el `sha256` del archivo, añade **solo los campos neutros** (`id`, `title`, `author`, `version`, `sizeMb`, `downloadUrl`, `checksum`, `submittedAt`) al `datapacks_index.json`, y fusiona (merge) tu Pull Request automáticamente.
6. Si alguna prueba falla, el bot comenta el motivo técnico específico en tu PR y lo cierra — puedes corregir y volver a intentarlo.

---

## 🔒 Qué hacer si tu pack es señalado por infracción de derechos

Si un tercero notifica que tu pack infringe derechos de autor, marca registrada o derecho de imagen, será retirado del índice de forma preventiva mientras se revisa. Este repositorio no tiene forma de verificar la titularidad de cada nombre o fotografía que un creador decide usar — esa responsabilidad es de quien sube el contenido a su propio hosting.
