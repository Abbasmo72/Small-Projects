<div align="center">

# پروژه های کوچک با پایتون
<img alt="Gif" src="https://media3.giphy.com/media/coxQHKASG60HrHtvkt/giphy.gif" height="250px" width="500px">
</div>
<hr>

[Click to see the descriptions in English language](README.md)<br>

هر بخش دارای یک فایل README به زبان انگلیسی و فارسی در فایل مربوطه می باشد. با کلیک بر روی پیوندهای هر بخش، می توانید اطلاعات عمیق بیشتری در مورد کد و عملکرد آن کسب کنید.
<hr>

## عملیات روی فایل
1.  ساخت PDF : : این کد یک برنامه گرافیکی با استفاده از کتابخانه Tkinter در پایتون ایجاد می‌کند که امکان تولید فایل‌های PDF را فراهم می‌سازد. کاربر می‌تواند متن دلخواه خود را در جعبه متنی وارد کرده و با فشردن دکمه، فایل PDF خروجی ایجاد کند. برای ایجاد فایل PDF، از کتابخانه ReportLab استفاده شده است که قابلیت پشتیبانی از فونت فارسی را نیز دارد. متن وارد شده در یک جعبه متنی (Text Box) ذخیره شده و خطوط آن در صفحات PDF با مدیریت موقعیت مکانی نوشته می‌شوند. این برنامه برای ساخت اسناد متنی ساده با پشتیبانی از زبان فارسی مناسب است.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/FileOperations/CeratePDF/CeratePDF_English.md)</b> و <b>[Persian README.md](SmallProjects/FileOperations/CeratePDF/CeratePDF_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/FileOperations/CeratePDF/PDF_Persian.py)</b>.
2. چک کردن کد پایتون: این برنامه یک واسط گرافیکی با استفاده از کتابخانه Tkinter ایجاد می‌کند که امکان بررسی صحت سینتکسی کد پایتون را فراهم می‌کند. از ماژول ast برای تجزیه و تحلیل کد و شناسایی خطاهای سینتکسی استفاده شده است و خطاهای موجود به همراه شماره خط به کاربر گزارش می‌شوند. شماره خطوط در یک جعبه متنی جداگانه نمایش داده می‌شود که به طور خودکار با هر تغییر در متن کد به‌روزرسانی می‌شود. دو جعبه متنی در قاب کناری چیده شده‌اند؛ یکی برای شماره خطوط و دیگری برای ورودی کد کاربر. با استفاده از دکمه "Check Syntax"، کاربر می‌تواند بررسی صحت کد را اجرا کرده و نتیجه را مشاهده کند.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/FileOperations/ChekCodePython/CodeCheker_English.md)</b> و <b>[Persian README.md](SmallProjects/FileOperations/ChekCodePython/CodeCheker_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/FileOperations/ChekCodePython/CodeCheker_Persian.py)</b>.

<hr>

## ابزارهای شبکه
1. پیدا کردن IP: این کد به زبان پایتون نوشته شده و برای دریافت و نمایش آدرس IP عمومی کاربر طراحی شده است. با استفاده از کتابخانه urllib.request، یک درخواست به API سرویس ipify ارسال می‌شود تا آدرس IP کاربر بازیابی شود. در صورت موفقیت، آدرس IP دریافت شده به صورت متنی چاپ می‌شود. در صورتی که خطایی رخ دهد، پیام خطا نمایش داده خواهد شد. این کد قابلیت اجرا به صورت مستقل را دارد و عملکرد آن از طریق بخش if __name__ == "__main__": تضمین می‌شود.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/NetworkUtilities/GetIP/GetIP_English.md)</b> و <b>[Persian README.md](SmallProjects/NetworkUtilities/GetIP/GetIP_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/NetworkUtilities/GetIP/GetIP_Persian.py)</b>.
2. کد فوق تابعی به نام is_secure_website تعریف می‌کند که بررسی می‌کند آیا یک وب‌سایت با استفاده از HTTPS امن است یا خیر. این تابع با استفاده از کتابخانه requests، درخواست HTTP به URL داده‌شده ارسال کرده و از گواهینامه‌های معتبر موجود در کتابخانه certifi برای اعتبارسنجی استفاده می‌کند. اگر درخواست موفقیت‌آمیز باشد و URL با https شروع شود، وب‌سایت امن تلقی می‌شود. در صورت بروز هر گونه خطا مانند URL نامعتبر یا مشکل در اتصال، نتیجه به صورت ناامن اعلام می‌شود. در نهایت، کاربر می‌تواند URL یک وب‌سایت را وارد کرده و نتیجه را مشاهده کند.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/NetworkUtilities/SSLShield/SSLShield_ٍEnglish.md)</b> و <b>[Persian README.md](SmallProjects/NetworkUtilities/SSLShield/SSLShield_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/NetworkUtilities/SSLShield/SSLShield_Persian.py)</b>.
<hr>

