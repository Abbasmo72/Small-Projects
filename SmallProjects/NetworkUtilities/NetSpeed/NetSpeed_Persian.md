## اندازه‌گیری پهنای باند شبکه با استفاده از psutil
این کد با استفاده از کتابخانه psutil میزان داده‌های ارسالی و دریافتی شبکه را در یک بازه زمانی مشخص اندازه‌گیری می‌کند. مراحل کلی عملکرد کد عبارت‌اند از:
1. دریافت داده‌های اولیه شبکه: از طریق تابع psutil.net_io_counters() اطلاعات مربوط به میزان داده‌های ارسالی (bytes_sent) و دریافتی (bytes_recv) شبکه جمع‌آوری می‌شود.
2. تاخیر زمانی: کد با استفاده از تابع time.sleep() به مدت زمان مشخصی منتظر می‌ماند تا میزان تغییرات داده‌های شبکه را محاسبه کند.
3. محاسبه پهنای باند: تغییرات در مقادیر ارسالی و دریافتی شبکه بین دو زمان اندازه‌گیری شده، تقسیم بر زمان تاخیر، محاسبه شده و به صورت پهنای باند (به واحد بایت بر ثانیه) نمایش داده می‌شود.
4. خروجی: نتایج محاسبات، شامل میزان ارسال و دریافت داده، به صورت خوانا چاپ می‌شوند.
   
این کد به ویژه برای مانیتورینگ ساده و لحظه‌ای پهنای باند شبکه مفید است و می‌تواند در ابزارهای مدیریت شبکه یا اسکریپت‌های نظارتی استفاده شود.

## کد پایتون
```python
import psutil
import time

def measure_bandwidth():
    # دریافت اطلاعات اولیه از پهنای باند
    old_value = psutil.net_io_counters()
    old_bytes_recv = old_value.bytes_recv
    old_bytes_sent = old_value.bytes_sent

    # زمان شروع
    start_time = time.time()

    # مدت زمانی که برای اندازه‌گیری پهنای باند استفاده می‌کنیم
    time.sleep(1)  # به مدت 1 ثانیه اندازه‌گیری می‌کنیم

    # دریافت اطلاعات جدید از پهنای باند
    new_value = psutil.net_io_counters()
    new_bytes_recv = new_value.bytes_recv
    new_bytes_sent = new_value.bytes_sent

    # محاسبه سرعت دانلود و آپلود
    download_speed = (new_bytes_recv - old_bytes_recv) / 1024  # به کیلوبایت در ثانیه
    upload_speed = (new_bytes_sent - old_bytes_sent) / 1024  # به کیلوبایت در ثانیه

    # محاسبه مدت زمان
    end_time = time.time()

    # نمایش نتیجه
    print(f"Download Speed: {download_speed:.2f} KB/s")
    print(f"Upload Speed: {upload_speed:.2f} KB/s")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    measure_bandwidth()
```

