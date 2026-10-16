#!/usr/bin/env python3
"""Validate country JSON syntax + required DX schema fields."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

REQUIRED_TOP = [
    "hijri_year",
    "gregorian_year",
    "last_updated",
    "country_code",
    "country_name_ar",
    "country_name_en",
    "currency",
    "official_source_url",
    "zakat_al_fitr",
    "zakat_categories",
    "asnaf_al_zakat",
]

REQUIRED_CATEGORIES = [
    "zakat_al_mal",
    "agriculture",
    "livestock",
    "treasures_and_minerals",
]


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid JSON ({exc})"]

    for key in REQUIRED_TOP:
        if key not in doc:
            errors.append(f"{path}: missing top-level field '{key}'")

    cats = doc.get("zakat_categories") or {}
    for key in REQUIRED_CATEGORIES:
        if key not in cats:
            errors.append(f"{path}: missing zakat_categories.{key}")

    mal = cats.get("zakat_al_mal") or {}
    if "nisab_cash" not in mal:
        errors.append(f"{path}: zakat_al_mal.nisab_cash is required (use null if unknown)")
    # Reject legacy currency-suffixed field names
    for legacy in list(mal.keys()):
        if legacy.startswith("nisab_cash_") and legacy != "nisab_cash":
            errors.append(
                f"{path}: legacy field '{legacy}' found — use unified 'nisab_cash' instead"
            )

    agri = cats.get("agriculture") or {}
    if "nisab_value" not in agri:
        errors.append(f"{path}: agriculture.nisab_value (numeric) is required")

    for animal in cats.get("livestock", {}).get("sub_categories", []):
        if "nisab_value" not in animal:
            errors.append(
                f"{path}: livestock sub_category missing nisab_value ({animal.get('type_en')})"
            )

    expected_code = path.stem.lower()
    actual = str(doc.get("country_code", "")).lower()
    if actual and actual != expected_code:
        errors.append(f"{path}: country_code '{actual}' != filename '{expected_code}'")

    return errors


def main() -> int:
    files = sorted(DATA.glob("*/*.json"))
    if not files:
        fail("No data/<year>/*.json files found")
        return 1

    all_errors: list[str] = []
    for path in files:
        all_errors.extend(validate_file(path))
        print(f"checked {path.relative_to(ROOT)}")

    # catalog optional but recommended
    catalog = DATA / "index.json"
    if catalog.exists():
        try:
            json.loads(catalog.read_text(encoding="utf-8"))
            print("checked data/index.json")
        except json.JSONDecodeError as exc:
            all_errors.append(f"data/index.json: invalid JSON ({exc})")

    if all_errors:
        for err in all_errors:
            fail(err)
        print(f"\nFailed with {len(all_errors)} error(s).", file=sys.stderr)
        return 1

    print(f"\nSuccess: validated {len(files)} country file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
