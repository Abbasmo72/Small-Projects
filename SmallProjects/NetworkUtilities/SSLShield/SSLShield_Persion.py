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
