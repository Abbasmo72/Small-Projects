<div align="center">

# پروژه های کوچک با پایتون
<img alt="Gif" src="https://media3.giphy.com/media/coxQHKASG60HrHtvkt/giphy.gif" height="250px" width="500px">
</div>
<hr>

[Click to see the descriptions in English language](README.md)<br>

هر بخش دارای یک فایل README به زبان انگلیسی و فارسی در فایل مربوطه می باشد. با کلیک بر روی پیوندهای هر بخش، می توانید اطلاعات عمیق بیشتری در مورد کد و عملکرد آن کسب کنید.
<hr>

# عملیات روی فایل
### 1.  ساخت PDF : 
این کد یک برنامه گرافیکی با استفاده از کتابخانه Tkinter در پایتون ایجاد می‌کند که امکان تولید فایل‌های PDF را فراهم می‌سازد. کاربر می‌تواند متن دلخواه خود را در جعبه متنی وارد کرده و با فشردن دکمه، فایل PDF خروجی ایجاد کند. برای ایجاد فایل PDF، از کتابخانه ReportLab استفاده شده است که قابلیت پشتیبانی از فونت فارسی را نیز دارد. متن وارد شده در یک جعبه متنی (Text Box) ذخیره شده و خطوط آن در صفحات PDF با مدیریت موقعیت مکانی نوشته می‌شوند. این برنامه برای ساخت اسناد متنی ساده با پشتیبانی از زبان فارسی مناسب است.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/FileOperations/CeratePDF/CeratePDF_English.md)</b> و <b>[Persian README.md](SmallProjects/FileOperations/CeratePDF/CeratePDF_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/FileOperations/CeratePDF/PDF_Persian.py)</b>.
### 2. چک کردن کد پایتون: 
این برنامه یک واسط گرافیکی با استفاده از کتابخانه Tkinter ایجاد می‌کند که امکان بررسی صحت سینتکسی کد پایتون را فراهم می‌کند. از ماژول ast برای تجزیه و تحلیل کد و شناسایی خطاهای سینتکسی استفاده شده است و خطاهای موجود به همراه شماره خط به کاربر گزارش می‌شوند. شماره خطوط در یک جعبه متنی جداگانه نمایش داده می‌شود که به طور خودکار با هر تغییر در متن کد به‌روزرسانی می‌شود. دو جعبه متنی در قاب کناری چیده شده‌اند؛ یکی برای شماره خطوط و دیگری برای ورودی کد کاربر. با استفاده از دکمه "Check Syntax"، کاربر می‌تواند بررسی صحت کد را اجرا کرده و نتیجه را مشاهده کند.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/FileOperations/ChekCodePython/CodeCheker_English.md)</b> و <b>[Persian README.md](SmallProjects/FileOperations/ChekCodePython/CodeCheker_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/FileOperations/ChekCodePython/CodeCheker_Persian.py)</b>.

### 3. ادغام فایل های CSV: <br>
این برنامه برای ترکیب چند فایل CSV از یک پوشه مشخص به یک فایل CSV واحد طراحی شده است. فرآیند با بررسی وجود پوشه ورودی آغاز می‌شود و سپس تمام فایل‌های CSV موجود در آن شناسایی می‌شوند. هر فایل به ترتیب با استفاده از کتابخانه pandas خوانده شده و به یک مجموعه داده‌ی واحد اضافه می‌شود، در حالی که از طریق مدیریت خطا، از سلامت داده‌ها اطمینان حاصل می‌شود. پس از پردازش موفقیت‌آمیز تمام فایل‌ها، داده‌های ترکیب‌شده در یک فایل CSV جدید که توسط کاربر مشخص شده است ذخیره می‌شوند. همچنین، پیام‌های اطلاع‌رسانی در هر مرحله ارائه می‌شوند تا کاربر از پیشرفت و مشکلات احتمالی آگاه شود و تجربه‌ای روان و کاربرپسند ایجاد گردد.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/FileOperations/CSVCollector/CSVCollectorEnglish.md)</b> و <b>[Persian README.md](SmallProjects/FileOperations/CSVCollector/CSVCollectorPersian.md)</b> و کد کامل <b>[Python Code](SmallProjects/FileOperations/CSVCollector/CSVCollectorPersian.py)</b>.

