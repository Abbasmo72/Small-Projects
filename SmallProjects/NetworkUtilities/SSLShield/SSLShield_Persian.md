## بررسی ایمنی وب‌سایت‌ها با استفاده از HTTPS و گواهی‌نامه SSL در پایتون
این کد پایتون بررسی می‌کند که آیا یک وب‌سایت ایمن است یا خیر. بررسی ایمنی وب‌سایت شامل این می‌شود که آیا از پروتکل HTTPS استفاده می‌کند و آیا گواهی SSL سرور آن معتبر است یا خیر. در ادامه توضیح مفصل این کد آورده شده است:
1. وارد کردن کتابخانه‌ها:
   - کتابخانه certifi که برای دریافت مجموعه‌ای از گواهی‌نامه‌های ریشه برای اعتبارسنجی SSL استفاده می‌شود.
   - کتابخانه requests که یک کتابخانه محبوب برای ارسال درخواست‌های HTTP و مدیریت پاسخ‌ها در پایتون است.
2. تعریف تابع is_secure_website:
   - این تابع آدرس URL یک وب‌سایت را به عنوان ورودی می‌گیرد و ایمنی آن را با ارسال یک درخواست HTTPS و اعتبارسنجی گواهی SSL بررسی می‌کند.
3. ارسال درخواست GET:
   - در داخل تابع، یک درخواست GET به URL داده شده ارسال می‌شود با استفاده از requests.get(url, verify=certifi.where()).
   - پارامتر verify به certifi.where() تنظیم شده است که به مسیر گواهی‌نامه‌های ریشه CA (Certificate Authority) اشاره دارد. این امر باعث می‌شود که گواهی SSL سرور هنگام ارسال درخواست بررسی شود.
4. مدیریت خطاها:
   - متد response.raise_for_status() بررسی می‌کند که آیا پاسخ HTTP موفقیت‌آمیز بوده است یا خیر. اگر پاسخ شامل خطای HTTP (مانند 404 یا 500) باشد، یک استثنا ایجاد می‌شود.
   - هرگونه استثنای رخ داده در حین ارسال درخواست (مانند خطاهای ارتباطی یا URL نامعتبر) توسط بلاک except مدیریت می‌شود و تابع False برمی‌گرداند.
5. بررسی URL که با 'https://' شروع می‌شود:
   - تابع بررسی می‌کند که آیا URL با https:// شروع می‌شود یا خیر، زیرا این پروتکل نشان‌دهنده استفاده از اتصال ایمن (SSL/TLS) است.
   - اگر URL ایمن باشد، True برمی‌گرداند؛ در غیر این صورت، False برمی‌گرداند.
6. بلاک اصلی برنامه (if __name__ == "__main__":):
   - این بلاک اطمینان می‌دهد که کد زیر تنها زمانی اجرا شود که اسکریپت به طور مستقیم اجرا شود و نه زمانی که به عنوان ماژول وارد شود.
   - برنامه از کاربر می‌خواهد که URL یک وب‌سایت را وارد کند.
7. بررسی ایمنی وب‌سایت:
   - تابع is_secure_website با URL وارد شده توسط کاربر فراخوانی می‌شود تا بررسی کند که آیا وب‌سایت ایمن است یا خیر.
   - بر اساس نتیجه (True یا False)، پیام مناسبی چاپ می‌شود که آیا وب‌سایت ایمن است یا خیر.
8. پیام ایمنی وب‌سایت:
   - اگر وب‌سایت ایمن باشد (از HTTPS و گواهی معتبر استفاده کند)، پیام "وب‌سایت ایمن است" چاپ می‌شود.
   - اگر وب‌سایت ایمن نباشد (از HTTP استفاده کند یا اعتبارسنجی گواهی ناموفق باشد)، پیام "وب‌سایت ایمن نیست" چاپ می‌شود.

## ویژگی‌های کد
1. اعتبارسنجی گواهی‌نامه SSL/TLS:
   - استفاده از certifi اطمینان می‌دهد که گواهی‌نامه SSL سرور معتبر است و این باعث افزایش امنیت در تأیید اصالت وب‌سایت می‌شود.
2. مدیریت خطاها:
   - کد خطاهای مختلف مانند مشکلات ارتباطی یا URL نامعتبر را مدیریت کرده و از کرش کردن برنامه جلوگیری می‌کند.
3. بررسی پروتکل HTTPS:
   - علاوه بر اعتبارسنجی گواهی‌نامه SSL، کد بررسی می‌کند که URL با https:// شروع شود، که نشان‌دهنده استفاده از اتصال ایمن است.
4. ورودی از کاربر:
   - برنامه از کاربر درخواست می‌کند تا URL یک وب‌سایت را وارد کند، که این امکان را می‌دهد که وب‌سایت‌های مختلف را بررسی کند.
5. بررسی پروتکل HTTP/HTTPS:
   - با بررسی پروتکل (https://)، کد به راحتی می‌تواند تشخیص دهد که وب‌سایت ایمن است یا خیر.
6. سادگی و کارایی:
   - این برنامه به صورت مختصر و کارا نوشته شده و ابزاری ساده برای بررسی ایمنی وب‌سایت‌ها فراهم می‌کند.

این برنامه برای بررسی ایمنی وب‌سایت‌ها مفید است، به‌ویژه برای اطمینان از اینکه داده‌های حساس از طریق HTTPS و گواهی‌نامه‌های SSL معتبر منتقل می‌شوند.

## کد پایتون
```python
import certifi
import requests

def is_secure_website(url):
    try:
        # ارسال درخواست GET به URL وارد شده با اعتبارسنجی گواهینامه با استفاده از certifi
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()  # بررسی خطاهای HTTP و ایجاد استثنا در صورت وجود
        return response.url.startswith('https://')  # بررسی اینکه آیا URL با 'https' شروع می‌شود
    except requests.exceptions.RequestException:
        # بازگشت False در صورت بروز هرگونه استثنای درخواست (مانند خطای اتصال یا URL نامعتبر)
        return False

if __name__ == "__main__":
    # درخواست از کاربر برای وارد کردن آدرس URL یک وب‌سایت
    website_url = input("Enter the website URL: ")

    # بررسی اینکه آیا وب‌سایت امن است و چاپ نتیجه
    if is_secure_website(website_url):
        print(f"{website_url} is a secure website.")
    else:
        print(f"{website_url} is not a secure website.")

```
