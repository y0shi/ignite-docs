"""Render design-system CSS for every output format from tokens.yaml."""

import shutil
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

DESIGN_DIR = Path(__file__).resolve().parent
VAULT_ROOT = DESIGN_DIR.parent.parent
OUTPUTS = ("mkdocs.css", "print.css", "marp-theme.css", "obsidian-snippet.css")


def load_tokens() -> dict:
    return yaml.safe_load((DESIGN_DIR / "tokens.yaml").read_text(encoding="utf-8"))


def main() -> None:
    tokens = load_tokens()
    env = Environment(loader=FileSystemLoader(DESIGN_DIR / "templates"), undefined=StrictUndefined)
    out_dir = DESIGN_DIR / "generated"
    out_dir.mkdir(exist_ok=True)
    for name in OUTPUTS:
        (out_dir / name).write_text(env.get_template(f"{name}.j2").render(**tokens), encoding="utf-8")
        print(f"wrote generated/{name}")
    snippet_dir = VAULT_ROOT / ".obsidian" / "snippets"
    snippet_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(out_dir / "obsidian-snippet.css", snippet_dir / "ignite.css")
    print("synced .obsidian/snippets/ignite.css")


if __name__ == "__main__":
    main()
