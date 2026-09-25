#!/usr/bin/env bash
# Usage: build-slides.sh <deck.md> [...]   (defaults to every deck in 5-publish/slides/)
# Decks need `marp: true` and `theme: ignite` in frontmatter.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
python _system/design-system/build_css.py >/dev/null
if [ $# -eq 0 ]; then set -- 5-publish/slides/*.md; fi
mkdir -p output/slides
THEME=_system/design-system/generated/marp-theme.css
for deck in "$@"; do
  name="$(basename "$deck" .md)"
  npx -y @marp-team/marp-cli@latest --theme-set "$THEME" --html --allow-local-files "$deck" -o "output/slides/$name.html"
  npx -y @marp-team/marp-cli@latest --theme-set "$THEME" --pdf --allow-local-files "$deck" -o "output/slides/$name.pdf"
done
