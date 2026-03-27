#!/usr/bin/env python3
"""Positioning Workshop MCP server for Claude Desktop."""

from __future__ import annotations

import json
import mimetypes
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


SERVER_NAME = "positioning-workshop"
SERVER_TITLE = "Positioning Workshop"
SERVER_VERSION = "0.2.0"
PROTOCOL_VERSION = "2025-06-18"
URI_SCHEME = "positioning-workshop"
ALLOWED_RESOURCE_SUFFIXES = {".md", ".json"}

SCRIPT_PATH = Path(__file__).resolve()
EXTENSION_ROOT = SCRIPT_PATH.parents[1]
BUNDLE_ROOT = EXTENSION_ROOT / "bundle"
PLUGIN_ROOT = EXTENSION_ROOT.parents[1]
REPO_ROOT = PLUGIN_ROOT.parents[1]

STATIC_SINGLE_FILES: List[Tuple[str, str]] = [
    ("plugin/README.md", "Core plugin overview and local workflow."),
    ("docs/artifact-pipeline.md", "Artifact persistence model and source-of-truth rules."),
    ("docs/plugin-spec.md", "Product scope, workflow, and output contract."),
    ("docs/product-principles.md", "Product principles and design intent."),
    ("docs/roadmap.md", "Roadmap and upcoming priorities."),
    ("docs/validation-notes-mercuryo.md", "Notes from the Mercuryo validation run."),
]

STATIC_TREE_ROOTS: List[Tuple[str, str]] = [
    ("skills", "Skill definitions and reference templates."),
    ("examples/incidentbridge", "Filled fictional example workshop."),
    ("workshops/mercuryo-io", "Validated public-company workshop reference."),
]

TEMPLATE_MAP = [
    ("skills/positioning-workshop/references/evidence-file-template.md", Path("01-evidence-file.md")),
    ("skills/positioning-workshop/references/market-pressure-map-template.md", Path("02-market-pressure-map.md")),
    ("skills/positioning-workshop/references/route-scorecard-template.md", Path("03-route-scorecard.md")),
    ("skills/positioning-workshop/references/team-pulse-template.md", Path("04-team-pulse-packet.md")),
    ("skills/positioning-workshop/references/messaging-pack-template.md", Path("05-messaging-pack.md")),
    ("skills/positioning-workshop/references/decision-log-template.md", Path("artifacts/decision-log.md")),
    ("skills/positioning-workshop/references/workshop-summary-template.json", Path("artifacts/workshop-summary.json")),
    ("skills/positioning-workshop/references/claim-ledger-template.json", Path("artifacts/claim-ledger.json")),
    ("skills/positioning-workshop/references/route-recommendation-template.md", Path("artifacts/route-recommendation.md")),
]


def slugify(value: str) -> str:
    slug = value.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "workshop"


def workshops_root() -> Path:
    configured = os.environ.get("POSITIONING_WORKSHOP_DATA_DIR", "").strip()
    if configured:
        return Path(configured).expanduser()
    return Path.home() / "Documents" / "positioning-workshop-workshops"


def ensure_workshops_root() -> Path:
    root = workshops_root()
    root.mkdir(parents=True, exist_ok=True)
    return root


def resolve_static_path(logical_path: str) -> Path:
    relative_path = Path(logical_path)
    if BUNDLE_ROOT.exists():
        return BUNDLE_ROOT / relative_path

    top_level = relative_path.parts[0]
    remainder = Path(*relative_path.parts[1:]) if len(relative_path.parts) > 1 else Path()
    if top_level == "plugin":
        return PLUGIN_ROOT / remainder
    if top_level == "docs":
        return REPO_ROOT / relative_path
    if top_level in {"skills", "examples", "workshops"}:
        return PLUGIN_ROOT / relative_path
    raise FileNotFoundError(f"Unsupported static resource path: {logical_path}")


def guess_mime_type(path_str: str) -> str:
    path = Path(path_str)
    if path.suffix == ".md":
        return "text/markdown"
    if path.suffix == ".json":
        return "application/json"
    return mimetypes.guess_type(path.name)[0] or "text/plain"