### 4. استخراج عکس های موجود در PDF:<br>
می‌کند. ابتدا پوشه‌ای برای ذخیره تصاویر استخراج‌شده ایجاد می‌کند، در صورت نیاز به وجود آن. سپس فایل PDF را باز کرده و صفحات آن را برای یافتن تصاویر بررسی می‌کند. اگر صفحه‌ای دارای اشیای تصویری باشد، داده‌های تصویر را استخراج و با استفاده از PIL به تصویر تبدیل می‌کند. تصاویر در فرمت PNG ذخیره و در پوشه مشخص‌شده ذخیره می‌شوند. کاربر می‌تواند با استفاده از پنجره انتخاب فایل، فایل PDF موردنظر خود را انتخاب کند. پوشه‌ای به نام "extracted_images" در همان مسیر فایل PDF ایجاد شده و تصاویر در آن ذخیره می‌شوند. اگر در فایل PDF هیچ تصویری یافت نشود، پیام مناسب چاپ می‌شود. در صورت وجود خطا در پردازش تصاویر، پیام خطای مرتبط نمایش داده می‌شود. این کد یک رابط کاربری ساده با استفاده از tkinter برای انتخاب فایل ارائه می‌دهد.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/FileOperations/PDFImageSaver/PDFImageSaverEnglish.md)</b> و <b>[Persian README.md](SmallProjects/FileOperations/PDFImageSaver/PDFImageSaverPersian.md)</b> و کد کامل <b>[Python Code](SmallProjects/FileOperations/PDFImageSaver/PDFImageSaverPersian.py)</b>.


<hr>

# ابزارهای شبکه
### 1. پیدا کردن IP: 
این کد به زبان پایتون نوشته شده و برای دریافت و نمایش آدرس IP عمومی کاربر طراحی شده است. با استفاده از کتابخانه urllib.request، یک درخواست به API سرویس ipify ارسال می‌شود تا آدرس IP کاربر بازیابی شود. در صورت موفقیت، آدرس IP دریافت شده به صورت متنی چاپ می‌شود. در صورتی که خطایی رخ دهد، پیام خطا نمایش داده خواهد شد. این کد قابلیت اجرا به صورت مستقل را دارد و عملکرد آن از طریق بخش if __name__ == "__main__": تضمین می‌شود.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/NetworkUtilities/GetIP/GetIP_English.md)</b> و <b>[Persian README.md](SmallProjects/NetworkUtilities/GetIP/GetIP_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/NetworkUtilities/GetIP/GetIP_Persian.py)</b>.
### 2. سپر SSL:
کد فوق تابعی به نام is_secure_website تعریف می‌کند که بررسی می‌کند آیا یک وب‌سایت با استفاده از HTTPS امن است یا خیر. این تابع با استفاده از کتابخانه requests، درخواست HTTP به URL داده‌شده ارسال کرده و از گواهینامه‌های معتبر موجود در کتابخانه certifi برای اعتبارسنجی استفاده می‌کند. اگر درخواست موفقیت‌آمیز باشد و URL با https شروع شود، وب‌سایت امن تلقی می‌شود. در صورت بروز هر گونه خطا مانند URL نامعتبر یا مشکل در اتصال، نتیجه به صورت ناامن اعلام می‌شود. در نهایت، کاربر می‌تواند URL یک وب‌سایت را وارد کرده و نتیجه را مشاهده کند.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/NetworkUtilities/SSLShield/SSLShield_ٍEnglish.md)</b> و <b>[Persian README.md](SmallProjects/NetworkUtilities/SSLShield/SSLShield_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/NetworkUtilities/SSLShield/SSLShield_Persian.py)</b>.
### 3. اندازه‌گیری پهنای باند شبکه: 
این کد از کتابخانه psutil برای اندازه‌گیری سرعت دانلود و آپلود شبکه استفاده می‌کند. ابتدا اطلاعات ورودی/خروجی شبکه قبل و بعد از یک ثانیه زمان خواب گرفته می‌شود. سپس سرعت دانلود و آپلود بر حسب کیلوبایت در ثانیه محاسبه شده و نمایش داده می‌شود. در نهایت، زمان صرف شده برای این اندازه‌گیری نیز نمایش می‌یابد. <br>
برای مشاهده فایل <b>[English README.md](SmallProjects/NetworkUtilities/NetSpeed/NetSpeed_English.md)</b> و <b>[Persian README.md](SmallProjects/NetworkUtilities/NetSpeed/NetSpeed_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/NetworkUtilities/NetSpeed/NetSpeed_Persian.py)</b>.
### 4. مانیتور شبکه: 
این اسکریپت ترافیک شبکه را با استفاده از کتابخانه psutil برای واکشی آمار شبکه و کتابخانه زمان برای کنترل زمان کنترل می کند. این تابع، monitor_network را تعریف می کند که به طور مداوم تعداد بایت های ارسال شده، دریافتی و کل بایت های منتقل شده را در فواصل زمانی منظم محاسبه و نمایش می دهد (پیش فرض 1 ثانیه است). در ابتدا، اسکریپت آمار شبکه جاری را واکشی و ذخیره می کند. در داخل یک حلقه بی نهایت، تفاوت بایت های ارسالی و دریافتی را در مقایسه با آمار قبلی محاسبه می کند، داده ها را در یک جدول قالب بندی شده چاپ می کند و آمارهای قبلی را برای تکرار بعدی به روز می کند. برنامه به طور مداوم اجرا می شود تا زمانی که به صورت دستی متوقف شود.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/NetworkUtilities/NetMonitor/NetMonitor_English.md)</b> و <b>[Persian README.md](SmallProjects/NetworkUtilities/NetMonitor/NetMonitor_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/NetworkUtilities/NetMonitor/NetMonitor_Persian.py)</b>.
### 5. نظارت شبکه:
این کد برای نظارت بر ترافیک شبکه و شناسایی دسترسی‌های غیرمجاز از طریق بسته‌های شبکه نوشته شده است. از کتابخانه scapy برای دریافت و تجزیه بسته‌ها استفاده می‌کند و جزئیات هر بسته را به یک فایل JSON ذخیره می‌کند. نظارت شبکه برای مدت زمان مشخص شده در یک نخ جداگانه انجام می‌شود تا برنامه اصلی متوقف نشود. کاربر می‌تواند رابط شبکه و فیلتر بسته‌ها را به دلخواه انتخاب کند. در نهایت، زمان اجرای برنامه و محل ذخیره‌سازی لاگ‌ها نمایش داده می‌شود.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/NetworkUtilities/NetSniffer/NetSnifferEnglish.md)</b> و <b>[Persian README.md](SmallProjects/NetworkUtilities/NetSniffer/NetSnifferPersian.md)</b> و کد کامل <b>[Python Code](SmallProjects/NetworkUtilities/NetSniffer/NetSnifferPersian.py)</b>.
<hr>

