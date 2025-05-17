from dataclasses import dataclass
from typing import List
import random

@dataclass
class Expert:
    name: str
    category: str
    competencies: List[str]

# دیتاست نمونه کارشناسان
EXPERTS = [
    Expert(name="علی رضایی", category="ارزیابی املاک", competencies=["ارزیابی املاک و مستغلات"]),
    Expert(name="مینا محمدی", category="ارزیابی املاک", competencies=["برآورد قیمت زمین"]),
    Expert(name="حسین کریمی", category="خط و امضا", competencies=["تشخیص اصالت اسناد"]),
    Expert(name="سارا احمدی", category="خط و امضا", competencies=["بررسی جعل"]),
    Expert(name="مجید صادقی", category="حسابداری", competencies=["بررسی حساب ها"]),
    Expert(name="ندا قاسمی", category="حسابداری", competencies=["حسابرسی مالی"]),
    Expert(name="کامران اکبری", category="وسایل نقلیه", competencies=["ارزیابی خسارت خودرو"]),
    Expert(name="الهام نوروزی", category="وسایل نقلیه", competencies=["تشخیص علت تصادف"]),
    Expert(name="فرزاد طاهری", category="امور بانکی", competencies=["بررسی امور بانکی"]),
    Expert(name="شیوا اسدی", category="امور بانکی", competencies=["محاسبه بهره"]),
    # چند کارشناس اضافی برای تنوع
    Expert(name="محمد مرادی", category="حسابداری", competencies=["بررسی حساب ها", "حسابرسی مالی"]),
    Expert(name="لیلا غلامی", category="ارزیابی املاک", competencies=["ارزیابی املاک و مستغلات"]),
    Expert(name="حمید طالبی", category="وسایل نقلیه", competencies=["ارزیابی خسارت خودرو"]),
    Expert(name="پریسا نادری", category="خط و امضا", competencies=["تشخیص اصالت اسناد"]),
    Expert(name="رضا سلیمانی", category="امور بانکی", competencies=["بررسی امور بانکی"]),
]


def find_experts(category: str, limit: int = 10) -> List[Expert]:
    """بر اساس رشته، تعدادی کارشناس برمی گرداند"""
    matches = [e for e in EXPERTS if e.category == category]
    random.shuffle(matches)
    return matches[:limit]
