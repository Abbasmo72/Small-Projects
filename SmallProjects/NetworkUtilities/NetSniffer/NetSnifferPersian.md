### نظارت شبکه
این کد یک اسکریپت برای نظارت بر ترافیک شبکه است که از کتابخانه scapy برای دریافت و تحلیل بسته‌های شبکه استفاده می‌کند. کد به این صورت عمل می‌کند:

<hr>

### بخش‌های مختلف کد:
## 1. وارد کردن کتابخانه‌ها:
- کتابخانه scapy.all: برای استفاده از ابزارهای مرتبط با شبکه مانند sniff (برای دریافت بسته‌های شبکه)، get_if_list (برای گرفتن لیست رابط‌های شبکه) و conf (برای تنظیمات پیکربندی شبکه).
- کتابخانه datetime: برای دریافت تاریخ و زمان فعلی.
- کتابخانه threading.Thread: برای اجرای نظارت شبکه در یک نخ جداگانه (برای انجام همزمان عملیات).
- کتابخانه json: برای نوشتن داده‌ها در فرمت JSON به فایل.
- کتابخانه time: برای اندازه‌گیری مدت زمان اجرا.
## 2. تشخیص دسترسی غیرمجاز
- تابع detect_unauthorized_access وظیفه پردازش هر بسته دریافتی را دارد:
    - در این تابع، زمان فعلی در قالبی استاندارد (YYYY-MM-DD HH:MM:SS) ثبت می‌شود.
    - خلاصه‌ای از اطلاعات بسته با استفاده از متد packet.summary() استخراج می‌شود.
    - داده‌های جمع‌آوری‌شده در قالب یک شی JSON (شامل زمان و خلاصه بسته) ذخیره می‌شوند.
    - فایل لاگ (network_logs.json) به‌صورت الحاقی باز می‌شود و اطلاعات به آن اضافه می‌گردد.
    - اگر خطایی در فرآیند ذخیره‌سازی رخ دهد، برنامه با پیام خطا کاربر را مطلع می‌کند.
## 3. پایش شبکه
- تابع monitor_network ترافیک شبکه را بررسی می‌کند:
   - کاربر می‌تواند رابط شبکه (interface)، مدت زمان پایش و نوع بسته‌های هدف (فیلتر بسته‌ها) را مشخص کند.
   - اگر کاربر رابط خاصی انتخاب نکند، برنامه از رابط پیش‌فرض سیستم استفاده می‌کند.
   - با استفاده از sniff (تابعی از Scapy)، بسته‌ها دریافت می‌شوند و برای هر بسته، تابع detect_unauthorized_access فراخوانی می‌شود.
   - گزینه‌های store=False و timeout=duration تضمین می‌کنند که حافظه بیهوده اشغال نشود و فرآیند پایش محدود به زمان تعیین‌شده باشد.
## 4. اجرای پایش
- تابع monitor_in_thread عملیات پایش شبکه را در یک نخ جداگانه اجرا می‌کند:
  - این طراحی اجازه می‌دهد که برنامه اصلی مسدود نشود و به تعامل با کاربر ادامه دهد.
  - برای هر عملیات پایش، یک نخ جدید ایجاد شده و پس از پایان، به برنامه اصلی بازمی‌گردد.
 ## 5. ورودی کاربر و تنظیمات برنامه
- در بخش اصلی برنامه:
  - لیست رابط‌های شبکه با استفاده از get_if_list نمایش داده می‌شود.
  - کاربر می‌تواند رابط شبکه و مدت زمان پایش را تعیین کند. اگر اطلاعات واردشده نامعتبر باشد، برنامه از مقادیر پیش‌فرض استفاده می‌کند.
  - فیلتر بسته‌ها نیز یک ورودی اختیاری است که امکان تحلیل دقیق‌تر را فراهم می‌کند.
- ویژگی‌های قابل توجه:
  - نمایش رابط‌های موجود، کاربر را در انتخاب رابط مناسب یاری می‌کند.
  - مقادیر پیش‌فرض، برنامه را برای استفاده آسان‌تر توسط کاربران مبتدی مناسب می‌سازد.
