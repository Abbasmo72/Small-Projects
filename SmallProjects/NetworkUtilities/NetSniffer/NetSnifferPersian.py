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
