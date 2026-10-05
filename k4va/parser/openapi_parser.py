import json
from pathlib import Path
from typing import Any

import yaml


class OpenAPIParseError(ValueError):
    """Raised when a document cannot be loaded or is not an OpenAPI contract."""


def parse_openapi(path: str | Path) -> dict[str, Any]:
    source = Path(path)
    try:
        raw = source.read_text(encoding="utf-8")
    except OSError as exc:
        raise OpenAPIParseError(f"Could not read {source}: {exc}") from exc
    try:
        document = json.loads(raw) if source.suffix.lower() == ".json" else yaml.safe_load(raw)
    except (json.JSONDecodeError, yaml.YAMLError) as exc:
        raise OpenAPIParseError(f"Invalid YAML or JSON in {source}: {exc}") from exc
    if not isinstance(document, dict):
        raise OpenAPIParseError("The document must contain an object at its root.")
    version = document.get("openapi")
    if not isinstance(version, str) or not (version.startswith("3.0") or version.startswith("3.1")):
        raise OpenAPIParseError("K4VA Community supports OpenAPI 3.0.x and 3.1.x documents.")
    if not isinstance(document.get("info"), dict) or not isinstance(document.get("paths"), dict):
        raise OpenAPIParseError("An OpenAPI document must include object fields: info and paths.")
    return document
