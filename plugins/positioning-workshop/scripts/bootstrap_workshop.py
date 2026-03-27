#!/usr/bin/env python3
"""Create a workshop folder from the reference templates."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
REFERENCES_DIR = PLUGIN_ROOT / "skills" / "positioning-workshop" / "references"
DEFAULT_WORKSHOPS_DIR = PLUGIN_ROOT / "workshops"

TEMPLATE_MAP = [
    ("evidence-file-template.md", "01-evidence-file.md"),
    ("market-pressure-map-template.md", "02-market-pressure-map.md"),
    ("route-scorecard-template.md", "03-route-scorecard.md"),
    ("team-pulse-template.md", "04-team-pulse-packet.md"),
    ("messaging-pack-template.md", "05-messaging-pack.md"),
]


def slugify(value: str) -> str:
    slug = value.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "workshop"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bootstrap a new positioning workshop folder.")
    parser.add_argument("company_name", help="Human-readable company name")
    parser.add_argument(
        "--output",
        default=str(DEFAULT_WORKSHOPS_DIR),
        help="Parent directory where the workshop folder should be created",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite an existing workshop folder")
    return parser.parse_args()


def render_session_readme(company_name: str, slug: str) -> str:
    return f"""# {company_name} Workshop

- Slug: `{slug}`
- Status: draft
- Owner:
- Date:

## Suggested flow

1. Fill in `01-evidence-file.md`
2. Build `02-market-pressure-map.md`
3. Compare routes in `03-route-scorecard.md`
4. Send `04-team-pulse-packet.md`
5. Finalize `05-messaging-pack.md`

## Notes

- Keep proof and bets separate.
- Make one primary decision per strategic axis.
- Revise the messaging pack only after route selection.
"""


def ensure_templates_exist() -> None:
    missing = [source for source, _ in TEMPLATE_MAP if not (REFERENCES_DIR / source).exists()]
    if missing:
        joined = ", ".join(missing)
        raise FileNotFoundError(f"Missing reference templates: {joined}")


def write_file(path: Path, text: str, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"{path} already exists. Use --force to overwrite.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def main() -> int:
    args = parse_args()
    ensure_templates_exist()

    company_name = args.company_name.strip()
    slug = slugify(company_name)
    output_dir = Path(args.output).expanduser().resolve() / slug

    if output_dir.exists() and not args.force:
        print(f"Workshop folder already exists: {output_dir}", file=sys.stderr)
        print("Use --force to overwrite.", file=sys.stderr)
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)

    session_readme = output_dir / "README.md"
    write_file(session_readme, render_session_readme(company_name, slug), args.force)
    print(f"Created {session_readme}")

    for source_name, target_name in TEMPLATE_MAP:
        source_path = REFERENCES_DIR / source_name
        target_path = output_dir / target_name
        template_text = source_path.read_text()
        title = f"# {company_name}: {target_name.replace('.md', '').replace('-', ' ').title()}\n\n"
        write_file(target_path, title + template_text, args.force)
        print(f"Created {target_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
