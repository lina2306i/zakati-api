#!/usr/bin/env python3
"""Generate / refresh country JSON datasets and the public catalog."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib_zakat import agriculture, country_doc  # noqa: E402

HIJRI_YEAR = 1448
GREGORIAN_YEAR = 2026
LAST_UPDATED = "2026-10-16"
OUT_DIR = ROOT / "data" / str(HIJRI_YEAR)
CATALOG_PATH = ROOT / "data" / "index.json"


def countries() -> list[dict]:
    return [
        country_doc(
            hijri_year=HIJRI_YEAR,
            gregorian_year=GREGORIAN_YEAR,
            country_code="TN",
            country_name_ar="تونس",
            country_name_en="Tunisia",
            currency="TND",
            official_source_url="https://www.tunisiatv.tn/ar/article/6a34072c35f27da20948b973/%D9%86%D8%B5%D8%A7%D8%A8-%D8%B2%D9%83%D8%A7%D8%A9-%D8%A7%D9%84%D9%85%D8%A7%D9%84-%D9%84%D9%84%D8%B9%D8%A7%D9%85-%D8%A7%D9%84%D9%87%D8%AC%D8%B1%D9%8A-1448-34369356-%D8%AF%D9%8A%D9%86%D8%A7%D8%B1%D8%A7",
            last_updated=LAST_UPDATED,
            status="complete",
            zakat_al_fitr={
                "value_per_person": 2.0,
                "notes_ar": "ديناران تشتمل على الصاع النبوي ويجوز إخراجها نقداً، وتستحب قبل صلاة العيد ويجوز تقديمها بيومين أو ثلاثة وفق المذهب المالكي. يصدر ديوان الإفتاء بيان زكاة الفطر عادة في منتصف شهر رمضان من كل عام هجري.",
                "notes_en": "2 TND per person. Equivalent to one Sa'a of staple food, allowed in cash according to the Maliki school, best paid before Eid prayer. The Diwan of Ifta typically announces the cash value mid-Ramadan each Hijri year.",
            },
            nisab_cash=34369.356,
            mal_conditions_ar=[
                "بلوغ النصاب المعتمد",
                "دوران الحول القمري الكامل",
                "الملكية التامة والخلو من الدين",
                "تم احتساب هذا المبلغ بناءً على القيمة النقدية لـ 85 غراماً من الذهب الخالص (عيار 24) وفقاً لأسعار السوق المتداولة محلياً",
            ],
            mal_conditions_en=[
                "Reaching the approved Nisab",
                "Possession for one full lunar year",
                "Full ownership and debt-free status",
                "This amount is calculated from the cash value of 85 grams of pure gold (24K) according to locally traded market prices",
            ],
        ),
        country_doc(
            hijri_year=HIJRI_YEAR,
            gregorian_year=GREGORIAN_YEAR,
            country_code="EG",
            country_name_ar="مصر",
            country_name_en="Egypt",
            currency="EGP",
            official_source_url="https://www.dar-alifta.org/ar/articles/details/11042/%D8%AF%D8%A7%D8%B1-%D8%A7%D9%84%D8%A7%D9%81%D8%AA%D8%A7%D8%A1-%D8%A7%D9%84%D9%85%D8%B5%D8%B1%D9%8A%D8%A9-%D8%AA%D8%AD%D8%AF%D8%AF-%D9%82%D9%8A%D9%85%D8%A9-%D8%B2%D9%83%D8%A7%D8%A9-%D8%A7%D9%84%D9%81%D8%B7%D8%B1-%D9%84%D9%87%D8%B0%D8%A7-%D8%A7%D9%84%D8%B9%D8%A7%D9%85-1447%D9%87%D9%80-2026%D9%85",
            last_updated=LAST_UPDATED,
            status="partial",
            zakat_al_fitr={
                "value_per_person": 35.0,
                "notes_ar": "حد أدنى 35 جنيهاً مصرياً عن كل فرد وفق دار الإفتاء المصرية بالتنسيق مع مجمع البحوث الإسلامية. يعادل نحو 2.04 كغ من القمح، ويجوز إخراجها نقداً من أول رمضان حتى قبل صلاة العيد.",
                "notes_en": "Minimum 35 EGP per person per Dar al-Ifta Egypt. Equivalent to about 2.04 kg of wheat; cash payment allowed from the start of Ramadan until before Eid prayer.",
            },
            nisab_cash=None,
            agriculture_block=agriculture(
                category_ar="الزروع والثمار",
                category_en="Crops and Fruits",
                nisab_kg_approx=653.0,
            ),
        ),
        country_doc(
            hijri_year=HIJRI_YEAR,
            gregorian_year=GREGORIAN_YEAR,
            country_code="SA",
            country_name_ar="المملكة العربية السعودية",
            country_name_en="Saudi Arabia",
            currency="SAR",
            official_source_url="https://www.spa.gov.sa/N2538111",
            last_updated=LAST_UPDATED,
            status="partial",
            zakat_al_fitr={
                "value_per_person": None,
                "value_food_ar": "صاع من غالب قوت البلد (نحو 3 كغ من الأرز أو التمر أو الطحين)",
                "value_food_en": "One Sa'a of the common staple food (~3 kg of rice, dates, or flour)",
                "cash_proxy_sar_range": {
                    "min": 18,
                    "max": 30,
                    "notes_ar": "قيمة تقريبية تستخدمها بعض الجمعيات لشراء الصاع؛ المفتي العام يؤكد وجوب إخراجها طعاماً لا نقداً.",
                    "notes_en": "Approximate proxy used by some charities to purchase one Sa'a; the Grand Mufti affirms it must be given as food, not cash.",
                },
                "notes_ar": "واجبة صاعاً من قوت البلد. وقتها من غروب شمس آخر يوم رمضان إلى صلاة العيد، ويجوز تقديمها بيوم أو يومين. لا يجوز إخراج القيمة نقداً عند المفتي العام.",
                "notes_en": "Obligatory as one Sa'a of staple food. Due from sunset of the last day of Ramadan until Eid prayer; may be advanced by one or two days. Cash instead of food is not permitted according to the Grand Mufti.",
            },
            nisab_cash=None,
            mal_extra={
                "regulatory_authority_ar": "هيئة الزكاة والضريبة والجمارك (ZATCA) لجباية زكاة المنشآت",
                "regulatory_authority_en": "ZATCA for corporate Zakat collection",
            },
        ),
        country_doc(
            hijri_year=HIJRI_YEAR,
            gregorian_year=GREGORIAN_YEAR,
            country_code="DZ",
            country_name_ar="الجزائر",
            country_name_en="Algeria",
            currency="DZD",
            official_source_url="http://marw.gov.dz/%D8%A5%D8%B9%D9%84%D8%A7%D9%85%20%D9%88%D8%A8%D9%8A%D8%A7%D9%86",
            last_updated=LAST_UPDATED,
            status="partial",
            zakat_al_fitr={
                "value_per_person": 170.0,
                "notes_ar": "170 ديناراً جزائرياً عن كل فرد وفق بلاغ وزارة الشؤون الدينية والأوقاف لسنة 1447هـ/2026م، يعادل متوسط قيمة صاع من غالب قوت البلد (نحو 2 كغ).",
                "notes_en": "170 DZD per person per the Ministry of Religious Affairs announcement for 1447 AH / 2026 CE (~2 kg staple food equivalent).",
            },
            nisab_cash=None,
        ),
        country_doc(
            hijri_year=HIJRI_YEAR,
            gregorian_year=GREGORIAN_YEAR,
            country_code="MY",
            country_name_ar="ماليزيا",
            country_name_en="Malaysia",
            currency="MYR",
            official_source_url="https://baitulmal.jawhar.gov.my/statistik-kadar-nisab-zakat-fitrah/",
            last_updated=LAST_UPDATED,
            status="partial",
            zakat_al_fitr={
                "value_per_person": 8.0,
                "value_tiers": [
                    {
                        "tier_ar": "أرز محلي / مستورد عادي (الأقاليم الاتحادية)",
                        "tier_en": "Local / regular imported rice (Federal Territories)",
                        "rate": 8.0,
                    },
                    {
                        "tier_ar": "أرز مستورد ممتاز",
                        "tier_en": "Premium imported rice",
                        "rate": 15.0,
                    },
                    {
                        "tier_ar": "أرز بسمتي أو ما يعادله",
                        "tier_en": "Basmati or equivalent",
                        "rate": 25.0,
                    },
                ],
                "notes_ar": "المعدلات وفق MAIWP للأقاليم الاتحادية لسنة 1447هـ/2026م. تختلف المعدلات حسب الولاية؛ راجع جداول JAWHAR الرسمية.",
                "notes_en": "Rates follow MAIWP (Federal Territories) for 1447 AH / 2026 CE. Rates vary by Malaysian state; check official JAWHAR tables.",
            },
            nisab_cash=None,
        ),
        # --- New countries ---
        country_doc(
            hijri_year=HIJRI_YEAR,
            gregorian_year=GREGORIAN_YEAR,
            country_code="MA",
            country_name_ar="المغرب",
            country_name_en="Morocco",
            currency="MAD",
            official_source_url="https://www.habous.gov.ma/%D8%A7%D9%84%D9%85%D8%AC%D9%84%D8%B3-%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A-%D8%A7%D9%84%D8%A7%D8%B9%D9%84%D9%89/22172-%20-%D8%B1%D8%A3%D9%8A-%D8%A7%D9%84%D9%85%D8%AC%D9%84%D8%B3-%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A-%D8%A7%D9%84%D8%A3%D8%B9%D9%84%D9%89-%D9%81%D9%8A-%D8%B4%D8%A3%D9%86-%D8%B2%D9%83%D8%A7%D8%A9-%D8%A7%D9%84%D9%81%D8%B7%D8%B1-%D9%88%D9%85%D9%82%D8%AF%D8%A7%D8%B1%D9%87%D8%A7-%D9%83%D9%8A%D9%84%D8%A7%D9%8B-%D9%88%D9%86%D9%82%D8%AF%D8%A7%D9%8B-%D9%84%D8%B9%D8%A7%D9%85-1447%D9%87%D9%80-2026%D9%85.html",
            last_updated=LAST_UPDATED,
            status="partial",
            zakat_al_fitr={
                "value_per_person": 25.0,
                "notes_ar": "25 درهماً مغربياً عن كل نفس وفق رأي المجلس العلمي الأعلى لسنة 1447هـ/2026م. الأصل صاع نبوي (~2.5 كغ من الحبوب أو الدقيق)، ويجوز إخراجها نقداً قبل العيد بيومين إلى ثلاثة.",
                "notes_en": "25 MAD per person per the Higher Scientific Council for 1447 AH / 2026 CE. Food equivalent ~2.5 kg of grains/flour; cash allowed; may be paid 2–3 days before Eid.",
            },
            nisab_cash=None,
        ),
        country_doc(
            hijri_year=HIJRI_YEAR,
            gregorian_year=GREGORIAN_YEAR,
            country_code="ID",
            country_name_ar="إندونيسيا",
            country_name_en="Indonesia",
            currency="IDR",
            official_source_url="https://baznas.go.id/news-show/Ramadan_2026__BAZNAS_RI_Tetapkan_Zakat_Fitrah_Rp50_Ribu/3708",
            last_updated=LAST_UPDATED,
            status="partial",
            zakat_al_fitr={
                "value_per_person": 50000.0,
                "notes_ar": "50,000 روبية إندونيسية للفرد وفق قرار رئيس BAZNAS رقم 14 لسنة 2026 (1447هـ)، تعادل 2.5 كغ أو 3.5 لتر من الأرز الممتاز. قد تختلف المعدلات محلياً حسب قرارات مجالس العلماء الإقليمية.",
                "notes_en": "IDR 50,000 per person per BAZNAS RI Decree No. 14/2026 (1447 AH), equivalent to 2.5 kg / 3.5 L of premium rice. Local MUI/BAZNAS rates may differ by region.",
            },
            nisab_cash=None,
        ),
        country_doc(
            hijri_year=HIJRI_YEAR,
            gregorian_year=GREGORIAN_YEAR,
            country_code="AE",
            country_name_ar="الإمارات العربية المتحدة",
            country_name_en="United Arab Emirates",
            currency="AED",
            official_source_url="https://www.khaleejtimes.com/uae/zakat-al-fitr-cash-allowed-dh25-recommended",
            last_updated=LAST_UPDATED,
            status="partial",
            zakat_al_fitr={
                "value_per_person": 25.0,
                "notes_ar": "25 درهماً إماراتياً للفرد وفق مجلس الإمارات للإفتاء لسنة 1447هـ/2026م، أو 2.5 كغ من الأرز. يجوز إخراجها نقداً عبر الجهات الخيرية المعتمدة.",
                "notes_en": "AED 25 per person per the UAE Council for Fatwa (1447 AH / 2026 CE), or 2.5 kg of rice. Cash payment through approved charities is allowed.",
            },
            nisab_cash=None,
        ),
    ]


def write_json(path: Path, payload: dict | list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def build_catalog(docs: list[dict]) -> dict:
    by_year: dict[str, list[dict]] = {}
    for doc in docs:
        year = str(doc["hijri_year"])
        code = doc["country_code"].lower()
        entry = {
            "code": code,
            "country_code": doc["country_code"],
            "name_ar": doc["country_name_ar"],
            "name_en": doc["country_name_en"],
            "currency": doc["currency"],
            "status": doc.get("status", "partial"),
            "last_updated": doc.get("last_updated"),
            "path": f"data/{year}/{code}.json",
            "url": f"https://lina2306i.github.io/zakati-api/data/{year}/{code}.json",
        }
        by_year.setdefault(year, []).append(entry)

    for year in by_year:
        by_year[year].sort(key=lambda x: x["code"])

    return {
        "api_base": "https://lina2306i.github.io/zakati-api",
        "url_pattern": "https://lina2306i.github.io/zakati-api/data/{hijri_year}/{country_code}.json",
        "schema": "https://lina2306i.github.io/zakati-api/schema/country.schema.json",
        "last_generated": LAST_UPDATED,
        "hijri_years": sorted(by_year.keys()),
        "countries_by_year": by_year,
        "total_files": sum(len(v) for v in by_year.values()),
    }


def main() -> None:
    docs = countries()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for doc in docs:
        code = doc["country_code"].lower()
        write_json(OUT_DIR / f"{code}.json", doc)
        print(f"wrote data/{HIJRI_YEAR}/{code}.json")

    catalog = build_catalog(docs)
    write_json(CATALOG_PATH, catalog)
    print(f"wrote data/index.json ({catalog['total_files']} countries)")


if __name__ == "__main__":
    main()
