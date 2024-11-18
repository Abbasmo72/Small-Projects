import psutil
import time
import pygame

# پیکربندی pygame برای پخش صدا
pygame.mixer.init()

def battery_alert():
    alert_playing = False  # بررسی اینکه آیا هشدار در حال پخش است یا خیر
    
    while True:
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged  # وضعیت اتصال به برق

        if not plugged and not alert_playing:  # اگر برق قطع شده باشد و صدای هشدار هنوز پخش نشده باشد
            print("برق قطع شده است! از باتری استفاده می‌شود.")
            pygame.mixer.music.load("sg.mp3")  # بارگذاری فایل صدا
            pygame.mixer.music.play(-1)  # پخش مداوم صدا
            alert_playing = True  # وضعیت هشدار به پخش تنظیم شود

        elif plugged and alert_playing:  # اگر باتری به برق متصل شده باشد و صدا در حال پخش باشد
            print("باتری به برق متصل شد. آلارم متوقف شد.")
            pygame.mixer.music.stop()  # توقف پخش صدا
            alert_playing = False  # وضعیت هشدار به غیرفعال تنظیم شود
        
        time.sleep(1)  # هر ۱ ثانیه وضعیت چک شود

battery_alert()

