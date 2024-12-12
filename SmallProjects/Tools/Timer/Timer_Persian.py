import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # تبدیل ثانیه‌ها به دقیقه و ثانیه
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # نمایش زمان در یک خط
        time.sleep(1)  # توقف به مدت یک ثانیه
        seconds -= 1
    
    print("زمان تمام شد!")

# مدت زمان شمارش معکوس (به ثانیه)
duration = int(input("مدت زمان شمارش معکوس (به ثانیه) را وارد کنید: "))
countdown_timer(duration)
