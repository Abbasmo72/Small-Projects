import calendar

def display_calendar():
    # درخواست از کاربر برای وارد کردن سال
    year = int(input("Enter year: "))
    
    # درخواست از کاربر برای وارد کردن ماه (عدد بین 1 تا 12)
    month = int(input("Enter month (1-12): "))

    # ایجاد یک شیء از کلاس TextCalendar با شروع هفته از یکشنبه
    cal = calendar.TextCalendar(calendar.SUNDAY)
    
    # دریافت تقویم ماه به صورت متنی برای سال و ماه وارد شده
    month_calendar = cal.formatmonth(year, month)
    
    # نمایش تقویم ماه وارد شده
    print(month_calendar)

# فراخوانی تابع برای نمایش تقویم
display_calendar()
