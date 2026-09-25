# CLAUDE.md — ignite-docs vault

Obsidian vault for FRC 6829 Ignite Robotics documentation. **PARA** for authored docs,
a **knowledge graph** for ingested research, and one **design system** driving every
output format. Fully separate from `../docs` (ignition-labs); programming curriculum lives there, not here.

## Layout

| Path | Holds | Rule |
|---|---|---|
| `_inbox/` | Quick capture, brand assets | New notes default here. Triage often. |
| `_inbox/capture.md` | Running list of notes and links | Never move or delete. Content below the `capture:start` marker is drained by `ingest-inbox.sh` |
| `wiki/` | Knowledge graph: wiki-ingest output | Plugin-owned; see below |
| `_research/` | Research drops: clippings, PDFs, repo notes | Staged to `.raw/` by `ingest-inbox.sh` |
| `.raw/` | Immutable ingest sources + `.manifest.json` | Never edit sources. Hidden in Obsidian. |
| `1-projects/<name>/` | Time-boxed doc efforts with a deliverable | Start from `project-brief` template |
| `2-areas/robot-engineering/` | Mech, electrical, build, hardware | Ongoing, no deadline |
| `2-areas/team-operations/` | Onboarding, mentors, process, strategy/scouting | |
| `2-areas/business-outreach/` | Fundraising, sponsors, outreach, awards | |
| `3-resources/references/` | Hand-written reference notes | |
| `4-archives/<year>/` | Finished projects, retired docs | |
| `5-publish/{site,pdf,slides}/` | **The only folder that produces output** | Never write here unless Josh asks |
| `_system/` | Templates, design system, build scripts | |

Where new material goes: working docs → `2-areas/` or `1-projects/`; research → `_research/` → knowledge graph;
finished output → copy into `5-publish/` when asked.

## Knowledge graph (claude-obsidian plugin)

`wiki/` is the plugin's native layout (`index.md`, `hot.md`, `log.md`, `sources/`, `entities/`, `concepts/`).
It sits at the vault root, outside PARA, because the claude-obsidian skills hardcode that path. Don't move it.

Mode is `generic` (`.vault-meta/mode.json`). Do not switch to the plugin's `para` mode: it would file research
into `wiki/areas/` and mix it with authored docs. Ingested notes never go into `2-areas/`. Area docs link *to*
knowledge-graph notes as their sources.

Flow: drop files in `_research/` (or `_inbox/`, or jot lines in `_inbox/capture.md`) → `_system/scripts/ingest-inbox.sh` → "ingest all new sources in .raw/".

## Frontmatter schema

```yaml
title: string
area: robot-engineering | team-operations | business-outreach   # area docs
status: draft | review | final
audience: students | mentors | sponsors | judges | public
tags: []
sources: []        # wikilinks into the knowledge graph
```
Research notes use `type: source|entity|concept`. Decks need `marp: true` and `theme: ignite`.

## Design system

`_system/design-system/tokens.yaml` is the single source of truth: colors, fonts, spacing, logo.
`build_css.py` renders `generated/{mkdocs,print,marp-theme,obsidian-snippet}.css` and syncs the Obsidian
snippet to `.obsidian/snippets/ignite.css`. Never hand-edit generated CSS. Change tokens, then rebuild.
HTML artifacts should embed `generated/mkdocs.css` variables (`--ig-*`) to stay on-brand.

Tokens are **placeholders** until brand assets land in `_inbox/`. Then move them to `design-system/assets/`
and update `tokens.yaml`.

## Commands

Env: pyenv virtualenv `ignite-docs` (3.13.6, set in `.python-version`). Run `pyenv activate ignite-docs` before
`poetry install --no-root`. Without an active `VIRTUAL_ENV`, Poetry makes its own cache env instead.

```bash
python _system/design-system/build_css.py            # regenerate all CSS
_system/scripts/build-pdf.sh [note.md ...]           # → output/pdf/   (default: 5-publish/pdf/*.md)
_system/scripts/build-slides.sh [deck.md ...]        # → output/slides/ (Marp via npx)
_system/scripts/build-site.sh                        # → output/site/  (doc-builder, needs ../doc-builder installed)
_system/scripts/ingest-inbox.sh                      # _inbox/ + _research/ → .raw/<date>/
```
`output/` is gitignored. GitHub Pages deploy (CI) is not set up yet.

## MCP

Project `.mcp.json` defines `ignite-vault` (`@bitbonsai/mcpvault`) scoped to this repo. The global `obsidian`
server points at a different vault (brain2); don't use it for this repo.

## Obsidian plugins to install manually

Templater (optional; core Templates is configured), Dataview, Marp Slides.
