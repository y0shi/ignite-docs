"""Render an Obsidian note to a branded PDF using the design-system print stylesheet."""

import argparse
import re
from datetime import date
from pathlib import Path

import markdown
import yaml
from weasyprint import HTML

VAULT_ROOT = Path(__file__).resolve().parents[2]
DESIGN_DIR = VAULT_ROOT / "_system" / "design-system"
OUTPUT_DIR = VAULT_ROOT / "output" / "pdf"

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
WIKILINK_RE = re.compile(r"(!?)\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]+))?\]\]")
CALLOUT_RE = re.compile(r"^> \[!(\w+)\][+-]? ?(.*)$")


def split_frontmatter(text: str) -> tuple[dict, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    return yaml.safe_load(match.group(1)) or {}, text[match.end():]


def resolve_wikilinks(body: str, note_dir: Path) -> str:
    """Embeds of images become <img>; other wikilinks become plain text (PDFs have no vault)."""

    def replace(match: re.Match[str]) -> str:
        embed, target, alias = match.groups()
        if embed and Path(target).suffix.lower() in {".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp"}:
            candidates = [note_dir / target, VAULT_ROOT / "_system" / "attachments" / target]
            path = next((p for p in candidates if p.exists()), candidates[0])
            return f"![{alias or ''}]({path.as_uri()})"
        return alias or Path(target).stem

    return WIKILINK_RE.sub(replace, body)


def convert_callouts(body: str) -> str:
    """Turn Obsidian `> [!type] Title` blockquotes into styled divs."""
    out: list[str] = []
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        match = CALLOUT_RE.match(lines[i])
        if not match:
            out.append(lines[i])
            i += 1
            continue
        kind, title = match.group(1).lower(), match.group(2) or match.group(1).title()
        i += 1
        inner: list[str] = []
        while i < len(lines) and lines[i].startswith(">"):
            inner.append(lines[i][1:].lstrip(" ") if len(lines[i]) > 1 else "")
            i += 1
        content = markdown.markdown("\n".join(inner), extensions=["tables", "fenced_code"])
        out.append(
            f'<div class="callout callout-{kind}"><div class="callout-title">{title}</div>{content}</div>'
        )
    return "\n".join(out)


def render(note: Path) -> Path:
    meta, body = split_frontmatter(note.read_text(encoding="utf-8"))
    title = meta.get("title") or note.stem.replace("-", " ").title()
    body = convert_callouts(resolve_wikilinks(body, note.parent))
    # Drop a leading H1 that duplicates the header title.
    body = re.sub(r"\A\s*# .*\n", "", body)
    html_body = markdown.markdown(body, extensions=["tables", "fenced_code", "toc", "sane_lists"])

    tokens = yaml.safe_load((DESIGN_DIR / "tokens.yaml").read_text(encoding="utf-8"))
    logo = DESIGN_DIR / tokens["brand"]["logo"]
    logo_tag = f'<img src="{logo.as_uri()}" alt="">' if logo.exists() else ""
    meta_line = " · ".join(
        str(v) for v in (meta.get("audience"), meta.get("status"), meta.get("date", date.today())) if v
    )
    html = f"""<!doctype html><html><head><meta charset="utf-8"><title>{title}</title></head>
<body><header class="doc-header">{logo_tag}<div><h1>{title}</h1><div class="meta">{meta_line}</div></div></header>
{html_body}</body></html>"""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUTPUT_DIR / f"{note.stem}.pdf"
    HTML(string=html, base_url=str(note.parent)).write_pdf(
        out, stylesheets=[str(DESIGN_DIR / "generated" / "print.css")]
    )
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notes", nargs="+", type=Path)
    for note in parser.parse_args().notes:
        print(f"wrote {render(note.resolve()).relative_to(VAULT_ROOT)}")


if __name__ == "__main__":
    main()
