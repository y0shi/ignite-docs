#!/usr/bin/env bash
# Builds 5-publish/site/ into output/site/ with doc-builder, then applies design-system CSS.
# Preview: python -m http.server -d output/site
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
python _system/design-system/build_css.py >/dev/null
rm -rf output/site
doc-builder build-from-source 5-publish/site --output output/site --site-name "Ignite Robotics Docs"
# doc-builder already links stylesheets/extra.css; append our tokens-driven theme to it.
# TODO: replace with a proper --extra-css flag in ../doc-builder.
cat _system/design-system/generated/mkdocs.css >> output/site/stylesheets/extra.css
# GitHub Pages needs index.html; doc-builder emits the landing page as 00-index.html.
cp output/site/00-index.html output/site/index.html
echo "site built: output/site/index.html"
