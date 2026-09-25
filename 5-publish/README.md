# Publish

The **only** place output is built from. Nothing outside this folder is ever published.

| Folder | Output | Build |
|---|---|---|
| `site/` | GitHub Pages (MkDocs Material via doc-builder) | `_system/scripts/build-site.sh` |
| `pdf/` | Styled PDFs | `_system/scripts/build-pdf.sh <note.md>` |
| `slides/` | Marp decks (HTML/PDF) | `_system/scripts/build-slides.sh <deck.md>` |

Promote a note by copying its final version here from `2-areas/` or `1-projects/`.
`site/00-index.md` defines the site navigation.
