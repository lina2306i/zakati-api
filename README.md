# 🌙 Zakati API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![GitHub Pages](https://img.shields.io/badge/CDN-GitHub%20Pages-0f6b4c.svg)](https://lina2306i.github.io/zakati-api/)
[![Countries](https://img.shields.io/badge/countries-8-blue.svg)](./data/1448/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/lina2306i/zakati-api)

> **واجهة برمجية مفتوحة المصدر لبيانات الزكاة الرسمية** — نصاب زكاة المال، زكاة الفطر، والزروع والأنعام — حسب الدولة والسنة الهجرية، من دور الإفتاء والمجالس الشرعية.  
> **Open-source static API for official Zakat data** — Nisab, Zakat al-Fitr, crops & livestock — by country and Hijri year, sourced from Fatwa councils.

**Live homepage:** https://lina2306i.github.io/zakati-api/  
**Catalog JSON:** https://lina2306i.github.io/zakati-api/data/index.json

---

## ✨ Why Zakati API?

Islamic app developers used to hardcode yearly Nisab / Fitr values, scrape news sites, or ship stale numbers.  
**Zakati API** replaces that with a versioned, community-maintained JSON CDN:

| Pain | Solution |
|------|----------|
| Manual yearly updates in every app | One shared `data/<year>/<country>.json` |
| Inconsistent field names across countries | Unified schema (`nisab_cash`, `nisab_value`, …) |
| No verification trail | Mandatory `official_source_url` + `last_updated` |
| Costly backends | 100% static GitHub Pages CDN |

---

## 🚀 Getting Started / البدء السريع

### 1. Consume the API (no install)

```text
https://lina2306i.github.io/zakati-api/data/<HIJRI_YEAR>/<COUNTRY_CODE>.json
```

**Example — Tunisia 1448 AH:**

```text
https://lina2306i.github.io/zakati-api/data/1448/tn.json
```

### 2. Fetch in JavaScript

```javascript
const res = await fetch(
  "https://lina2306i.github.io/zakati-api/data/1448/tn.json"
);
const zakat = await res.json();

const nisab = zakat.zakat_categories.zakat_al_mal.nisab_cash; // 34369.356
const fitr = zakat.zakat_al_fitr.value_per_person;            // 2
const camelNisab = zakat.zakat_categories.livestock
  .sub_categories[0].nisab_value;                             // 5 (number → math-ready)
```

### 3. Discover all countries

```javascript
const catalog = await fetch(
  "https://lina2306i.github.io/zakati-api/data/index.json"
).then((r) => r.json());

console.log(catalog.countries_by_year["1448"]);
```

### 4. Contribute a country (5 minutes)

```bash
git clone https://github.com/lina2306i/zakati-api.git
cd zakati-api
cp templates/country.template.json data/1448/xx.json
# fill official values → validate → PR
python scripts/validate_data.py
```

Full guide: [`CONTRIBUTING.md`](./CONTRIBUTING.md)

---

## ⚙️ How it works? / كيف يعمل؟

```text
┌──────────────────┐     static JSON      ┌─────────────────────────┐
│ Fatwa councils   │ ───────────────────► │ data/<year>/<cc>.json   │
│ + contributors   │                      └───────────┬─────────────┘
└──────────────────┘                                  │
                                                      ▼
                                          GitHub Pages (global CDN)
                                                      │
                      ┌───────────────────────────────┼────────────────┐
                      ▼                               ▼                ▼
                 Mobile apps                      Web apps        Calculators
```

1. Maintainers / contributors add or update a country file under `data/<hijri_year>/`.
2. CI (`json-validator.yml`) checks syntax + DX rules (`nisab_cash`, numeric `nisab_value`, …).
3. GitHub Pages serves files instantly — no backend, no API key.
4. Apps read `data/index.json` to list years/countries dynamically.

### Auto new Hijri year

When a new Hijri year starts, maintainers can scaffold all country files automatically:

```bash
python scripts/scaffold_year.py --year 1449 --gregorian 2027
```

Or run **Actions → Scaffold New Hijri Year** (opens a PR with `status: needs_update` and cleared yearly cash fields ready for official re-verification).

---

## 📦 Available countries (1448 AH / 2026 CE)

| Code | Country | Currency | Status | Endpoint |
|------|---------|----------|--------|----------|
| `tn` | Tunisia / تونس | TND | complete | [`tn.json`](https://lina2306i.github.io/zakati-api/data/1448/tn.json) |
| `eg` | Egypt / مصر | EGP | partial | [`eg.json`](https://lina2306i.github.io/zakati-api/data/1448/eg.json) |
| `sa` | Saudi Arabia / السعودية | SAR | partial | [`sa.json`](https://lina2306i.github.io/zakati-api/data/1448/sa.json) |
| `dz` | Algeria / الجزائر | DZD | partial | [`dz.json`](https://lina2306i.github.io/zakati-api/data/1448/dz.json) |
| `my` | Malaysia / ماليزيا | MYR | partial | [`my.json`](https://lina2306i.github.io/zakati-api/data/1448/my.json) |
| `ma` | Morocco / المغرب | MAD | partial | [`ma.json`](https://lina2306i.github.io/zakati-api/data/1448/ma.json) |
| `id` | Indonesia / إندونيسيا | IDR | partial | [`id.json`](https://lina2306i.github.io/zakati-api/data/1448/id.json) |
| `ae` | UAE / الإمارات | AED | partial | [`ae.json`](https://lina2306i.github.io/zakati-api/data/1448/ae.json) |

> `partial` = Fitr (and sometimes Nisab) filled from official sources; remaining cash Nisab may be `null` until councils publish yearly figures.

---

## 🛠️ Unified JSON Schema / الهيكل الموحد

**DX rules (important for mobile parsing):**

1. **`nisab_cash`** — currency-agnostic; read together with top-level `currency`.
2. **`nisab_value`** — numeric Nisab for livestock / agriculture (math-ready).
3. **`last_updated`** — ISO date `YYYY-MM-DD` for cache invalidation.

<details>
<summary><strong>▶ Expand full schema example (Tunisia-shaped)</strong></summary>

```json
{
  "hijri_year": 1448,
  "gregorian_year": 2026,
  "last_updated": "2026-10-16",
  "status": "complete",
  "country_code": "TN",
  "country_name_ar": "تونس",
  "country_name_en": "Tunisia",
  "currency": "TND",
  "official_source_url": "https://…",
  "zakat_al_fitr": {
    "value_per_person": 2.0,
    "notes_ar": "…",
    "notes_en": "…"
  },
  "zakat_categories": {
    "zakat_al_mal": {
      "nisab_cash": 34369.356,
      "nisab_gold_grams": 85,
      "nisab_silver_grams": 595,
      "percentage_rate": 2.5
    },
    "agriculture": {
      "nisab_value": 5,
      "nisab_unit": "awsuq",
      "nisab_kg_approx": 750,
      "rates": [
        { "type_en": "Rain-fed", "rate_percentage": 10.0 },
        { "type_en": "Artificially irrigated", "rate_percentage": 5.0 }
      ]
    },
    "livestock": {
      "sub_categories": [
        {
          "type_en": "Camels",
          "nisab_value": 5,
          "nisab_unit": "heads",
          "nisab_ar": "5 إبل",
          "nisab_en": "5 camels"
        }
      ]
    },
    "treasures_and_minerals": { }
  },
  "asnaf_al_zakat": {
    "ar": ["الفقراء", "المساكين", "العاملون عليها", "المؤلفة قلوبهم", "في الرقاب", "الغارمون", "في سبيل الله", "ابن السبيل"],
    "en": ["Al-Fuqara", "Al-Masakin", "Al-Amilina Alayha", "Al-Mu'allafati Qulubuhum", "Fi al-Riqab", "Al-Gharimin", "Fi Sabilillah", "Ibn al-Sabil"]
  }
}
```

</details>

Machine-readable schema: [`schema/country.schema.json`](./schema/country.schema.json)

---

## 🤝 Contributing / المساهمة

We welcome developers from every Muslim country.

1. **Fork** this repository.
2. Add `data/<HIJRI_YEAR>/<iso>.json` (or update an existing one).
3. **Mandatory:** set `official_source_url` to the Fatwa / ministry announcement and paste it in the PR.
4. Run `python scripts/validate_data.py`.
5. Submit a **Pull Request**.

See the full checklist in [`CONTRIBUTING.md`](./CONTRIBUTING.md).

### Looking for help filling data

Open an Issue titled `data: <COUNTRY> <YEAR>` if you found an official source but need review — or claim a `partial` country and upgrade it to `complete`.

---

## 👥 Contributors / المساهمون

Thanks to everyone who verifies Fatwa sources and improves the schema.

<a href="https://github.com/lina2306i/zakati-api/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=lina2306i/zakati-api" alt="Contributors" />
</a>

| Role | Person |
|------|--------|
| Creator & Maintainer | [@lina2306i](https://github.com/lina2306i) |

Want your name here? Ship a verified country PR 💚

---

## 📚 Sources & Documentation / المصادر والتوثيق

| Resource | Link |
|----------|------|
| API homepage | https://lina2306i.github.io/zakati-api/ |
| Dataset catalog | [`data/index.json`](./data/index.json) |
| JSON Schema | [`schema/country.schema.json`](./schema/country.schema.json) |
| Country template | [`templates/country.template.json`](./templates/country.template.json) |
| Contribution guide | [`CONTRIBUTING.md`](./CONTRIBUTING.md) |
| Year scaffold script | [`scripts/scaffold_year.py`](./scripts/scaffold_year.py) |
| Validator | [`scripts/validate_data.py`](./scripts/validate_data.py) |

Country files always include their own `official_source_url` (Diwan of Ifta, Dar al-Ifta, Habous, BAZNAS, UAE Fatwa Council, etc.).

---

## 💬 Community & Contact / المجتمع والتواصل

- **Issues:** bug reports, missing countries, schema proposals → [GitHub Issues](https://github.com/lina2306i/zakati-api/issues)
- **Pull Requests:** data + docs + tooling welcome
- **Maintainer:** [@lina2306i](https://github.com/lina2306i)
- **Share:** LinkedIn / X / Muslim developer communities — help others discover the CDN

If you build an app on Zakati API, open an Issue with your project link — we love featuring real consumers.

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=lina2306i/zakati-api&type=Date)](https://star-history.com/#lina2306i/zakati-api&Date)

If this project saves you time, **star the repo** so other Islamic-tech developers can find it.

---

## 📁 Project structure

```text
zakati-api/
├── index.html                 # GitHub Pages homepage
├── assets/style.css
├── data/
│   ├── index.json             # machine-readable catalog
│   └── 1448/
│       ├── tn.json … ae.json
├── schema/country.schema.json
├── templates/country.template.json
├── scripts/
│   ├── generate_data.py
│   ├── scaffold_year.py
│   ├── validate_data.py
│   └── lib_zakat.py
├── .github/workflows/
│   ├── json-validator.yml
│   └── scaffold-year.yml
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## 📄 License / الترخيص

MIT License — free for personal and commercial Islamic applications worldwide.  
رخصة MIT — متاحة للاستخدام الشخصي والتجاري لكافة التطبيقات الإسلامية.

See [`LICENSE`](./LICENSE).

---

<p align="center">
  <sub>Built with care for the Ummah · صُنع لخدمة الأمة</sub><br/>
  <a href="https://github.com/lina2306i/zakati-api">github.com/lina2306i/zakati-api</a>
</p>