## 6. لاگ‌ها و مدت زمان اجرا
- زمان شروع و پایان فرآیند پایش ثبت می‌شود تا مدت زمان اجرای برنامه محاسبه شود.
- در انتها، کاربر مطلع می‌شود که لاگ‌ها در کجا ذخیره شده‌اند.
## 7. کاربردهای عملی
- نظارت بر ترافیک شبکه برای شناسایی فعالیت‌های مشکوک.
- تحلیل داده‌های ثبت‌شده برای بهبود امنیت سایبری.
- ابزار آموزشی برای یادگیری تحلیل شبکه و امنیت اطلاعات.<br>
این برنامه با وجود طراحی ساده، پایه‌ای قدرتمند برای گسترش به ابزارهای پیچیده‌تر فراهم می‌کند.
<hr>

## کد پایتون
```python
from scapy.all import sniff, get_if_list, conf
from datetime import datetime
from threading import Thread
import json
import time

def detect_unauthorized_access(packet):
    """جزئیات بسته را در یک فایل JSON ثبت می‌کند."""
    # دریافت زمان فعلی به فرمت YYYY-MM-DD HH:MM:SS
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # ایجاد ورودی لاگ شامل زمان و خلاصه بسته
    log_entry = {"timestamp": timestamp, "packet_summary": packet.summary()}
    try:
        # باز کردن فایل 'network_logs.json' برای افزودن داده جدید
        with open("network_logs.json", "a") as log_file:
            log_file.write(json.dumps(log_entry) + "\n")  # نوشتن داده‌ها در فایل JSON
    except IOError as e:
        # در صورت بروز خطا در نوشتن، پیغام خطا چاپ می‌شود
        print(f"Error writing to log file: {e}")

def monitor_network(interface=None, duration=60, packet_filter=None):
    """نظارت بر ترافیک شبکه در یک رابط خاص."""
    # اگر رابط شبکه مشخص نشده باشد، از رابط پیش‌فرض سیستم استفاده می‌شود
    if interface is None:
        interface = conf.iface  # استفاده از رابط پیش‌فرض

    print(f"Monitoring network on interface: {interface} for {duration} seconds")

    try:
        # شروع به دریافت بسته‌ها با استفاده از تابع sniff از کتابخانه scapy
        sniff(
            iface=interface,  # رابط شبکه
            prn=detect_unauthorized_access,  # تابعی که برای هر بسته اجرا می‌شود
            store=False,  # از ذخیره‌سازی بسته‌ها جلوگیری می‌شود
            timeout=duration,  # مدت زمان نظارت
            filter=packet_filter,  # فیلتر بسته‌ها (اختیاری)
        )
    except Exception as e:
        # در صورت بروز خطا در حین نظارت، پیغام خطا چاپ می‌شود
        print(f"Error occurred while monitoring: {e}")

def monitor_in_thread(interface, duration, packet_filter=None):
    """نظارت بر شبکه را در یک نخ جداگانه اجرا می‌کند."""
    # ایجاد نخ جدید برای اجرای تابع نظارت در پس‌زمینه
    thread = Thread(target=monitor_network, args=(interface, duration, packet_filter))
    thread.start()  # شروع به اجرای نخ
    thread.join()  # منتظر می‌ماند تا نخ تکمیل شود

if __name__ == "__main__":
    # نمایش رابط‌های شبکه موجود
    print("Available interfaces:", get_if_list())

    # دریافت ورودی‌های کاربر برای رابط و مدت زمان نظارت
    interface = input("Enter the network interface (default: system default): ") or conf.iface
    try:
        # دریافت مدت زمان نظارت از کاربر
        duration = int(input("Enter the monitoring duration in seconds (default: 60): ") or 60)
    except ValueError:
        # در صورت وارد کردن مقدار اشتباه، از مقدار پیش‌فرض استفاده می‌شود
        print("Invalid duration. Using default value of 60 seconds.")
        duration = 60

    # دریافت فیلتر بسته (اختیاری)
    packet_filter = input("Enter a packet filter (e.g., 'tcp or udp', default: None): ") or None

    # شروع به نظارت بر شبکه
    start_time = time.time()
    monitor_in_thread(interface, duration, packet_filter)
    end_time = time.time()

    # نمایش مدت زمان اجرای نظارت و مکان ذخیره‌سازی لاگ‌ها
    print(f"Monitoring completed. Duration: {end_time - start_time:.2f} seconds")
    print("Logs saved in 'network_logs.json'")

```