## عملیات سیستم
1. آلارم باطری: برنامه با استفاده از کتابخانه‌های psutil و pygame، وضعیت باتری و اتصال دستگاه به برق را بررسی کرده و در صورت نیاز آلارم پخش می‌کند. با دستور pygame.mixer.init تنظیمات پخش صدا آماده‌سازی می‌شود. در یک حلقه بی‌نهایت، برنامه وضعیت باتری و اتصال برق را بررسی می‌کند و در صورت قطع اتصال، فایل صوتی sg.mp3 به صورت مداوم پخش می‌شود. اگر دستگاه مجدداً به برق متصل شود، پخش آلارم متوقف می‌شود. بررسی وضعیت هر ثانیه یک بار انجام می‌گیرد.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/SystemOprations/AlarmBattrey/AllarmBattery_ٍEnglish.md)</b> و <b>[Persian README.md](SmallProjects/SystemOprations/AlarmBattrey/AllarmBattery_ٍPersian.md)</b> و کد کامل <b>[Python Code](SmallProjects/SystemOprations/AlarmBattrey/AllarmBattery_ٍPersian.py)</b>.
2. دیدن باطری: کد ابتدا با استفاده از تابع psutil.sensors_battery() اطلاعات مربوط به باتری را دریافت می‌کند و بررسی می‌کند که آیا این اطلاعات موجود است یا خیر. اگر اطلاعات باتری وجود داشته باشد، درصد شارژ باتری و وضعیت اتصال به برق را چاپ می‌کند. سپس تابعی به نام convertTime تعریف می‌شود که زمان باقی‌مانده باتری را از واحد ثانیه به فرمت ساعت:دقیقه:ثانیه تبدیل می‌کند. در ادامه، زمان باقی‌مانده باتری با استفاده از این تابع نمایش داده می‌شود. اگر اطلاعات باتری در دسترس نباشد، پیام "No battery information available." چاپ می‌شود.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/SystemOprations/BatteryMonitor/BatteryMonitor_English.md)</b> و <b>[Persian README.md](SmallProjects/SystemOprations/BatteryMonitor/BatteryMonitor_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/SystemOprations/BatteryMonitor/BatteryMonitor_Persian.py)</b>.

<hr>

## اسکریپت های وب
1. اسخراج جداول(از هر سایت با فرمت CSV): این کد یک ابزار وب‌اسکرپینگ ساده است که با استفاده از کتابخانه‌های پایتون مانند requests، BeautifulSoup و pandas، اطلاعات موجود در جداول یک وبسایت را استخراج می‌کند. ابتدا، با استفاده از requests.get محتوای HTML صفحه را دریافت می‌کند. سپس با BeautifulSoup این محتوا تجزیه شده و جداول دارای کلاس wikitable شناسایی می‌شوند. هر جدول استخراج شده به کمک pandas.read_html به یک DataFrame تبدیل می‌شود. در نهایت، این جداول می‌توانند برای تحلیل‌های بیشتر به فایل‌های CSV تبدیل شوند. این کد برای جمع‌آوری داده‌های ساختارمند از صفحات وب بسیار کاربردی است.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/WebScripts/FindTable/FindTable_English.md)</b> و <b>[Persian README.md](SmallProjects/WebScripts/FindTable/FindTable_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/WebScripts/FindTable/FindTable_Persian.py)</b>.

