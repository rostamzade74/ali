from typing import List, Tuple

# نقشه ای ساده از کلیدواژه های مربوط به هر رشته و صلاحیت های مرتبط
CATEGORIES = {
    "ارزیابی املاک": {
        "keywords": ["زمین", "ساختمان", "ملک", "خانه"],
        "competencies": ["ارزیابی املاک و مستغلات", "برآورد قیمت زمین"]
    },
    "خط و امضا": {
        "keywords": ["امضا", "دست خط", "سند", "اصالت"],
        "competencies": ["تشخیص اصالت اسناد", "بررسی جعل"]
    },
    "حسابداری": {
        "keywords": ["حساب", "مالی", "حسابرسی", "تراز"],
        "competencies": ["بررسی حساب ها", "حسابرسی مالی"]
    },
    "وسایل نقلیه": {
        "keywords": ["خودرو", "تصادف", "وسیله نقلیه", "خسارت"],
        "competencies": ["ارزیابی خسارت خودرو", "تشخیص علت تصادف"]
    },
    "امور بانکی": {
        "keywords": ["بانک", "وام", "اعتبار", "حساب بانکی"],
        "competencies": ["بررسی امور بانکی", "محاسبه بهره"]
    }
}


def analyze_text(text: str) -> Tuple[List[str], List[str]]:
    """بر اساس متن ورودی، ۵ رشته مرتبط و صلاحیت های آن را پیشنهاد می دهد."""
    text = text or ""
    found = []
    for category, info in CATEGORIES.items():
        for kw in info["keywords"]:
            if kw in text:
                found.append(category)
                break
    # اگر کمتر از ۵ رشته پیدا شد، بقیه را به صورت تصادفی اضافه می کنیم
    all_categories = list(CATEGORIES.keys())
    while len(found) < 5 and all_categories:
        cat = all_categories.pop(0)
        if cat not in found:
            found.append(cat)
    # استخراج صلاحیت ها بر اساس رشته های پیدا شده
    competencies: List[str] = []
    for cat in found:
        competencies.extend(CATEGORIES[cat]["competencies"])
    # حذف تکرار
    competencies = list(dict.fromkeys(competencies))
    return found[:5], competencies
