#!/usr/bin/env bash
# Stage research from _inbox/ and _research/ into .raw/ for claude-obsidian wiki-ingest.
# Then tell Claude: "ingest all new sources in .raw/".
# Brand assets (images/fonts/svg) in _inbox/ are left alone for the design system.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
stamp="$(date +%Y-%m-%d)"
dest=".raw/$stamp"
moved=0
for src in _inbox _research; do
  while IFS= read -r -d '' f; do
    case "$f" in
      *.png|*.jpg|*.jpeg|*.svg|*.ttf|*.otf|*.woff|*.woff2) [ "$src" = "_inbox" ] && continue ;;
    esac
    mkdir -p "$dest"
    if git ls-files --error-unmatch "$f" >/dev/null 2>&1; then git mv "$f" "$dest/"; else mv "$f" "$dest/"; fi
    echo "staged $f -> $dest/"
    moved=$((moved + 1))
  done < <(find "$src" -maxdepth 1 -type f ! -name '.gitkeep' -print0)
done
echo "$moved file(s) staged in $dest"
