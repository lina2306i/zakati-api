"""Shared Zakat category builders for Zakati API country datasets."""

from __future__ import annotations

from copy import deepcopy
from typing import Any


ASNAF: dict[str, list[str]] = {
    "ar": [
        "الفقراء",
        "المساكين",
        "العاملون عليها",
        "المؤلفة قلوبهم",
        "في الرقاب",
        "الغارمون",
        "في سبيل الله",
        "ابن السبيل",
    ],
    "en": [
        "Al-Fuqara",
        "Al-Masakin",
        "Al-Amilina Alayha",
        "Al-Mu'allafati Qulubuhum",
        "Fi al-Riqab",
        "Al-Gharimin",
        "Fi Sabilillah",
        "Ibn al-Sabil",
    ],
}


def agriculture(
    category_ar: str = "الزروع والثمار (الحبوب والتمور والزيتون)",
    category_en: str = "Crops and Fruits (Grains, Dates, and Olives)",
    nisab_kg_approx: float = 750.0,
) -> dict[str, Any]:
    return {
        "category_ar": category_ar,
        "category_en": category_en,
        "nisab_value": 5,
        "nisab_unit": "awsuq",
        "nisab_kg_approx": nisab_kg_approx,
        "nisab_ar": f"5 أوسق (ما يعادل حوالي {int(nisab_kg_approx)} كغ تقريباً)",
        "nisab_en": f"5 Awsuq (equivalent to approx. {int(nisab_kg_approx)} kg)",
        "rates": [
            {
                "type_ar": "مسقي بماء المطر دون كلفة (بعلي)",
                "type_en": "Rain-fed / Naturally irrigated",
                "rate_percentage": 10.0,
            },
            {
                "type_ar": "مسقي بآلات وكلفة اصطناعية (سقوي)",
                "type_en": "Artificially irrigated with cost",
                "rate_percentage": 5.0,
            },
        ],
        "conditions_ar": [
            "بلوغ النصاب وقت الحصاد والاشتداد ولا يشترط فيها الحول"
        ],
        "conditions_en": [
            "Reaching Nisab at the time of harvest; the lunar-year condition does not apply"
        ],
    }


def livestock() -> dict[str, Any]:
    return {
        "category_ar": "الأنعام والمواشي",
        "category_en": "Livestock (An'am)",
        "sub_categories": [
            {
                "type_ar": "الإبل (الجمال)",
                "type_en": "Camels",
                "nisab_value": 5,
                "nisab_unit": "heads",
                "nisab_ar": "5 إبل",
                "nisab_en": "5 camels",
                "rate_ar": "في كل 5 إبل شاة، وتتغير الفريضة بعد ذلك حسب الجداول الشرعية التفصيلية",
                "rate_en": "1 sheep for every 5 camels; rules scale according to detailed Sharia tables",
            },
            {
                "type_ar": "البقر",
                "type_en": "Cows/Cattle",
                "nisab_value": 30,
                "nisab_unit": "heads",
                "nisab_ar": "30 بقرة",
                "nisab_en": "30 cows",
                "rate_ar": "في كل 30 بقرة تبيع أو تبيعة، وفي كل 40 مسنة",
                "rate_en": "For every 30 cows: 1 Tabi'; for every 40: 1 Musinnah",
            },
            {
                "type_ar": "الغنم والماعز",
                "type_en": "Sheep and Goats",
                "nisab_value": 40,
                "nisab_unit": "heads",
                "nisab_ar": "40 شاة",
                "nisab_en": "40 sheep/goats",
                "rate_ar": "من 40 إلى 120: شاة. من 121 إلى 200: شاتان. من 201 إلى 300: ثلاث. ثم شاة لكل 100",
                "rate_en": "40–120: 1 sheep. 121–200: 2. 201–300: 3. Then 1 sheep per additional 100",
            },
        ],
        "conditions_ar": [
            "أن تكون سائمة (ترعى الكلأ المباح معظم العام) وفق جمهور الفقهاء، مع دوران الحول"
        ],
        "conditions_en": [
            "Freely grazing (Saimah) for most of the year per the majority of scholars, plus one lunar year"
        ],
    }


def treasures_and_minerals() -> dict[str, Any]:
    return {
        "category_ar": "الركاز والمعادن (ما يستخرج من باطن الأرض)",
        "category_en": "Rikaz and Minerals (Buried Treasures)",
        "sub_categories": [
            {
                "type_ar": "الركاز (دفن الجاهلية)",
                "type_en": "Rikaz (Ancient buried treasure)",
                "nisab_value": None,
                "nisab_ar": "لا يشترط له نصاب ولا حول",
                "nisab_en": "No Nisab or lunar year required",
                "rate_percentage": 20.0,
                "rate_ar": "الخمس (20%) يخرج فور العثور عليه",
                "rate_en": "One-fifth (20%) paid immediately upon extraction",
            },
            {
                "type_ar": "المعادن والنفط والغاز",
                "type_en": "Minerals, Oil, and Gas",
                "nisab_value": 85,
                "nisab_unit": "gold_grams",
                "nisab_ar": "ما يعادل نصاب الذهب (85 غراماً)",
                "nisab_en": "Equivalent to Gold Nisab (85 grams)",
                "rate_percentage": 2.5,
                "rate_ar": "ربع العشر (2.5%) يخرج فور الاستخراج بعد خصم تكاليف الإنتاج",
                "rate_en": "2.5% paid after deducting production costs",
            },
        ],
    }


def zakat_al_mal(
    nisab_cash: float | None,
    conditions_ar: list[str] | None = None,
    conditions_en: list[str] | None = None,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    block: dict[str, Any] = {
        "category_ar": "الأموال النقدية والذهب والفضة وعروض التجارة",
        "category_en": "Cash, Gold, Silver, and Commercial Goods",
        "nisab_cash": nisab_cash,
        "nisab_gold_grams": 85,
        "nisab_silver_grams": 595,
        "percentage_rate": 2.5,
        "conditions_ar": conditions_ar
        or [
            "بلوغ النصاب المعتمد",
            "دوران الحول القمري الكامل",
            "الملكية التامة والخلو من الدين",
        ],
        "conditions_en": conditions_en
        or [
            "Reaching the approved Nisab",
            "Possession for one full lunar year",
            "Full ownership and debt-free status",
        ],
    }
    if extra:
        block.update(extra)
    return block


def country_doc(
    *,
    hijri_year: int,
    gregorian_year: int,
    country_code: str,
    country_name_ar: str,
    country_name_en: str,
    currency: str,
    official_source_url: str,
    last_updated: str,
    status: str,
    zakat_al_fitr: dict[str, Any],
    nisab_cash: float | None,
    mal_conditions_ar: list[str] | None = None,
    mal_conditions_en: list[str] | None = None,
    mal_extra: dict[str, Any] | None = None,
    agriculture_block: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "hijri_year": hijri_year,
        "gregorian_year": gregorian_year,
        "last_updated": last_updated,
        "status": status,
        "country_code": country_code.upper(),
        "country_name_ar": country_name_ar,
        "country_name_en": country_name_en,
        "currency": currency.upper(),
        "official_source_url": official_source_url,
        "zakat_al_fitr": zakat_al_fitr,
        "zakat_categories": {
            "zakat_al_mal": zakat_al_mal(
                nisab_cash,
                mal_conditions_ar,
                mal_conditions_en,
                mal_extra,
            ),
            "agriculture": agriculture_block or agriculture(),
            "livestock": livestock(),
            "treasures_and_minerals": treasures_and_minerals(),
        },
        "asnaf_al_zakat": deepcopy(ASNAF),
    }
