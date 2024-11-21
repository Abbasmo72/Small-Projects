## عملکرد و نوع اجرای پروژه ساخت PDF
این پروژه یک برنامه گرافیکی با استفاده از کتابخانه Tkinter است که به کاربر این امکان را می‌دهد تا متنی را وارد کرده و آن را به یک فایل PDF تبدیل کند. در این برنامه، مراحل زیر به ترتیب انجام می‌شود:
1. طراحی رابط کاربری: از Tkinter برای طراحی یک پنجره با عنوان "PDF Generator" استفاده می‌شود. در این پنجره یک جعبه متنی (Text Box) برای وارد کردن متن و یک دکمه برای ایجاد فایل PDF قرار داده شده است.
2. ورود متن: کاربر می‌تواند متنی را وارد کند که ممکن است شامل چندین خط باشد. این متن پس از وارد کردن با فشار دادن دکمه "Create PDF" به فرمت PDF تبدیل می‌شود.
3. تبدیل به PDF: پس از دریافت متن، از کتابخانه ReportLab برای ساخت فایل PDF استفاده می‌شود. این کتابخانه اجازه می‌دهد که متن در یک فایل PDF به صورت گرافیکی نوشته شود.
4. تنظیمات PDF: در ابتدا فونت فارسی 'B Nazanin' ثبت و به عنوان فونت پیش‌فرض برای نوشتن متن در فایل PDF انتخاب می‌شود. پس از آن، متن ورودی به صورت خط به خط در فایل PDF قرار می‌گیرد. اگر متن در انتهای صفحه تمام شود، صفحه جدیدی ایجاد می‌شود تا متن به درستی ادامه یابد.
5. ذخیره PDF: در نهایت، متن تبدیل شده به PDF در یک فایل با نام "output.pdf" ذخیره می‌شود.

در مجموع، این برنامه به کاربر این امکان را می‌دهد که متنی که وارد می‌کند را به راحتی به یک فایل PDF تبدیل کند و در قالب یک فایل قابل چاپ و با فونت فارسی ذخیره نماید.

## کد پایتون
```python
from tkinter import Tk, Text, Button, END
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def save_pdf(text):
    # تنظیمات PDF و فونت فارسی
    c = canvas.Canvas("output.pdf", pagesize=A4)
    width, height = A4
    
    # ثبت فونت فارسی
    pdfmetrics.registerFont(TTFont('Persian', 'B Nazanin.ttf'))
    
    # تنظیم مکان اولیه نوشتن
    y_position = height - 40
    lines = text.split('\n')

    for line in lines:
        if y_position < 40:  # اگر به پایین صفحه رسیدیم، صفحه جدیدی باز کن
            c.showPage()
            y_position = height - 40
        c.setFont("Persian", 12)  # تنظیم فونت و اندازه 12
        c.drawString(40, y_position, line)
        y_position -= 20

    c.save()

def get_text():
    # دریافت متن از باکس متنی
    user_text = text_box.get("1.0", END)
    save_pdf(user_text)

# تنظیمات رابط کاربری
root = Tk()
root.title("PDF Generator")
root.geometry("400x400")

# باکس متنی برای دریافت ورودی
text_box = Text(root, wrap='word', font=("Arial", 12))
text_box.pack(expand=True, fill='both')

# دکمه برای ایجاد PDF
save_button = Button(root, text="Create PDF", command=get_text)
save_button.pack()

root.mainloop()

```
