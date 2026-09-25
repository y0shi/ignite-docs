#!/usr/bin/env bash
# Stage research from _inbox/ and _research/ into .raw/ for claude-obsidian wiki-ingest.
# Then tell Claude: "ingest all new sources in .raw/".
# Brand assets (images/fonts/svg) in _inbox/ are left alone for the design system.
# _inbox/capture.md stays in place: its content below the capture:start marker is drained to .raw/.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
stamp="$(date +%Y-%m-%d)"
dest=".raw/$stamp"
moved=0

capture="_inbox/capture.md"
marker="<!-- capture:start"
if [ -f "$capture" ]; then
  if grep -q "^$marker" "$capture"; then
    body="$(sed -n "/^$marker/,\$p" "$capture" | tail -n +2)"
    if [ -n "$(printf '%s' "$body" | tr -d '[:space:]')" ]; then
      mkdir -p "$dest"
      out="$dest/capture-$(date +%H%M%S).md"
      printf -- '---\ntitle: Capture drained %s\nsource_type: capture\n---\n%s\n' "$(date '+%Y-%m-%d %H:%M')" "$body" > "$out"
      header="$(sed "/^$marker/q" "$capture")"
      printf '%s\n\n' "$header" > "$capture"
      echo "drained $capture -> $out"
      moved=$((moved + 1))
    fi
  else
    echo "WARNING: $capture has no capture:start marker; left untouched" >&2
  fi
fi

for src in _inbox _research; do
  while IFS= read -r -d '' f; do
    case "$f" in
      *.png|*.jpg|*.jpeg|*.svg|*.ttf|*.otf|*.woff|*.woff2) [ "$src" = "_inbox" ] && continue ;;
    esac
    mkdir -p "$dest"
    if git ls-files --error-unmatch "$f" >/dev/null 2>&1; then git mv "$f" "$dest/"; else mv "$f" "$dest/"; fi
    echo "staged $f -> $dest/"
    moved=$((moved + 1))
  done < <(find "$src" -maxdepth 1 -type f ! -name '.gitkeep' ! -path "$capture" -print0)
done
echo "$moved file(s) staged in $dest"
