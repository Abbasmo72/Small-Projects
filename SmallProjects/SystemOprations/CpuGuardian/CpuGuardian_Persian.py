import psutil
import time

class CpuMonitor:
    def __init__(self, max_usage=80, check_interval=1):
        self.max_usage = max_usage  # حد مصرف CPU
        self.check_interval = check_interval  # فاصله زمانی بین بررسی‌ها

    def check_cpu_usage(self):
        """بررسی مصرف فعلی CPU"""
        usage = psutil.cpu_percent(interval=self.check_interval)
        print(f"مصرف CPU: {usage}%")
        return usage

    def monitor_cpu(self):
        """نظارت مداوم بر مصرف CPU و هشدار در صورت عبور از حد مجاز"""
        while True:
            usage = self.check_cpu_usage()
            if usage > self.max_usage:
                print(f"هشدار: مصرف CPU از {self.max_usage}% بیشتر شد!")
                self.take_action()
            time.sleep(self.check_interval)

    def take_action(self):
        """اقدام در صورت عبور مصرف CPU از حد مجاز"""
        print("در حال انجام اقدامات برای کاهش مصرف CPU...")
        # به عنوان مثال می‌توانید برنامه‌های پرمصرف را متوقف کنید
        # مثلاً با استفاده از psutil می‌توانید پروسه‌هایی که CPU زیادی مصرف می‌کنند را شناسایی کرده و متوقف کنید
        # این قسمت می‌تواند بر اساس نیاز شما تغییر یابد.

        # به عنوان نمونه، لیست پروسه‌ها را می‌گیریم و پروسه‌های پرمصرف را نمایش می‌دهیم
        processes = psutil.process_iter(['pid', 'name', 'cpu_percent'])
        high_cpu_processes = [p for p in processes if p.info['cpu_percent'] > 20]

        if high_cpu_processes:
            print("پروسه‌های با مصرف CPU بالا:")
            for proc in high_cpu_processes:
                print(f"PID: {proc.info['pid']} - نام: {proc.info['name']} - مصرف CPU: {proc.info['cpu_percent']}%")
                # اگر لازم باشد می‌توانید این پروسه‌ها را متوقف کنید:
                # proc.terminate()  # این خط پروسه را متوقف می‌کند
        else:
            print("هیچ پروسه‌ای با مصرف بالا پیدا نشد.")

if __name__ == "__main__":
    cpu_monitor = CpuMonitor(max_usage=80, check_interval=1)  # حد مصرف 80% و فاصله زمانی 1 ثانیه
    cpu_monitor.monitor_cpu()
