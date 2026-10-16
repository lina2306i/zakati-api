#!/usr/bin/env python3
"""
Scaffold a new Hijri year folder from the previous year's country files.

Usage:
  python scripts/scaffold_year.py --year 1449 --gregorian 2027
  python scripts/scaffold_year.py --year 1449 --gregorian 2027 --from 1448

What it does:
  1. Copies every *.json from data/<from_year>/ into data/<new_year>/
  2. Bumps hijri_year / gregorian_year
  3. Sets status to "needs_update"
  4. Clears yearly cash fields that must be re-verified (nisab_cash, fitr value)
  5. Updates last_updated to today
  6. Rebuilds data/index.json
"""

from __future__ import annotations

import argparse
import json
import sys
from copy import deepcopy
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict | list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def reset_yearly_values(doc: dict, hijri: int, gregorian: int, today: str) -> dict:
    out = deepcopy(doc)
    out["hijri_year"] = hijri
    out["gregorian_year"] = gregorian
    out["last_updated"] = today
    out["status"] = "needs_update"

    fitr = out.get("zakat_al_fitr") or {}
    # Keep food notes, clear cash amount so maintainers must re-verify officially.
    if "value_per_person" in fitr:
        fitr["value_per_person"] = None
    fitr["notes_ar"] = (
        fitr.get("notes_ar", "")
        + " | يحتاج تحديثاً رسمياً للسنة الهجرية الجديدة."
    ).strip(" |")
    fitr["notes_en"] = (
        fitr.get("notes_en", "")
        + " | Needs official update for the new Hijri year."
    ).strip(" |")
    out["zakat_al_fitr"] = fitr

    mal = out.get("zakat_categories", {}).get("zakat_al_mal", {})
    if "nisab_cash" in mal:
        mal["nisab_cash"] = None
    return out


def rebuild_catalog() -> None:
    by_year: dict[str, list[dict]] = {}
    for year_dir in sorted(p for p in DATA.iterdir() if p.is_dir() and p.name.isdigit()):
        year = year_dir.name
        for path in sorted(year_dir.glob("*.json")):
            doc = load(path)
            code = path.stem.lower()
            by_year.setdefault(year, []).append(
                {
                    "code": code,
                    "country_code": doc.get("country_code", code.upper()),
                    "name_ar": doc.get("country_name_ar"),
                    "name_en": doc.get("country_name_en"),
                    "currency": doc.get("currency"),
                    "status": doc.get("status", "partial"),
                    "last_updated": doc.get("last_updated"),
                    "path": f"data/{year}/{code}.json",
                    "url": f"https://lina2306i.github.io/zakati-api/data/{year}/{code}.json",
                }
            )

    catalog = {
        "api_base": "https://lina2306i.github.io/zakati-api",
        "url_pattern": "https://lina2306i.github.io/zakati-api/data/{hijri_year}/{country_code}.json",
        "schema": "https://lina2306i.github.io/zakati-api/schema/country.schema.json",
        "last_generated": date.today().isoformat(),
        "hijri_years": sorted(by_year.keys()),
        "countries_by_year": by_year,
        "total_files": sum(len(v) for v in by_year.values()),
    }
    dump(DATA / "index.json", catalog)


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold a new Hijri year dataset folder")
    parser.add_argument("--year", type=int, required=True, help="New Hijri year, e.g. 1449")
    parser.add_argument(
        "--gregorian", type=int, required=True, help="Matching Gregorian year, e.g. 2027"
    )
    parser.add_argument(
        "--from",
        dest="from_year",
        type=int,
        default=None,
        help="Source Hijri year to copy from (default: latest existing)",
    )
    args = parser.parse_args()

    year_dirs = sorted(
        (int(p.name) for p in DATA.iterdir() if p.is_dir() and p.name.isdigit())
    )
    if not year_dirs:
        print("No existing data/<year> folders found.", file=sys.stderr)
        return 1

    from_year = args.from_year or year_dirs[-1]
    src = DATA / str(from_year)
    dst = DATA / str(args.year)

    if not src.exists():
        print(f"Source folder missing: {src}", file=sys.stderr)
        return 1
    if dst.exists() and any(dst.glob("*.json")):
        print(f"Target already has JSON files: {dst}", file=sys.stderr)
        return 1

    today = date.today().isoformat()
    dst.mkdir(parents=True, exist_ok=True)
    count = 0
    for path in sorted(src.glob("*.json")):
        doc = reset_yearly_values(load(path), args.year, args.gregorian, today)
        dump(dst / path.name, doc)
        count += 1
        print(f"scaffolded data/{args.year}/{path.name}")

    rebuild_catalog()
    print(f"Done: {count} files → data/{args.year}/ + data/index.json refreshed")
    print("Next: update official_source_url, nisab_cash, and zakat_al_fitr.value_per_person from Fatwa councils.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