# عملیات سیستم
### 1. آلارم باطری:
برنامه با استفاده از کتابخانه‌های psutil و pygame، وضعیت باتری و اتصال دستگاه به برق را بررسی کرده و در صورت نیاز آلارم پخش می‌کند. با دستور pygame.mixer.init تنظیمات پخش صدا آماده‌سازی می‌شود. در یک حلقه بی‌نهایت، برنامه وضعیت باتری و اتصال برق را بررسی می‌کند و در صورت قطع اتصال، فایل صوتی sg.mp3 به صورت مداوم پخش می‌شود. اگر دستگاه مجدداً به برق متصل شود، پخش آلارم متوقف می‌شود. بررسی وضعیت هر ثانیه یک بار انجام می‌گیرد.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/SystemOprations/AlarmBattrey/AllarmBattery_ٍEnglish.md)</b> و <b>[Persian README.md](SmallProjects/SystemOprations/AlarmBattrey/AllarmBattery_ٍPersian.md)</b> و کد کامل <b>[Python Code](SmallProjects/SystemOprations/AlarmBattrey/AllarmBattery_ٍPersian.py)</b>.
### 2. دیدن باطری: 
کد ابتدا با استفاده از تابع psutil.sensors_battery() اطلاعات مربوط به باتری را دریافت می‌کند و بررسی می‌کند که آیا این اطلاعات موجود است یا خیر. اگر اطلاعات باتری وجود داشته باشد، درصد شارژ باتری و وضعیت اتصال به برق را چاپ می‌کند. سپس تابعی به نام convertTime تعریف می‌شود که زمان باقی‌مانده باتری را از واحد ثانیه به فرمت ساعت:دقیقه:ثانیه تبدیل می‌کند. در ادامه، زمان باقی‌مانده باتری با استفاده از این تابع نمایش داده می‌شود. اگر اطلاعات باتری در دسترس نباشد، پیام "No battery information available." چاپ می‌شود.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/SystemOprations/BatteryMonitor/BatteryMonitor_English.md)</b> و <b>[Persian README.md](SmallProjects/SystemOprations/BatteryMonitor/BatteryMonitor_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/SystemOprations/BatteryMonitor/BatteryMonitor_Persian.py)</b>.
### 3. مصرف CPU:
کد فوق یک برنامه برای مانیتورینگ مصرف CPU است که از کتابخانه psutil استفاده می‌کند. کلاس CpuMonitor با دو ویژگی max_usage برای تعیین حداکثر میزان مصرف قابل قبول CPU و check_interval برای فاصله زمانی بین هر بررسی طراحی شده است. متد check_cpu_usage درصد مصرف CPU را بررسی کرده و نمایش می‌دهد، در حالی که متد monitor_cpu به‌طور مداوم مصرف CPU را پایش کرده و در صورت تجاوز از مقدار تعیین‌شده، هشدار داده و متد take_action را برای مدیریت این وضعیت فراخوانی می‌کند. متد take_action فرآیندهای پرمصرف را شناسایی و اطلاعات آنها را نمایش می‌دهد و در صورت نیاز می‌تواند آنها را متوقف کند. در بخش اصلی برنامه (__main__) یک نمونه از کلاس با تنظیمات دلخواه ایجاد شده و مانیتورینگ آغاز می‌شود. این برنامه می‌تواند به‌طور مؤثر مصرف CPU را در لحظه کنترل و بهینه‌سازی کند.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/SystemOprations/CpuGuardian/CpuGuardian_English.md)</b> و <b>[Persian README.md](SmallProjects/SystemOprations/CpuGuardian/CpuGuardian_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/SystemOprations/CpuGuardian/CpuGuardian_Persian.py)</b>.
### 4. فضای هارد:
کتابخانه‌ی psutil برای دسترسی به اطلاعات سیستم وارد شده است، سپس تابع get_disk_usage تعریف شده که اطلاعات دیسک مانند فضای کل، فضای استفاده‌شده، فضای آزاد و درصد استفاده‌شده را با استفاده از متد disk_usage دریافت می‌کند، مقادیر فضای کل، استفاده‌شده و آزاد از بایت به گیگابایت تبدیل شده‌اند، اطلاعات دیسک به صورت قالب‌بندی شده چاپ می‌شوند و در نهایت با بررسی شرط __name__ == "__main__"، تابع get_disk_usage فراخوانی می‌شود تا اطلاعات دیسک نمایش داده شود.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/SystemOprations/DiskSpace/DiskSpace_English.md)</b> و <b>[Persian README.md](SmallProjects/SystemOprations/DiskSpace/DiskSpace_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/SystemOprations/DiskSpace/DiskSpace_Persian.py)</b>.
### 5. پیدا کردن فایل پایتون:
کتابخانه‌های os و tkinter برای مدیریت فایل‌ها و ایجاد رابط گرافیکی وارد می‌شوند. تابع search_files با پیمایش دایرکتوری‌ها تمام فایل‌های با پسوند مشخص مثل .py را جستجو می‌کند. در تابع on_search_button_click، نام فایل از ورودی دریافت شده و در صورت خالی بودن هشدار داده می‌شود. سپس فایل‌های .py جستجو و مسیرهای حاوی عبارت مورد نظر فیلتر و در Listbox نمایش داده می‌شوند؛ اگر فایلی یافت نشود، پیام اطلاع‌رسانی نشان داده می‌شود. در پایان، با root.mainloop رابط کاربری اجرا شده و برنامه شروع به کار می‌کند.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/SystemOprations/PythonFileFinder/PythonFileFinder_English.md)</b> و <b>[Persian README.md](SmallProjects/SystemOprations/PythonFileFinder/PythonFileFinder_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/SystemOprations/PythonFileFinder/PythonFileFinder_Persian.py)</b>.
### 6.خاموش شدن اتوماتیک:
برنامه با وارد کردن ماژول‌های os و time شروع می‌شود که برای اجرای دستورات سیستم و افزودن تأخیر استفاده می‌شوند. یک تابع به نام schedule_shutdown تعریف شده که منطق زمان‌بندی خاموش شدن سیستم را مدیریت می‌کند. در داخل تابع، از کاربر خواسته می‌شود مدت زمان تأخیر تا خاموش شدن را به دقیقه وارد کند. این مقدار ورودی به ثانیه تبدیل می‌شود، با ضرب آن در ۶۰. برنامه با استفاده از time.sleep برای مدت زمان مشخص شده اجرای خود را متوقف می‌کند. پس از اتمام تأخیر، نوع سیستم‌عامل با استفاده از ویژگی os.name بررسی می‌شود. اگر سیستم‌عامل ویندوز باشد، دستور shutdown /s /t 1 اجرا می‌شود تا سیستم خاموش شود. برای سیستم‌عامل‌های لینوکس یا مک، از دستور shutdown -h now استفاده می‌شود. در صورت وارد کردن مقدار نامعتبر، مانند عدد غیرمجاز یا متن، پیام خطایی نمایش داده شده و برنامه به صورت ایمن متوقف می‌شود.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/SystemOprations/AutoShutdown/AutoShutdownEnglish.md)</b> و <b>[Persian README.md](SmallProjects/SystemOprations/AutoShutdown/AutoShutdownPersian.md)</b> و کد کامل <b>[Python Code](SmallProjects/SystemOprations/AutoShutdown/AutoShutdownPersian.py)</b>.
<hr>

