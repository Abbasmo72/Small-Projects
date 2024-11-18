import pandas as pd  # وارد کردن کتابخانه pandas برای کار با دیتا فریم‌ها و عملیات CSV
import requests  # وارد کردن کتابخانه requests برای دریافت محتوای وب
from bs4 import BeautifulSoup  # وارد کردن BeautifulSoup از کتابخانه bs4 برای تجزیه HTML

# دریافت صفحه HTML از وب‌سایت
url = "اسم سایت را وارد کنید"  # آدرس URL سایت مورد نظر را وارد کنید
response = requests.get(url)  # ارسال درخواست GET به سایت
soup = BeautifulSoup(response.text, 'html.parser')  # تجزیه محتوای HTML پاسخ

# پیدا کردن تمامی جداول با کلاس 'wikitable'
tables = soup.find_all('table', {'class': 'wikitable'})  # جستجوی تمامی جداول با کلاس مشخص شده

# تبدیل جداول به فایل‌های CSV
for i, table in enumerate(tables):  # تکرار روی هر جدول پیدا شده
    df = pd.read_html(str(table))[0]  # تبدیل جدول HTML به DataFrame پانداس
    df.to_csv(f"table_{i + 1}.csv", index=False)  # ذخیره DataFrame به عنوان فایل CSV
