#!/usr/bin/env python3

from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ENTRIES = ROOT / "entries"
README = ROOT / "README.md"
REQUIRED_SCALARS = {
    "added",
    "category",
    "category_label",
    "category_order",
    "list",
    "name",
    "slug",
    "tagline",
    "url",
}


def parse_entry(path: Path) -> tuple[dict[str, str], list[str]]:
    scalars: dict[str, str] = {}
    tags: list[str] = []
    active_list = ""
    active_scalar = ""
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("- "):
            if active_list != "tags":
                raise ValueError(f"{path}: unexpected list item")
            tags.append(line[2:].strip())
            continue
        if line.startswith((" ", "\t")):
            if not active_scalar:
                raise ValueError(f"{path}: unexpected continuation")
            scalars[active_scalar] = f"{scalars[active_scalar]} {line.strip()}"
            continue
        if ":" not in line:
            raise ValueError(f"{path}: unsupported YAML structure")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        if key == "tags":
            active_list = key
            active_scalar = ""
            continue
        active_list = ""
        if key in scalars:
            raise ValueError(f"{path}: duplicate key {key}")
        scalars[key] = value
        active_scalar = key
    return scalars, tags


def validate_entry(path: Path, readme: str) -> tuple[str, str]:
    values, tags = parse_entry(path)
    missing = REQUIRED_SCALARS.difference(values)
    if missing:
        raise ValueError(f"{path}: missing {', '.join(sorted(missing))}")
    slug = values["slug"]
    url = values["url"]
    if slug != path.stem:
        raise ValueError(f"{path}: slug must match filename")
    if values["list"] != "mcp-servers":
        raise ValueError(f"{path}: list must be mcp-servers")
    if not values["category_order"].isdigit():
        raise ValueError(f"{path}: category_order must be an integer")
    date.fromisoformat(values["added"])
    if any(not tag for tag in tags):
        raise ValueError(f"{path}: tags cannot contain empty values")
    if f"]({url})" not in readme:
        raise ValueError(f"{path}: README is missing {url}")
    return slug, url


def reject_duplicates(label: str, values: list[str]) -> None:
    duplicates = sorted(value for value, count in Counter(values).items() if count > 1)
    if duplicates:
        raise ValueError(f"duplicate {label}: {', '.join(duplicates)}")


def main() -> None:
    readme = README.read_text(encoding="utf-8")
    validated = [validate_entry(path, readme) for path in sorted(ENTRIES.glob("*.yaml"))]
    reject_duplicates("slugs", [slug for slug, _ in validated])
    reject_duplicates("URLs", [url for _, url in validated])
    print(f"Validated {len(validated)} MCP entries.")


if __name__ == "__main__":
    main()