# اسکریپت های وب
### 1. اسخراج جداول(از هر سایت با فرمت CSV): 
این کد یک ابزار وب‌اسکرپینگ ساده است که با استفاده از کتابخانه‌های پایتون مانند requests، BeautifulSoup و pandas، اطلاعات موجود در جداول یک وبسایت را استخراج می‌کند. ابتدا، با استفاده از requests.get محتوای HTML صفحه را دریافت می‌کند. سپس با BeautifulSoup این محتوا تجزیه شده و جداول دارای کلاس wikitable شناسایی می‌شوند. هر جدول استخراج شده به کمک pandas.read_html به یک DataFrame تبدیل می‌شود. در نهایت، این جداول می‌توانند برای تحلیل‌های بیشتر به فایل‌های CSV تبدیل شوند. این کد برای جمع‌آوری داده‌های ساختارمند از صفحات وب بسیار کاربردی است.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/WebScripts/FindTable/FindTable_English.md)</b> و <b>[Persian README.md](SmallProjects/WebScripts/FindTable/FindTable_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/WebScripts/FindTable/FindTable_Persian.py)</b>.
### 2. استخراج تگ عنوان از یک سایت: 
این کد با ارسال یک درخواست HTTP به آدرس مشخص‌شده، محتوای HTML صفحه وب را دریافت می‌کند و اگر درخواست موفقیت‌آمیز باشد، با استفاده از کتابخانه BeautifulSoup محتوای HTML را تحلیل کرده و تمام تگ‌های (h1) را استخراج می‌کند و سپس متن این تگ‌ها را نمایش می‌دهد.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/WebScripts/WebScraper/WebScraper_English.md)</b> و <b>[Persian README.md](SmallProjects/WebScripts/WebScraper/WebScraper_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/WebScripts/WebScraper/WebScraper_Persian.py)</b>.
### 3. استخراج عکس از سایت: 
این اسکریپت کتابخانه‌های موردنیاز مانند os، requests، BeautifulSoup، urljoin و re را برای مدیریت فایل‌ها، ارسال درخواست HTTP، پردازش HTML و کار با عبارات منظم وارد می‌کند. سپس بررسی می‌کند که آیا فولدر مشخص‌شده وجود دارد یا در صورت نبود آن را ایجاد می‌کند تا تصاویر دانلودشده در آن ذخیره شوند. محتوای HTML صفحه وب با استفاده از کتابخانه requests دریافت شده و با استفاده از BeautifulSoup پردازش می‌شود تا تمام تگ‌های <img> استخراج شوند. آدرس تصاویر از ویژگی src هر تگ <img> گرفته شده و در صورت نسبی بودن با استفاده از urljoin به آدرس کامل تبدیل می‌شود. تنها تصاویری که پسوند .png یا .jpg دارند برای دانلود انتخاب می‌شوند. کاراکترهای نامعتبر در نام فایل‌ها با استفاده از re.sub با کاراکتر _ جایگزین می‌شوند تا هنگام ذخیره‌سازی مشکلی ایجاد نشود. تصاویر با requests.get دانلود شده و با نام‌های اصلاح‌شده در فولدر ذخیره می‌شوند. در پایان، اسکریپت از کاربر می‌خواهد آدرس وب‌سایت و نام فولدر را وارد کند و تمام تصاویر معتبر را در فولدر مشخص‌شده دانلود می‌کند.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/WebScripts/NetPics/NetPicsEnglish.md)</b> و <b>[Persian README.md](SmallProjects/WebScripts/NetPics/NetPicsPersian.md)</b> و کد کامل <b>[Python Code](SmallProjects/WebScripts/NetPics/NetPicsPersian.py)</b>.


