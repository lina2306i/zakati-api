# 🌙 Zakati API — Islamic Zakat Official Reference

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Open Source](https://img.shields.io/badge/Open%20Source-❤-red.svg)](https://github.com/lina2306i/zakati-api)
[![GitHub Pages](https://img.shields.io/badge/CDN-GitHub%20Pages-blue.svg)](https://lina2306i.github.io/zakati-api/)
[![CI: JSON Validator](https://img.shields.io/badge/CI-JSON%20Validator-success.svg)](./.github/workflows/json-validator.yml)

**Zakati API** هو أول واجهة برمجية مفتوحة المصدر تهدف إلى توفير البيانات الرسمية والشرعية لنصاب زكاة المال، زكاة الفطر، وأحكام الزكاة المعتمدة في مختلف الدول الإسلامية لكل سنة هجرية، بناءً على البيانات الصادرة عن دور الإفتاء والمجالس الشرعية الرسمية.

**Zakati API** is the first open-source static API dedicated to providing official, Sharia-compliant data for Zakat Nisab, Zakat al-Fitr, and Zakat regulations across Muslim countries for each Hijri year — sourced from official Fatwa councils.

> **Why this exists / لماذا وُجد هذا المشروع؟**  
> Islamic app developers historically had to scrape news, hardcode yearly values, or wait for manual updates. Zakati API solves that with a single, versioned, community-maintained JSON CDN.

---

## 🌐 كيف يعمل الـ API؟ / How to Use

The API is **100% serverless static JSON**, hosted free via **GitHub Pages** (global CDN).

### URL Pattern

```text
https://lina2306i.github.io/zakati-api/data/<HIJRI_YEAR>/<COUNTRY_CODE>.json
```

| Placeholder | Meaning | Example |
|---|---|---|
| `<HIJRI_YEAR>` | Hijri year folder | `1448` |
| `<COUNTRY_CODE>` | ISO 3166-1 alpha-2 (lowercase) | `tn`, `eg`, `sa`, `dz`, `my` |

### Example — Tunisia 1448 AH

```text
https://lina2306i.github.io/zakati-api/data/1448/tn.json
```

### Fetch example (JavaScript)

```javascript
const res = await fetch(
  "https://lina2306i.github.io/zakati-api/data/1448/tn.json"
);
const zakat = await res.json();

console.log(zakat.zakat_al_fitr.value_per_person); // 2
console.log(zakat.zakat_categories.zakat_al_mal.nisab_cash_tnd); // 34369.356
```

### Available countries (1448 AH / 2026 CE)

| Code | Country | File |
|------|---------|------|
| `tn` | Tunisia / تونس | [`data/1448/tn.json`](./data/1448/tn.json) |
| `eg` | Egypt / مصر | [`data/1448/eg.json`](./data/1448/eg.json) |
| `sa` | Saudi Arabia / السعودية | [`data/1448/sa.json`](./data/1448/sa.json) |
| `dz` | Algeria / الجزائر | [`data/1448/dz.json`](./data/1448/dz.json) |
| `my` | Malaysia / ماليزيا | [`data/1448/my.json`](./data/1448/my.json) |

---

## 🛠️ هيكل البيانات الموحد / Unified JSON Schema

All contributions **must** follow this schema so consuming apps stay compatible.

```json
{
  "hijri_year": 1448,
  "gregorian_year": 2026,
  "country_code": "TN",
  "country_name_ar": "تونس",
  "country_name_en": "Tunisia",
  "currency": "TND",
  "official_source_url": "https://official-fatwa-council-link.gov",
  "zakat_al_fitr": {
    "value_per_person": 2.0,
    "notes_ar": "...",
    "notes_en": "..."
  },
  "zakat_categories": {
    "zakat_al_mal": {
      "category_ar": "الأموال النقدية والذهب والفضة وعروض التجارة",
      "category_en": "Cash, Gold, Silver, and Commercial Goods",
      "nisab_cash_tnd": 34369.356,
      "nisab_gold_grams": 85,
      "nisab_silver_grams": 595,
      "percentage_rate": 2.5,
      "conditions_ar": ["..."],
      "conditions_en": ["..."]
    },
    "agriculture": {
      "category_ar": "الزروع والثمار",
      "category_en": "Crops and Fruits",
      "nisab_ar": "5 أوسق",
      "nisab_en": "5 Awsuq",
      "rates": [
        {
          "type_ar": "بعلي",
          "type_en": "Rain-fed",
          "rate_percentage": 10.0
        },
        {
          "type_ar": "سقوي",
          "type_en": "Artificially irrigated",
          "rate_percentage": 5.0
        }
      ],
      "conditions_ar": ["..."],
      "conditions_en": ["..."]
    },
    "livestock": {
      "category_ar": "الأنعام والمواشي",
      "category_en": "Livestock (An'am)",
      "sub_categories": [
        {
          "type_ar": "الإبل",
          "type_en": "Camels",
          "nisab_ar": "أقل النصاب 5 إبل",
          "nisab_en": "Minimum Nisab is 5 camels",
          "rate_ar": "...",
          "rate_en": "..."
        }
      ],
      "conditions_ar": ["..."],
      "conditions_en": ["..."]
    },
    "treasures_and_minerals": {
      "category_ar": "الركاز والمعادن",
      "category_en": "Rikaz and Minerals",
      "sub_categories": [
        {
          "type_ar": "الركاز",
          "type_en": "Rikaz",
          "nisab_ar": "لا يشترط له نصاب ولا حول",
          "nisab_en": "No Nisab or lunar year required",
          "rate_percentage": 20.0,
          "rate_ar": "الخمس (20%)",
          "rate_en": "One-fifth (20%)"
        }
      ]
    }
  },
  "asnaf_al_zakat": {
    "ar": [
      "الفقراء",
      "المساكين",
      "العاملون عليها",
      "المؤلفة قلوبهم",
      "في الرقاب",
      "الغارمون",
      "في سبيل الله",
      "ابن السبيل"
    ],
    "en": [
      "Al-Fuqara",
      "Al-Masakin",
      "Al-Amilina Alayha",
      "Al-Mu'allafati Qulubuhum",
      "Fi al-Riqab",
      "Al-Gharimin",
      "Fi Sabilillah",
      "Ibn al-Sabil"
    ]
  }
}
```

### Required top-level fields

| Field | Type | Description |
|-------|------|-------------|
| `hijri_year` | number | Hijri year of the dataset |
| `gregorian_year` | number | Corresponding Gregorian year |
| `country_code` | string | ISO alpha-2 uppercase (e.g. `TN`) |
| `country_name_ar` / `country_name_en` | string | Localized country name |
| `currency` | string | ISO 4217 currency code |
| `official_source_url` | string | **Mandatory** link to Fatwa council / official announcement |
| `zakat_al_fitr` | object | Per-person Fitr value + notes |
| `zakat_categories` | object | All Sharia Zakat types (`zakat_al_mal`, `agriculture`, `livestock`, `treasures_and_minerals`) |
| `asnaf_al_zakat` | object | The eight categories of recipients (Qur'an 9:60) |

> **Note:** Use `null` for cash Nisab / Fitr fields when the council has not published a yearly cash figure (e.g. Saudi Fitr is food-based). Document food equivalents in bilingual notes.

---

## 🚀 تفعيل GitHub Pages / Enable GitHub Pages

1. Push this repository to GitHub as `zakati-api` under your account.
2. Open **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
4. Select branch **`main`** and folder **`/` (root)**.
5. Save — your CDN becomes:

```text
https://lina2306i.github.io/zakati-api/data/1448/tn.json
```

---

## 🤝 كيف تساهم؟ / How to Contribute

نرحب بمساهمات المطورين من كافة أنحاء العالم الإسلامي.  
We welcome contributions from developers worldwide.

1. **Fork** this repository.
2. Create the Hijri year folder if missing, e.g. `data/1448/`.
3. Add your country file using the lowercase ISO code, e.g. `eg.json`, `ma.json`, `id.json`.
4. **Mandatory:** set `official_source_url` to the Fatwa council / ministry announcement, and paste the same link in the Pull Request description.
5. Ensure valid JSON (CI will reject broken syntax).
6. Open a **Pull Request** targeting `main`.

### Contribution checklist

- [ ] File path matches `data/<HIJRI_YEAR>/<iso>.json`
- [ ] Schema fields match the unified structure above
- [ ] Bilingual notes (`_ar` / `_en`) are filled
- [ ] Official source URL is public and verifiable
- [ ] JSON passes the GitHub Actions validator

---

## 📁 هيكل المشروع / Project Structure

```text
zakati-api/
├── .github/
│   └── workflows/
│       └── json-validator.yml
├── data/
│   └── 1448/
│       ├── tn.json
│       ├── eg.json
│       ├── sa.json
│       ├── dz.json
│       └── my.json
├── README.md
└── LICENSE
```

---

## 📄 الترخيص / License

This project is licensed under the **MIT License** — free for personal and commercial Islamic applications worldwide.

هذا المشروع مرخص بموجب رخصة **MIT** — متاح للاستخدام المجاني والتجاري لكافة التطبيقات الإسلامية.

See [`LICENSE`](./LICENSE) for the full text.

---

## 👤 Creator

| Role | GitHub |
|------|--------|
| Creator & Maintainer | [@lina2306i](https://github.com/lina2306i) |

## 🙌 Contributors

Contributions of country data, schema improvements, and documentation translations are credited here via GitHub's contributor graph after merge.

تم إنشاء هذا المشروع لخدمة مطوري التطبيقات الإسلامية والمجتمع — بارك الله فيمن ساهم.
