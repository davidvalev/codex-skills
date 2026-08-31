#!/usr/bin/env python3
"""Validate the deliverable contract for create-token-chat-brand."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_FILES = (
    "README.md",
    "assumptions.md",
    "manifest.json",
    "qa-report.md",
    "brand/brand-strategy.md",
    "brand/voice-and-messaging.md",
    "brand/palette.json",
    "brand/typography.md",
    "brand/logo-primary.svg",
    "brand/logo-mark.svg",
    "brand/logo-mono-dark.svg",
    "brand/logo-mono-light.svg",
    "brand/favicon.svg",
    "content/site-copy.md",
    "content/ui-copy.md",
    "content/chat-persona.md",
    "content/transactional-emails.md",
    "content/seo-metadata.csv",
    "images/hero.png",
    "images/hero.webp",
    "images/feature-01.svg",
    "images/feature-02.svg",
    "images/feature-03.svg",
    "images/feature-04.svg",
    "images/token-pack-01.png",
    "images/token-pack-01.webp",
    "images/token-pack-02.png",
    "images/token-pack-02.webp",
    "images/token-pack-03.png",
    "images/token-pack-03.webp",
    "images/social-share.png",
    "images/social-share.webp",
    "images/generation-prompts.md",
    "brandbook/brandbook.md",
    "brandbook/brandbook.pdf",
)

TEXT_SUFFIXES = {".md", ".csv", ".json", ".svg"}
LEAK_PATTERNS = {
    "unfinished marker": re.compile(r"\b(?:TODO|TBD|FIXME|LOREM IPSUM)\b", re.IGNORECASE),
    "machine-specific path": re.compile(r"/(?:Users|home)/[^/\s]+/"),
}

PALETTE_KEYS = {
    "primary",
    "secondary",
    "accent",
    "background",
    "surface",
    "text",
    "muted_text",
    "border",
    "success",
    "warning",
    "error",
    "focus",
    "hero_overlay",
    "contrast_pairs",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package_dir", type=Path, help="Generated brand package directory")
    return parser.parse_args()


def read_json(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"Cannot parse {path}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"Expected a JSON object in {path}")
        return {}
    return value


def validate_magic(path: Path, errors: list[str]) -> None:
    data = path.read_bytes()[:16]
    suffix = path.suffix.lower()
    if suffix == ".pdf" and not data.startswith(b"%PDF-"):
        errors.append(f"Not a valid PDF header: {path}")
    elif suffix == ".png" and not data.startswith(b"\x89PNG\r\n\x1a\n"):
        errors.append(f"Not a valid PNG header: {path}")
    elif suffix == ".webp" and not (data.startswith(b"RIFF") and data[8:12] == b"WEBP"):
        errors.append(f"Not a valid WebP header: {path}")


def main() -> int:
    args = parse_args()
    root = args.package_dir.expanduser().resolve()
    errors: list[str] = []

    if not root.is_dir():
        print(f"ERROR: package directory does not exist: {root}", file=sys.stderr)
        return 2

    for relative in REQUIRED_FILES:
        path = root / relative
        if not path.is_file():
            errors.append(f"Missing required file: {relative}")
        elif path.stat().st_size == 0:
            errors.append(f"Empty required file: {relative}")
        elif path.suffix.lower() in {".pdf", ".png", ".webp"}:
            validate_magic(path, errors)

    manifest_path = root / "manifest.json"
    manifest = read_json(manifest_path, errors) if manifest_path.is_file() else {}
    brand_name = manifest.get("brand_name")
    domain = manifest.get("domain")
    if not isinstance(brand_name, str) or not brand_name.strip():
        errors.append("manifest.json needs a non-empty brand_name")
    if not isinstance(domain, str) or not re.fullmatch(r"https://[^\s/]+/?", domain.strip()):
        errors.append("manifest.json domain must be a canonical https origin")

    forbidden_terms = manifest.get("forbidden_terms", [])
    if not isinstance(forbidden_terms, list) or not all(
        isinstance(term, str) and term.strip() for term in forbidden_terms
    ):
        errors.append("manifest.json forbidden_terms must be an array of non-empty strings")
        forbidden_terms = []

    listed_files = manifest.get("files")
    if not isinstance(listed_files, list):
        errors.append("manifest.json files must be an array")
        listed_paths: set[str] = set()
    else:
        listed_paths = {
            entry.get("path")
            for entry in listed_files
            if isinstance(entry, dict) and isinstance(entry.get("path"), str)
        }
        for relative in REQUIRED_FILES:
            if relative != "manifest.json" and relative not in listed_paths:
                errors.append(f"manifest.json does not list: {relative}")
        for relative in listed_paths:
            if relative.startswith("/") or ".." in Path(relative).parts:
                errors.append(f"Manifest path must be package-relative: {relative}")
            elif not (root / relative).is_file():
                errors.append(f"Manifest points to a missing file: {relative}")

    palette_path = root / "brand/palette.json"
    palette = read_json(palette_path, errors) if palette_path.is_file() else {}
    missing_palette = sorted(PALETTE_KEYS - set(palette))
    if missing_palette:
        errors.append("palette.json is missing keys: " + ", ".join(missing_palette))

    for svg_relative in (
        "brand/logo-primary.svg",
        "brand/logo-mark.svg",
        "brand/logo-mono-dark.svg",
        "brand/logo-mono-light.svg",
        "brand/favicon.svg",
        "images/feature-01.svg",
        "images/feature-02.svg",
        "images/feature-03.svg",
        "images/feature-04.svg",
    ):
        svg_path = root / svg_relative
        if svg_path.is_file() and "<svg" not in svg_path.read_text(encoding="utf-8", errors="ignore"):
            errors.append(f"File does not contain an SVG root: {svg_relative}")

    excluded_scan_files = {root / "qa-report.md"}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES or path in excluded_scan_files:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in LEAK_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"Found {label} in {path.relative_to(root)}")
        for term in forbidden_terms:
            if term.casefold() in text.casefold():
                errors.append(f"Found forbidden reference term {term!r} in {path.relative_to(root)}")

    forbidden_paths = [
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file()
        and re.search(r"(?:privacy|refund|terms|cookies?)[-_ ]?(?:policy|conditions)?\.(?:md|txt|html|pdf)$", path.name, re.IGNORECASE)
    ]
    if forbidden_paths:
        errors.append("Legal-policy files are out of scope: " + ", ".join(sorted(forbidden_paths)))

    if isinstance(domain, str):
        canonical = domain.rstrip("/")
        seo_path = root / "content/seo-metadata.csv"
        if seo_path.is_file() and canonical not in seo_path.read_text(encoding="utf-8", errors="replace"):
            errors.append("seo-metadata.csv does not contain the canonical domain")

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"Validation passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
