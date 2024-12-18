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
