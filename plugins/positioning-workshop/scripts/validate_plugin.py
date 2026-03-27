#!/usr/bin/env python3
"""Lightweight validator for the local Positioning Workshop plugin."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
README_PATH = PLUGIN_ROOT / "README.md"
SKILLS_ROOT = PLUGIN_ROOT / "skills"
SKILL_SPECS = {
    "positioning-workshop": [
        "evidence-file-template.md",
        "market-pressure-map-template.md",
        "route-scorecard-template.md",
        "team-pulse-template.md",
        "messaging-pack-template.md",
    ],
    "positioning-variants": [
        "variant-matrix-template.md",
    ],
}

REQUIRED_SCRIPT_FILES = [
    "validate_plugin.py",
    "bootstrap_workshop.py",
]

REQUIRED_MANIFEST_FIELDS = [
    "name",
    "version",
    "description",
    "author",
    "license",
    "keywords",
    "skills",
    "interface",
]


def load_json(path: Path) -> dict:
    with path.open() as handle:
        return json.load(handle)


def read_text(path: Path) -> str:
    with path.open() as handle:
        return handle.read()


def check(condition: bool, ok_message: str, fail_message: str, errors: list[str]) -> None:
    if condition:
        print(f"OK   {ok_message}")
    else:
        print(f"FAIL {fail_message}")
        errors.append(fail_message)


def validate_manifest(errors: list[str]) -> dict:
    check(MANIFEST_PATH.exists(), "plugin manifest exists", f"missing {MANIFEST_PATH}", errors)
    if not MANIFEST_PATH.exists():
        return {}

    try:
        payload = load_json(MANIFEST_PATH)
        print("OK   plugin manifest is valid JSON")
    except Exception as exc:  # noqa: BLE001
        errors.append(f"invalid plugin manifest JSON: {exc}")
        print(f"FAIL invalid plugin manifest JSON: {exc}")
        return {}

    for field in REQUIRED_MANIFEST_FIELDS:
        check(field in payload, f"manifest field '{field}' present", f"manifest missing '{field}'", errors)

    if payload:
        check(
            payload.get("name") == PLUGIN_ROOT.name,
            "manifest name matches plugin directory",
            "manifest name does not match plugin directory",
            errors,
        )

        prompts = payload.get("interface", {}).get("defaultPrompt", [])
        check(
            isinstance(prompts, list),
            "defaultPrompt is a list",
            "interface.defaultPrompt must be a list",
            errors,
        )
        if isinstance(prompts, list):
            check(
                len(prompts) <= 3,
                "defaultPrompt count is within UI limit",
                "interface.defaultPrompt has more than 3 entries",
                errors,
            )
            too_long = [prompt for prompt in prompts if len(prompt) > 128]
            check(
                not too_long,
                "defaultPrompt entries fit within 128 characters",
                "one or more defaultPrompt entries exceed 128 characters",
                errors,
            )

        brand_color = payload.get("interface", {}).get("brandColor")
        check(
            isinstance(brand_color, str) and re.fullmatch(r"#[0-9A-Fa-f]{6}", brand_color or ""),
            "brandColor is a hex color",
            "interface.brandColor must be a 6-digit hex color",
            errors,
        )

        skills_path = payload.get("skills")
        check(
            isinstance(skills_path, str) and skills_path == "./skills/",
            "manifest points at ./skills/",
            "manifest skills path should be './skills/'",
            errors,
        )

    return payload


def validate_readme(errors: list[str]) -> None:
    check(README_PATH.exists(), "plugin README exists", f"missing {README_PATH}", errors)


def validate_skill(errors: list[str]) -> None:
    check(SKILLS_ROOT.exists(), "skills directory exists", f"missing {SKILLS_ROOT}", errors)
    for skill_name, reference_files in SKILL_SPECS.items():
        skill_dir = SKILLS_ROOT / skill_name
        skill_path = skill_dir / "SKILL.md"
        references_dir = skill_dir / "references"

        check(skill_dir.exists(), f"skill directory '{skill_name}' exists", f"missing skill directory '{skill_name}'", errors)
        check(skill_path.exists(), f"skill '{skill_name}' has SKILL.md", f"missing {skill_path}", errors)

        if not skill_path.exists():
            continue

        skill_text = read_text(skill_path)
        check(
            skill_text.startswith("---\n"),
            f"skill '{skill_name}' starts with front matter",
            f"skill '{skill_name}' is missing YAML front matter",
            errors,
        )
        check(
            f"name: {skill_name}" in skill_text,
            f"skill '{skill_name}' front matter includes the expected name",
            f"skill '{skill_name}' front matter is missing the expected name",
            errors,
        )
        check(
            "## Workflow" in skill_text,
            f"skill '{skill_name}' includes workflow section",
            f"skill '{skill_name}' is missing the workflow section",
            errors,
        )

        check(
            references_dir.exists(),
            f"references directory for '{skill_name}' exists",
            f"missing {references_dir}",
            errors,
        )
        for filename in reference_files:
            path = references_dir / filename
            check(
                path.exists(),
                f"reference file '{skill_name}/{filename}' exists",
                f"missing reference file '{skill_name}/{filename}'",
                errors,
            )
            if path.exists():
                check(
                    path.stat().st_size > 0,
                    f"reference file '{skill_name}/{filename}' is not empty",
                    f"reference file '{skill_name}/{filename}' is empty",
                    errors,
                )


def validate_scripts(errors: list[str]) -> None:
    scripts_dir = PLUGIN_ROOT / "scripts"
    check(scripts_dir.exists(), "scripts directory exists", f"missing {scripts_dir}", errors)
    for filename in REQUIRED_SCRIPT_FILES:
        path = scripts_dir / filename
        check(path.exists(), f"script '{filename}' exists", f"missing script '{filename}'", errors)
        if path.exists():
            check(path.stat().st_size > 0, f"script '{filename}' is not empty", f"script '{filename}' is empty", errors)


def main() -> int:
    errors: list[str] = []

    print(f"Validating plugin at {PLUGIN_ROOT}")
    validate_manifest(errors)
    validate_readme(errors)
    validate_skill(errors)
    validate_scripts(errors)

    if errors:
        print(f"\nValidation failed with {len(errors)} issue(s).")
        return 1

    print("\nValidation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
