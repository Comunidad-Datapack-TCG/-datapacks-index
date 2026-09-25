# Guía de Contribución de Data Packs Comunitarios

Bienvenido al repositorio oficial del **Índice de Data Packs de la Comunidad**. Este repositorio es un catálogo público, descentralizado y de código abierto gestionado automáticamente para la comunidad de jugadores.

---

## ⚖️ Principios de Integridad y Fair Play

Para mantener el juego justo y consistente para todos:
1. **Modificación Cosmética Exclusiva:** Los Data Packs únicamente sustituyen de forma visual nombres de jugadores, iniciales y fotografías.
2. **Sin Ventaja Competitiva:** Los Data Packs **no pueden** modificar estadísticas, atributos, clubes, rarezas ni el balance del juego.
3. **Alojamiento Externo:** Este repositorio **no aloja** archivos de imagen ni archivos `.zip`. Solo almacena los metadatos neutros (título, autor, versión y enlace de descarga externa directa proporcionado por el creador).

---

## 📦 Estructura Requerida del Paquete (.zip)

Tu paquete debe estar comprimido en un único archivo `.zip` (peso máximo: 50 MB) con la siguiente estructura interna:

mi_pack.zip
├── manifest.json
├── database.json
└── photos/
    ├── campe_01.png
    ├── campe_02.png
    └── ...

### 1. manifest.json
Contiene la información general de tu paquete:
{
  "schemaVersion": 2,
  "packId": "pack_temporada_2026",
  "title": "Nombres Reales Temporada 2026",
  "author": "TuAlias",
  "version": "1.0.0",
  "description": "Sustituciones cosméticas de futbolistas y fotos actualizadas.",
  "totalCards": 80,
  "hasPhotos": true
}

### 2. database.json
Define las sustituciones visuales por cada carta:
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

### 3. Carpeta photos/
Contiene las imágenes de los futbolistas en formato PNG cuadrado (mínimo 256x256 px o 512x512 px). El nombre de cada archivo debe coincidir exactamente con el cardId (ejemplo: campe_01.png).

---

## 🌐 ¿Dónde alojar tu archivo .zip?

El enlace debe ser una **descarga directa** (direct download URL). 
* **Recomendado:** En la sección **Releases** de tu propio repositorio público de GitHub personal (rápido, sin límites de tráfico y enlace permanente).
* **No recomendado:** Google Drive, Dropbox o Mega (suelen fallar o bloquearse cuando muchos usuarios descargan el archivo al mismo tiempo por límites de cuota).

---

## 🚀 Cómo enviar tu propuesta (Paso a Paso)

Todo el proceso de revisión e indexación es **100% automático** mediante GitHub Actions. Ningún humano aprueba a mano:

1. Haz un **Fork** de este repositorio a tu cuenta personal de GitHub.
2. Crea un archivo JSON dentro de la carpeta `proposals/` con el identificador de tu pack, por ejemplo `proposals/pack_temporada_2026.json`:

{
  "id": "pack_temporada_2026",
  "title": "Nombres Reales Temporada 2026",
  "author": "TuAlias",
  "version": "1.0.0",
  "description": "Sustituciones cosméticas de futbolistas y fotos actualizadas.",
  "downloadUrl": "https://github.com/tu-usuario/tu-repo/releases/download/v1.0/mi_pack.zip"
}

3. Haz commit y abre un **Pull Request** apuntando hacia la rama `main` de este repositorio.
4. El bot de GitHub Actions ejecutará las comprobaciones técnicas:
   - Verificará que el enlace de descarga responda correctamente.
   - Comprobará que no supere los 50 MB de peso.
   - Validará la integridad de los archivos JSON internos.
5. Si todas las pruebas técnicas pasan en verde, **el bot actualizará el archivo `datapacks_index.json` y fusionará (merge) tu Pull Request automáticamente**.
