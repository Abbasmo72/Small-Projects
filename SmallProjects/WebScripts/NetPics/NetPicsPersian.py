import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def download_images(url, folder_name):
    # بررسی اینکه آیا فولدر وجود دارد یا نه
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)  # ساخت فولدر در صورت عدم وجود

    # درخواست برای دریافت HTML صفحه
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # پیدا کردن تمام تگ‌های img در صفحه
    img_tags = soup.find_all('img')

    for img in img_tags:
        # گرفتن آدرس تصویر از تگ
        img_url = img.get('src')
        if not img_url:
            continue  # اگر URL تصویر وجود نداشت، ادامه بده
        img_url = urljoin(url, img_url)  # کامل کردن URL تصویر در صورت نسبی بودن

        # بررسی فرمت تصویر (فقط .png و .jpg مجاز هستند)
        if not img_url.endswith(('.png', '.jpg')):
            continue  # اگر فرمت تصویر معتبر نیست، ادامه بده

        # استخراج نام فایل از URL
        img_name = os.path.basename(img_url)
        
        # حذف کاراکترهای غیرمجاز از نام فایل
        img_name = re.sub(r'[<>:"/\\|?*]', '_', img_name)  # جایگزینی کاراکترهای نامعتبر با '_'

        # مسیر کامل ذخیره فایل
        img_path = os.path.join(folder_name, img_name)

        # دانلود و ذخیره تصویر
        try:
            img_data = requests.get(img_url).content
            with open(img_path, 'wb') as f:
                f.write(img_data)  # نوشتن داده‌های تصویر در فایل
            print(f'تصویر دانلود شد: {img_path}')  # پیام موفقیت
        except requests.exceptions.RequestException as e:
            print(f'خطا در دانلود {img_url}: {e}')  # پیام خطا در صورت مشکل

# گرفتن ورودی آدرس سایت و نام فولدر از کاربر
website_url = input("آدرس وب‌سایت را وارد کنید: ")  # آدرس وب‌سایت
folder_name = input("نام فولدر برای ذخیره تصاویر را وارد کنید: ")  # نام فولدر برای ذخیره تصاویر

# فراخوانی تابع برای دانلود تصاویر
download_images(website_url, folder_name)