<hr>

# ابزار
### 1. نمایش تاریخ: 
این کد از کاربر می‌خواهد تا سال و ماه مورد نظر را وارد کند و سپس یک شیء از کلاس TextCalendar با شروع هفته از روز یکشنبه ایجاد می‌کند. با استفاده از متد formatmonth، تقویم ماهانه به صورت متنی تولید می‌شود و در نهایت تقویم تولید شده برای مشاهده کاربر چاپ می‌گردد. تابع display_calendar برای اجرای کل فرآیند فراخوانی می‌شود.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/Tools/CalViewer/CalViewer_English.md)</b> و <b>[Persian README.md](SmallProjects/Tools/CalViewer/CalViewer_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/Tools/CalViewer/CalViewer_Persian.py)</b>.
### 2. پیداکردن اطلاعات کشورها: 
این کد با استفاده از کتابخانه countryinfo اطلاعات جامعی درباره یک کشور ارائه می‌دهد. ابتدا نام کشور را از کاربر دریافت می‌کند و سپس اطلاعات مختلف از جمله پایتخت، جمعیت، مساحت، منطقه جغرافیایی، زبان‌ها، واحد پول و کشورهای همسایه را از کتابخانه بازیابی کرده و به صورت چاپ شده نمایش می‌دهد.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/Tools/CountryInfoFinder/CountryInfoFinder_English.md)</b> و <b>[Persian README.md](SmallProjects/Tools/CountryInfoFinder/CountryInfoFinder_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/Tools/CountryInfoFinder/CountryInfoFinder_Persian.py)</b>.
### 3. وظیفه روزانه: 
این برنامه یک مدیریت‌کننده وظایف ساده است که وظایف را در یک فایل JSON ذخیره می‌کند و امکان افزودن وظایف جدید شامل نام، تاریخ سررسید و وضعیت تکمیل را فراهم می‌کند. کاربر می‌تواند تمامی وظایف را مشاهده کرده، وضعیت تکمیل آن‌ها را تغییر دهد و در صورت نیاز وظایف را حذف کند. تغییرات اعمال‌شده به صورت خودکار در فایل ذخیره می‌شوند و برنامه از طریق یک منوی اصلی مدیریت می‌شود که گزینه‌های مختلفی را برای عملیات روی وظایف ارائه می‌دهد.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/Tools/DailyTasker/DailyTasker_English.md)</b> و <b>[Persian README.md](SmallProjects/Tools/DailyTasker/DailyTasker_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/Tools/DailyTasker/DailyTasker_Persian.py)</b>.
### 4. جعل داده ها: 
این کد با استفاده از کتابخانه Faker داده‌های ساختگی مختلفی مانند نام، آدرس، متن، ایمیل، کشور، مختصات جغرافیایی و URL تولید و چاپ می‌کند. این ابزار برای تست و شبیه‌سازی در پروژه‌های نرم‌افزاری مفید است.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/Tools/DataFaker/DataFaker_English.md)</b> و <b>[Persian README.md](SmallProjects/Tools/DataFaker/DataFaker_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/Tools/DataFaker/DataFaker_Persian.py)</b>.
### 5. یادداشت ساده: 
این برنامه یک اپلیکیشن یادداشت‌برداری ساده است که از فایل notes.txt برای ذخیره و مدیریت یادداشت‌ها استفاده می‌کند. کاربر می‌تواند یادداشت جدید اضافه کند، یادداشت‌های موجود را مشاهده کند یا یک یادداشت را حذف کند. یادداشت‌ها در یک حلقه منو تعاملی مدیریت می‌شوند و تغییرات در فایل ذخیره می‌شوند. اگر فایل یادداشت وجود نداشته باشد، برنامه آن را ایجاد می‌کند. گزینه‌های موجود شامل اضافه کردن، مشاهده، حذف و خروج از برنامه هستند. <br>
برای مشاهده فایل <b>[English README.md](SmallProjects/Tools/EasyPad/EasyPad_English.md)</b> و <b>[Persian README.md](SmallProjects/Tools/EasyPad/EasyPad_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/Tools/EasyPad/EasyPad_Persian.py)</b>.
### 6. ردیاب سیاره: 
این کد موقعیت یک سیاره را نسبت به مکان رصدخانه گرینویچ در زمان فعلی با استفاده از ماژول‌های Astropy محاسبه و نمایش می‌دهد با دریافت نام سیاره از کاربر، موقعیت سیاره به صورت صعود مستقیم (RA) و میل (Dec) ارائه می‌شود.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/Tools/PlanetTracker/PlanetTracker_English.md)</b> و <b>[Persian README.md](SmallProjects/Tools/PlanetTracker/PlanetTracker_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/Tools/PlanetTracker/PlanetTracker_Persian.py)</b>.
### 7. ساخت QR Code: 
این کد یک برنامه ساده به زبان پایتون برای تولید کد QR از یک آدرس وب است. ابتدا از کاربر خواسته می‌شود که آدرس وبسایت (بدون پیشوند http یا https) را وارد کند. سپس، کد به‌طور خودکار پیشوند https:// را به آدرس اضافه می‌کند تا یک URL معتبر ایجاد شود. با استفاده از ماژول qrcode، کد QR مربوط به این آدرس تولید شده و به کاربر نمایش داده می‌شود. همچنین، این کد QR به صورت یک فایل تصویری با فرمت PNG در همان دایرکتوری ذخیره می‌شود و در پایان یک پیام موفقیت به کاربر نمایش داده می‌شود.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/Tools/QRcode/QRcode_English.md)</b> و <b>[Persian README.md](SmallProjects/Tools/QRcode/QRcode_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/Tools/QRcode/QRcode_Persian.md)</b>.
### 8. زمان اجرای کد: 
این کد زمان اجرای یک بخش از کد را با استفاده از ماژول time اندازه‌گیری می‌کند. زمان شروع و پایان ثبت شده و مدت زمان اجرای کد محاسبه و نمایش داده می‌شود.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/Tools/TimeCode/TimeCode_English.md)</b> و <b>[Persian README.md](SmallProjects/Tools/TimeCode/TimeCode_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/Tools/TimeCode/TimeCode_Persian.py)</b>.
### 9. زمان سنج: 
تابع countdown_timer یک شمارش معکوس از ثانیه‌هایی که وارد می‌شود ایجاد می‌کند و در هر ثانیه زمان باقی‌مانده را به فرمت MM:SS نمایش می‌دهد. پس از اتمام زمان، پیغام "Time's up!" را نشان می‌دهد.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/Tools/Timer/Timer_English.md)</b> و <b>[Persian README.md](SmallProjects/Tools/Timer/Timer_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/Tools/Timer/Timer_Persian.py)</b>.
### 10. ساخت پسورد امن:
این برنامه یک رمز عبور قوی و تصادفی با طول مشخص تولید می‌کند. رمز عبور از حروف بزرگ و کوچک، اعداد و کاراکترهای خاص تشکیل شده است. از ماژول secrets برای اطمینان از تولید رمزهای تصادفی با امنیت بالا استفاده شده است.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/Tools/safe_pass_generator/Safe_Pass_English.md)</b> و <b>[Persian README.md](SmallProjects/Tools/safe_pass_generator/Safe_Pass_Persian.md)</b> و کد کامل <b>[Python Code](SmallProjects/Tools/safe_pass_generator/Safe_Pass_Persian.py)</b>.
### 11. صفحه کلید:
این کد ورودی کاربر را دریافت کرده و زبان آن (انگلیسی یا فارسی) را تشخیص می‌دهد. سپس با استفاده از یک دیکشنری نگاشت، حروف متن را به زبان صحیح تبدیل می‌کند. متن اصلاح‌شده نمایش داده شده و به کلیپ‌بورد کپی می‌شود. از Counter برای شمارش حروف و re.sub برای جایگزینی کاراکترها استفاده شده است. این ابزار برای تصحیح متون اشتباه تایپ‌شده در کیبوردهای انگلیسی و فارسی مفید است.<br>
برای مشاهده فایل <b>[English README.md](SmallProjects/Tools/KeyboardFixer/KeyboardFixerEnglish.md)</b> و <b>[Persian README.md](SmallProjects/Tools/KeyboardFixer/KeyboardFixerPersian.md)</b> و کد کامل <b>[Python Code](SmallProjects/Tools/KeyboardFixer/KeyboardFixerPersian.py)</b>.
    
<hr>