def iso_timestamp(path: Path) -> str:
    modified = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    return modified.isoformat().replace("+00:00", "Z")


def safe_relative_path(relative_path: str) -> Path:
    path = Path(relative_path)
    if path.is_absolute():
        raise ValueError("relative_path must be relative to the workshop directory")
    if ".." in path.parts:
        raise ValueError("relative_path must not traverse upward")
    return path


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
5. Lock the route in `artifacts/route-recommendation.md`
6. Update `artifacts/decision-log.md`, `artifacts/workshop-summary.json`, and `artifacts/claim-ledger.json`
7. Finalize `05-messaging-pack.md`

## Artifact source of truth

- `artifacts/decision-log.md`: records the main strategic choices and why they won.
- `artifacts/workshop-summary.json`: compact workshop state for resuming later work.
- `artifacts/claim-ledger.json`: machine-readable list of approved claims and confidence levels.
- `artifacts/route-recommendation.md`: final route call with objections and next tests.

## Notes

- Keep proof and bets separate.
- Make one primary decision per strategic axis.
- Treat `artifacts/` as the source of truth for future edits and variants.
- Revise the messaging pack only after route selection.
"""


def render_template_text(template_text: str, company_name: str, slug: str) -> str:
    return template_text.replace("__COMPANY_NAME__", company_name).replace("__WORKSHOP_SLUG__", slug)


def strip_leading_heading(template_text: str) -> str:
    lines = template_text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        if lines and lines[0] == "":
            lines = lines[1:]
    return "\n".join(lines).strip()


def render_output_text(company_name: str, slug: str, target_path: Path, template_text: str) -> str:
    rendered = render_template_text(template_text, company_name, slug)
    if target_path.suffix == ".json":
        return rendered.rstrip() + "\n"

    title = target_path.stem.replace("-", " ").title()
    body = strip_leading_heading(rendered)
    return f"# {company_name}: {title}\n\n{body}\n"


def write_text_file(path: Path, text: str, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"{path} already exists. Pass overwrite=true to replace it.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def humanize_static_name(logical_path: str) -> str:
    parts = Path(logical_path).parts
    label_map = {
        "plugin": "Plugin",
        "docs": "Docs",
        "skills": "Skills",
        "examples": "Examples",
        "workshops": "Reference Workshops",
    }
    section = label_map.get(parts[0], "Resource")
    suffix = " / ".join(parts[1:]) if len(parts) > 1 else logical_path
    return f"{section} / {suffix}"


def static_resource_descriptor(logical_path: str, description: str) -> Dict[str, Any]:
    return {
        "uri": f"{URI_SCHEME}://static/{logical_path}",
        "name": humanize_static_name(logical_path),
        "description": description,
        "mimeType": guess_mime_type(logical_path),
    }


def iter_static_resources() -> Iterable[Dict[str, Any]]:
    seen: set[str] = set()
    for logical_path, description in STATIC_SINGLE_FILES:
        path = resolve_static_path(logical_path)
        if path.exists():
            seen.add(logical_path)
            yield static_resource_descriptor(logical_path, description)

    for logical_root, description in STATIC_TREE_ROOTS:
        root = resolve_static_path(logical_root)
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.suffix not in ALLOWED_RESOURCE_SUFFIXES:
                continue
            logical_path = str(Path(logical_root) / path.relative_to(root)).replace(os.sep, "/")
            if logical_path in seen:
                continue
            seen.add(logical_path)
            yield static_resource_descriptor(logical_path, description)


def iter_workshop_resources() -> Iterable[Dict[str, Any]]:
    root = workshops_root()
    if not root.exists():
        return []

    resources: List[Dict[str, Any]] = []
    for workshop_dir in sorted(root.iterdir()):
        if not workshop_dir.is_dir():
            continue
        for path in sorted(workshop_dir.rglob("*")):
            if not path.is_file() or path.suffix not in ALLOWED_RESOURCE_SUFFIXES:
                continue
            relative_path = path.relative_to(workshop_dir).as_posix()
            resources.append(
                {
                    "uri": f"{URI_SCHEME}://workshops/{workshop_dir.name}/{relative_path}",
                    "name": f"Workshops / {workshop_dir.name} / {relative_path}",
                    "description": "User workshop file stored in the writable workshop directory.",
                    "mimeType": guess_mime_type(relative_path),
                }
            )
    return resources


def list_resources() -> List[Dict[str, Any]]:
    return list(iter_static_resources()) + list(iter_workshop_resources())


def read_resource(uri: str) -> Dict[str, Any]:
    static_prefix = f"{URI_SCHEME}://static/"
    workshop_prefix = f"{URI_SCHEME}://workshops/"

    if uri.startswith(static_prefix):
        logical_path = uri[len(static_prefix) :]
        path = resolve_static_path(logical_path)
    elif uri.startswith(workshop_prefix):
        remainder = uri[len(workshop_prefix) :]
        if "/" not in remainder:
            raise ValueError("Workshop resource URIs must include workshop slug and file path")
        slug, relative_path = remainder.split("/", 1)
        path = ensure_workshops_root() / slug / safe_relative_path(relative_path)
    else:
        raise ValueError(f"Unsupported resource URI: {uri}")

    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"Resource not found: {uri}")

    text = path.read_text(encoding="utf-8")
    return {
        "contents": [
            {
                "uri": uri,
                "mimeType": guess_mime_type(path.name),
                "text": text,
            }
        ]
    }


def make_tool_result(text: str, structured: Dict[str, Any], is_error: bool = False) -> Dict[str, Any]:
    return {
        "content": [
            {
                "type": "text",
                "text": text,
            }
        ],
        "structuredContent": structured,
        "isError": is_error,
    }


def tool_bootstrap_workshop(arguments: Dict[str, Any]) -> Dict[str, Any]:
    company_name = str(arguments.get("company_name", "")).strip()
    if not company_name:
        return make_tool_result(
            "Missing required field `company_name`.",
            {"error": "missing_company_name"},
            is_error=True,
        )

    force = bool(arguments.get("force", False))
    slug = slugify(company_name)
    root = ensure_workshops_root()
    workshop_dir = root / slug
    created_files: List[str] = []

    try:
        if workshop_dir.exists() and not force:
            raise FileExistsError(f"Workshop already exists at {workshop_dir}")

        workshop_dir.mkdir(parents=True, exist_ok=True)
        session_readme = workshop_dir / "README.md"
        write_text_file(session_readme, render_session_readme(company_name, slug), force)
        created_files.append(str(session_readme))

        for source_logical_path, relative_target in TEMPLATE_MAP:
            template_text = resolve_static_path(source_logical_path).read_text(encoding="utf-8")
            rendered = render_output_text(company_name, slug, relative_target, template_text)
            target_path = workshop_dir / relative_target
            write_text_file(target_path, rendered, force)
            created_files.append(str(target_path))
    except (FileExistsError, FileNotFoundError) as exc:
        return make_tool_result(str(exc), {"error": type(exc).__name__, "workshop_slug": slug}, is_error=True)

    return make_tool_result(
        f"Created workshop `{slug}` at {workshop_dir}.",
        {
            "company_name": company_name,
            "workshop_slug": slug,
            "workshop_dir": str(workshop_dir),
            "created_files": created_files,
        },
    )


def tool_list_workshops(arguments: Dict[str, Any]) -> Dict[str, Any]:
    _ = arguments
    root = ensure_workshops_root()
    workshops: List[Dict[str, Any]] = []
    for workshop_dir in sorted(root.iterdir()):
        if not workshop_dir.is_dir():
            continue
        artifacts_dir = workshop_dir / "artifacts"
        workshops.append(
            {
                "slug": workshop_dir.name,
                "path": str(workshop_dir),
                "has_route_recommendation": (artifacts_dir / "route-recommendation.md").exists(),
                "has_workshop_summary": (artifacts_dir / "workshop-summary.json").exists(),
                "has_claim_ledger": (artifacts_dir / "claim-ledger.json").exists(),
                "updated_at": iso_timestamp(workshop_dir),
            }
        )

    if workshops:
        lines = [f"Found {len(workshops)} workshop(s) in {root}:"]
        lines.extend(f"- {item['slug']} ({item['updated_at']})" for item in workshops)
        text = "\n".join(lines)
    else:
        text = f"No workshops found yet in {root}."

    return make_tool_result(
        text,
        {
            "workshops_root": str(root),
            "workshops": workshops,
        },
    )


def tool_save_workshop_file(arguments: Dict[str, Any]) -> Dict[str, Any]:
    workshop_slug = str(arguments.get("workshop_slug", "")).strip()
    relative_path = str(arguments.get("relative_path", "")).strip()
    content = arguments.get("content", "")
    overwrite = bool(arguments.get("overwrite", False))

    if not workshop_slug:
        return make_tool_result("Missing required field `workshop_slug`.", {"error": "missing_workshop_slug"}, True)
    if not relative_path:
        return make_tool_result("Missing required field `relative_path`.", {"error": "missing_relative_path"}, True)
    if not isinstance(content, str):
        return make_tool_result("`content` must be a string.", {"error": "invalid_content_type"}, True)

    try:
        safe_path = safe_relative_path(relative_path)
    except ValueError as exc:
        return make_tool_result(str(exc), {"error": "invalid_relative_path"}, True)

    workshop_dir = ensure_workshops_root() / workshop_slug
    if not workshop_dir.exists():
        return make_tool_result(
            f"Workshop `{workshop_slug}` does not exist. Run bootstrap_workshop first.",
            {"error": "missing_workshop", "workshop_slug": workshop_slug},
            True,
        )

    if safe_path.suffix == ".json":
        try:
            json.loads(content)
        except json.JSONDecodeError as exc:
            return make_tool_result(
                f"Invalid JSON for `{relative_path}`: {exc}",
                {"error": "invalid_json", "relative_path": relative_path},
                True,
            )

    target_path = workshop_dir / safe_path
    try:
        write_text_file(target_path, content.rstrip() + "\n", overwrite)
    except FileExistsError as exc:
        return make_tool_result(str(exc), {"error": "file_exists", "relative_path": relative_path}, True)

    return make_tool_result(
        f"Saved `{relative_path}` in workshop `{workshop_slug}`.",
        {
            "workshop_slug": workshop_slug,
            "path": str(target_path),
            "bytes_written": len(content.encode("utf-8")),
        },
    )


def list_tools() -> List[Dict[str, Any]]:
    return [
        {
            "name": "bootstrap_workshop",
            "title": "Bootstrap Workshop",
            "description": "Create a new workshop folder with the standard templates and artifact files.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "type": "string",
                        "description": "Human-readable company name for the workshop.",
                    },
                    "force": {
                        "type": "boolean",
                        "description": "Overwrite an existing workshop folder with the same slug.",
                        "default": False,
                    },
                },
                "required": ["company_name"],
            },
            "outputSchema": {
                "type": "object",
                "properties": {
                    "company_name": {"type": "string"},
                    "workshop_slug": {"type": "string"},
                    "workshop_dir": {"type": "string"},
                    "created_files": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                },
                "required": ["workshop_slug", "workshop_dir", "created_files"],
            },
        },
        {
            "name": "list_workshops",
            "title": "List Workshops",
            "description": "List saved workshops in the writable workshop directory.",
            "inputSchema": {
                "type": "object",
                "properties": {},
            },
            "outputSchema": {
                "type": "object",
                "properties": {
                    "workshops_root": {"type": "string"},
                    "workshops": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "slug": {"type": "string"},
                                "path": {"type": "string"},
                                "has_route_recommendation": {"type": "boolean"},
                                "has_workshop_summary": {"type": "boolean"},
                                "has_claim_ledger": {"type": "boolean"},
                                "updated_at": {"type": "string"},
                            },
                            "required": ["slug", "path", "updated_at"],
                        },
                    },
                },
                "required": ["workshops_root", "workshops"],
            },
        },
        {
            "name": "save_workshop_file",
            "title": "Save Workshop File",
            "description": "Write or update a markdown or JSON file inside a saved workshop.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "workshop_slug": {
                        "type": "string",
                        "description": "Workshop slug returned by bootstrap_workshop or list_workshops.",
                    },
                    "relative_path": {
                        "type": "string",
                        "description": "Relative path inside the workshop folder, such as `05-messaging-pack.md` or `artifacts/workshop-summary.json`.",
                    },
                    "content": {
                        "type": "string",
                        "description": "Full file content to write.",
                    },
                    "overwrite": {
                        "type": "boolean",
                        "description": "Replace an existing file when true.",
                        "default": False,
                    },
                },
                "required": ["workshop_slug", "relative_path", "content"],
            },
            "outputSchema": {
                "type": "object",
                "properties": {
                    "workshop_slug": {"type": "string"},
                    "path": {"type": "string"},
                    "bytes_written": {"type": "number"},
                },
                "required": ["workshop_slug", "path", "bytes_written"],
            },
        },
    ]


def call_tool(name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    if name == "bootstrap_workshop":
        return tool_bootstrap_workshop(arguments)
    if name == "list_workshops":
        return tool_list_workshops(arguments)
    if name == "save_workshop_file":
        return tool_save_workshop_file(arguments)
    return make_tool_result(f"Unknown tool: {name}", {"error": "unknown_tool", "name": name}, is_error=True)


def list_prompts() -> List[Dict[str, Any]]:
    return [
        {
            "name": "run_positioning_workshop",
            "title": "Run Positioning Workshop",
            "description": "Start or resume a full evidence-first positioning workshop.",
            "arguments": [
                {
                    "name": "company_name",
                    "description": "Human-readable company name.",
                    "required": True,
                },
                {
                    "name": "goal",
                    "description": "What the team most wants to clarify or improve.",
                    "required": False,
                },
                {
                    "name": "source_material",
                    "description": "Links, notes, decks, or a short summary of available source material.",
                    "required": False,
                },
            ],
        },
        {
            "name": "adapt_positioning_variants",
            "title": "Adapt Positioning Variants",
            "description": "Adapt an approved positioning spine for segments, personas, channels, or sales stages.",
            "arguments": [
                {
                    "name": "workshop_slug",
                    "description": "Slug of an existing workshop to use as the source of truth.",
                    "required": True,
                },
                {
                    "name": "adaptation_axis",
                    "description": "The axis to adapt across, such as segment, persona, channel, or sales stage.",
                    "required": False,
                },
                {
                    "name": "target_context",
                    "description": "Specific target contexts or audiences for the variants.",
                    "required": False,
                },
            ],
        },
    ]


def get_prompt(name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    if name == "run_positioning_workshop":
        company_name = str(arguments.get("company_name", "")).strip() or "Unknown Company"
        goal = str(arguments.get("goal", "")).strip() or "Choose one believable market position with reusable outputs."
        source_material = str(arguments.get("source_material", "")).strip() or "No source material was provided yet."
        prompt_text = f"""Run the Positioning Workshop for {company_name}.

