#!/usr/bin/env python3
"""Build an installable Claude Desktop MCP bundle for Positioning Workshop."""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PLUGIN_ROOT.parents[1]
EXTENSION_ROOT = PLUGIN_ROOT / "integrations" / "claude-extension"
DIST_ROOT = PLUGIN_ROOT / "dist"
CODEX_MANIFEST_PATH = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
CLAUDE_MANIFEST_PATH = EXTENSION_ROOT / "manifest.json"


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def ensure_clean_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def copy_tree(source: Path, destination: Path) -> None:
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination)


def copy_extension_source(staging_root: Path) -> None:
    copy_file(EXTENSION_ROOT / "manifest.json", staging_root / "manifest.json")
    copy_file(EXTENSION_ROOT / "README.md", staging_root / "README.md")
    copy_tree(EXTENSION_ROOT / "server", staging_root / "server")


def copy_bundle_content(staging_root: Path) -> None:
    bundle_root = staging_root / "bundle"
    copy_file(PLUGIN_ROOT / "README.md", bundle_root / "plugin" / "README.md")
    if (PLUGIN_ROOT / "assets").exists():
        copy_tree(PLUGIN_ROOT / "assets", bundle_root / "plugin" / "assets")
    copy_tree(REPO_ROOT / "docs", bundle_root / "docs")
    copy_tree(PLUGIN_ROOT / "skills", bundle_root / "skills")
    copy_tree(PLUGIN_ROOT / "examples" / "incidentbridge", bundle_root / "examples" / "incidentbridge")


def create_archive(staging_root: Path, output_path: Path) -> None:
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(staging_root.rglob("*")):
            if path.is_dir():
                continue
            archive.write(path, path.relative_to(staging_root))


def main() -> int:
    codex_manifest = load_json(CODEX_MANIFEST_PATH)
    claude_manifest = load_json(CLAUDE_MANIFEST_PATH)
    version = claude_manifest.get("version")
    if version != codex_manifest.get("version"):
        print("Claude manifest version must match Codex plugin version.", file=sys.stderr)
        return 1

    DIST_ROOT.mkdir(parents=True, exist_ok=True)
    artifact_stem = f"{PLUGIN_ROOT.name}-claude-extension-v{version}"
    mcpb_path = DIST_ROOT / f"{artifact_stem}.mcpb"
    dxt_path = DIST_ROOT / f"{artifact_stem}.dxt"

    with tempfile.TemporaryDirectory(prefix="positioning-workshop-mcpb-") as temp_dir:
        staging_root = Path(temp_dir) / "package"
        ensure_clean_dir(staging_root)
        copy_extension_source(staging_root)
        copy_bundle_content(staging_root)
        create_archive(staging_root, mcpb_path)
        shutil.copyfile(mcpb_path, dxt_path)

    print(f"Built Claude Desktop bundle: {mcpb_path}")
    print(f"Built Claude Desktop compatibility bundle: {dxt_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
