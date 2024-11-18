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
