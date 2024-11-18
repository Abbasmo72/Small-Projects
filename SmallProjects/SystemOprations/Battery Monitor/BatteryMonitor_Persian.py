import psutil

# دریافت اطلاعات باتری
battery = psutil.sensors_battery()

if battery is not None:
    # چاپ درصد شارژ باتری
    print("درصد باتری:", battery.percent, "%")
    
    # چاپ وضعیت اتصال به برق
    print("اتصال به برق:", battery.power_plugged)

    def convertTime(seconds):
        # تبدیل ثانیه‌ها به فرمت ساعت:دقیقه:ثانیه
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hours, minutes, seconds)

    # چاپ زمان باقی‌مانده باتری
    print("زمان باقی‌مانده باتری:", convertTime(battery.secsleft))
else:
    # چاپ پیام در صورت عدم وجود اطلاعات باتری
    print("اطلاعات باتری موجود نیست.")