Start by checking whether a workshop already exists with `list_workshops`.
If none exists, call `bootstrap_workshop` for `{company_name}` before drafting outputs.

Use the following built-in resources as needed:
- `skills/positioning-workshop/SKILL.md`
- the reference templates under `skills/positioning-workshop/references/`
- the IncidentBridge example
- the Mercuryo validation workshop if you need a higher-fidelity benchmark

User goal:
{goal}

Available source material:
{source_material}

Workflow rules:
- Work evidence-first.
- Keep proof, support, and bets separate.
- Treat saved artifact files as the source of truth once they exist.
- Save durable outputs back into the workshop files, especially:
  - `artifacts/decision-log.md`
  - `artifacts/workshop-summary.json`
  - `artifacts/claim-ledger.json`
  - `artifacts/route-recommendation.md`
- Finalize `05-messaging-pack.md` only after route selection is clear.
"""
    elif name == "adapt_positioning_variants":
        workshop_slug = str(arguments.get("workshop_slug", "")).strip() or "unknown-workshop"
        adaptation_axis = str(arguments.get("adaptation_axis", "")).strip() or "segment or channel"
        target_context = str(arguments.get("target_context", "")).strip() or "No specific target context was provided."
        prompt_text = f"""Adapt the approved positioning for workshop `{workshop_slug}`.

