import psutil  # برای کار با اطلاعات سیستم از جمله شبکه
import time  # برای مدیریت زمان و تاخیر

# تابع برای مانیتور کردن ترافیک شبکه
def monitor_network(interval=1):  
    """
    نظارت بر ترافیک شبکه و نمایش تعداد بایت‌های ارسال شده، دریافت شده و مجموع آنها در هر بازه زمانی مشخص.
    
    پارامتر:
        interval: فاصله زمانی (بر حسب ثانیه) برای بروزرسانی اطلاعات (پیش‌فرض: ۱ ثانیه)
    """
    
    # چاپ سربرگ جدول
    print(f"{'Time':<15} {'Bytes Sent':<15} {'Bytes Received':<15} {'Total Bytes':<15}")
    print("=" * 60)  # خط جداکننده برای بهتر دیده شدن جدول
    
    # گرفتن اطلاعات شبکه در لحظه شروع برای مقایسه بعدی
    previous_counters = psutil.net_io_counters()
    
    while True:
        time.sleep(interval)  # مکث به اندازه فاصله زمانی مشخص شده
        
        # گرفتن اطلاعات شبکه در لحظه کنونی
        current_counters = psutil.net_io_counters()
        
        # محاسبه تعداد بایت‌های ارسال شده و دریافت شده در بازه زمانی مشخص
        bytes_sent = current_counters.bytes_sent - previous_counters.bytes_sent
        bytes_received = current_counters.bytes_recv - previous_counters.bytes_recv
        total_bytes = bytes_sent + bytes_received  # محاسبه مجموع بایت‌های جابجا شده
        
        # چاپ اطلاعات به صورت قالب‌بندی شده
        print(f"{time.strftime('%H:%M:%S'):<15} {bytes_sent:<15} {bytes_received:<15} {total_bytes:<15}")
        
        # به‌روزرسانی مقادیر قبلی برای مقایسه در دور بعدی
        previous_counters = current_counters

# اجرای برنامه اصلی
if __name__ == "__main__":
    monitor_network()  # فراخوانی تابع نظارت بر ترافیک شبکه
