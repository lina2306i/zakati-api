# Contributing to Zakati API / المساهمة

Thank you for helping keep official Zakat data accurate and accessible.  
شكراً لمساهمتك في إبقاء بيانات الزكاة الرسمية دقيقة ومتاحة.

## Quick start

1. Fork → clone the repository.
2. Copy the template:

```bash
cp templates/country.template.json data/1448/xx.json
```

3. Fill fields using an **official Fatwa / ministry announcement**.
4. Set `official_source_url` and `last_updated` (`YYYY-MM-DD`).
5. Use unified field names:
   - `nisab_cash` (not `nisab_cash_tnd` / `nisab_cash_egp`)
   - numeric `nisab_value` for livestock & agriculture
6. Validate locally:

```bash
python scripts/validate_data.py
```

7. Open a Pull Request and paste the official source link in the description.

## Checklist

- [ ] Path is `data/<HIJRI_YEAR>/<iso2>.json` (lowercase filename)
- [ ] `country_code` is uppercase ISO-2 matching the filename
- [ ] `currency` is ISO-4217 (e.g. `TND`, `EGP`)
- [ ] Bilingual notes (`_ar` / `_en`) are present
- [ ] Official source URL is public and verifiable
- [ ] `python scripts/validate_data.py` passes

## Scaffolding a new Hijri year (maintainers)

### Locally

```bash
python scripts/scaffold_year.py --year 1449 --gregorian 2027
```

### Via GitHub Actions

**Actions → Scaffold New Hijri Year → Run workflow**

This copies last year’s files, clears yearly cash fields, marks `status: needs_update`, and opens a PR.

## Regenerating the current year from the generator

```bash
python scripts/generate_data.py
python scripts/validate_data.py
```

## Code of accuracy

Never invent Fatwa values. If an official cash figure is unpublished, set the field to `null` and document food equivalents / notes clearly.
