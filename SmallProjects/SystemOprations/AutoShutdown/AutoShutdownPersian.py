import os
import time

def schedule_shutdown():
    try:
        # گرفتن مدت زمان خاموش شدن از کاربر (به دقیقه)
        minutes = int(input("مدت زمان (به دقیقه) تا خاموش شدن سیستم را وارد کنید: "))
        # محاسبه مدت زمان به ثانیه
        seconds = minutes * 60

        print(f"سیستم در {minutes} دقیقه خاموش خواهد شد...")
        time.sleep(seconds)  # انتظار برای مدت زمان تعیین شده

        # اجرای دستور خاموش کردن سیستم
        if os.name == "nt":  # ویندوز
            os.system("shutdown /s /t 1")
        elif os.name == "posix":  # لینوکس/مک
            os.system("shutdown -h now")
        else:
            print("سیستم‌عامل شما پشتیبانی نمی‌شود.")
    except ValueError:
        print("لطفاً یک عدد معتبر وارد کنید.")

if __name__ == "__main__":
    schedule_shutdown()