First read the workshop source-of-truth files before writing variants:
- `artifacts/route-recommendation.md`
- `artifacts/workshop-summary.json`
- `artifacts/claim-ledger.json`
- `05-messaging-pack.md`

Then use:
- `skills/positioning-variants/SKILL.md`
- `skills/positioning-variants/references/variant-matrix-template.md`

Adaptation axis:
{adaptation_axis}

Target context:
{target_context}

Rules:
- Keep buyer priority, category choice, wedge, proof boundary, and explicit boundary stable unless the user explicitly wants to reposition.
- Change emphasis before changing meaning.
- Mark any new stretch as a bet.
- Save the resulting variant pack into the relevant workshop files if the user asks for persistence.
"""
    else:
        raise ValueError(f"Unknown prompt: {name}")

    return {
        "description": f"Prompt for {name}",
        "messages": [
            {
                "role": "user",
                "content": {
                    "type": "text",
                    "text": prompt_text,
                },
            }
        ],
    }


def make_success_response(request_id: Any, result: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "result": result,
    }


def make_error_response(request_id: Any, code: int, message: str) -> Dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "error": {
            "code": code,
            "message": message,
        },
    }


def read_message() -> Dict[str, Any] | None:
    headers: Dict[str, str] = {}
    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        if line in {b"\r\n", b"\n"}:
            break
        decoded = line.decode("utf-8").strip()
        if not decoded:
            break
        key, _, value = decoded.partition(":")
        headers[key.lower()] = value.strip()

    length_text = headers.get("content-length")
    if not length_text:
        return None

    body = sys.stdin.buffer.read(int(length_text))
    if not body:
        return None
    return json.loads(body.decode("utf-8"))


def write_message(payload: Dict[str, Any]) -> None:
    body = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    sys.stdout.buffer.write(f"Content-Length: {len(body)}\r\n\r\n".encode("ascii"))
    sys.stdout.buffer.write(body)
    sys.stdout.buffer.flush()


def handle_request(message: Dict[str, Any]) -> Dict[str, Any] | None:
    method = message.get("method")
    params = message.get("params") or {}
    request_id = message.get("id")

    if method == "notifications/initialized":
        return None

    if method == "initialize":
        return make_success_response(
            request_id,
            {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {
                    "tools": {"listChanged": False},
                    "prompts": {"listChanged": False},
                    "resources": {"subscribe": False, "listChanged": True},
                },
                "serverInfo": {
                    "name": SERVER_NAME,
                    "title": SERVER_TITLE,
                    "version": SERVER_VERSION,
                },
                "instructions": (
                    "Use built-in resources for the workshop method and examples. "
                    "Use bootstrap_workshop to create new sessions, list_workshops to resume existing work, "
                    "and save_workshop_file to persist markdown or JSON outputs."
                ),
            },
        )

    if method == "ping":
        return make_success_response(request_id, {})

    try:
        if method == "tools/list":
            return make_success_response(request_id, {"tools": list_tools()})
        if method == "tools/call":
            name = str(params.get("name", "")).strip()
            arguments = params.get("arguments") or {}
            return make_success_response(request_id, call_tool(name, arguments))
        if method == "prompts/list":
            return make_success_response(request_id, {"prompts": list_prompts()})
        if method == "prompts/get":
            name = str(params.get("name", "")).strip()
            arguments = params.get("arguments") or {}
            return make_success_response(request_id, get_prompt(name, arguments))
        if method == "resources/list":
            return make_success_response(request_id, {"resources": list_resources()})
        if method == "resources/read":
            uri = str(params.get("uri", "")).strip()
            return make_success_response(request_id, read_resource(uri))
        if method == "resources/templates/list":
            return make_success_response(request_id, {"resourceTemplates": []})
    except Exception as exc:  # noqa: BLE001
        return make_error_response(request_id, -32000, str(exc))

    return make_error_response(request_id, -32601, f"Method not found: {method}")


def main() -> int:
    while True:
        message = read_message()
        if message is None:
            return 0
        response = handle_request(message)
        if response is not None and message.get("id") is not None:
            write_message(response)


if __name__ == "__main__":
    sys.exit(main())
