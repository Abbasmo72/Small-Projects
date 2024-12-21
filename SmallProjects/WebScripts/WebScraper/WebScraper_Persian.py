import requests
from bs4 import BeautifulSoup

# URL هدف
url = 'https://example.com'  # آدرس وبسایت خود را اینجا وارد کنید

# ارسال درخواست به وبسایت
response = requests.get(url)

# بررسی وضعیت درخواست
if response.status_code == 200:
    # ساخت پارس از محتوای HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # استخراج داده‌ها از HTML (مثال: استخراج تمام تگ‌های <h1>)
    headers = soup.find_all('h1')

    # نمایش داده‌های استخراج شده
    for header in headers:
        print(header.text)
else:
    print(f"Failed to retrieve the webpage: {response.status_code}")
