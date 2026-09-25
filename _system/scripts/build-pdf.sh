#!/usr/bin/env bash
# Usage: build-pdf.sh <note.md> [...]   (defaults to every note in 5-publish/pdf/)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
python _system/design-system/build_css.py >/dev/null
if [ $# -eq 0 ]; then set -- 5-publish/pdf/*.md; fi
python _system/scripts/build_pdf.py "$@"
