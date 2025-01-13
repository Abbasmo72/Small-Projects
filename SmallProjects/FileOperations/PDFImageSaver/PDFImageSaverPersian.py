import os
from tkinter import Tk, filedialog
from PyPDF2 import PdfReader
from PIL import Image
import io

def extract_images_from_pdf(pdf_path, output_folder):
    """
    استخراج تصاویر از یک فایل PDF و ذخیره آن‌ها در پوشه‌ای مشخص
    """
    # اگر پوشه خروجی وجود ندارد، آن را ایجاد کن
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # باز کردن فایل PDF
    pdf_reader = PdfReader(pdf_path)
    image_count = 0  # شمارش تعداد تصاویر استخراج‌شده

    # پیمایش صفحات PDF
    for page_number, page in enumerate(pdf_reader.pages):
        # بررسی وجود منابع تصویری در صفحه
        if '/XObject' in page['/Resources']:
            x_objects = page['/Resources']['/XObject'].get_object()
            for obj_name in x_objects:
                x_object = x_objects[obj_name]
                # بررسی اینکه آیا شیء فعلی تصویر است یا خیر
                if x_object['/Subtype'] == '/Image':
                    try:
                        # استخراج داده‌های تصویر
                        data = x_object.get_data()  # داده‌های باینری تصویر
                        mode = 'RGB' if x_object['/ColorSpace'] == '/DeviceRGB' else 'P'  # مشخص کردن مود رنگ
                        
                        # تبدیل داده‌های تصویر به یک تصویر واقعی
                        img = Image.open(io.BytesIO(data))
                        img = img.convert(mode)  # اطمینان از صحت مود تصویر

                        # ایجاد نام فایل و ذخیره تصویر
                        image_count += 1
                        img_path = os.path.join(output_folder, f"image_{page_number + 1}_{image_count}.png")
                        img.save(img_path)
                        print(f"ذخیره شد: {img_path}")
                    except Exception as e:
                        # اگر خطایی رخ دهد، آن را چاپ کن و ادامه بده
                        print(f"خطا در پردازش تصویر صفحه {page_number + 1}: {e}")

    # نمایش پیام نهایی
    if image_count > 0:
        print(f"استخراج کامل شد! {image_count} تصویر در پوشه '{output_folder}' ذخیره شد.")
    else:
        print("هیچ تصویری در فایل PDF پیدا نشد.")

def select_pdf_and_extract_images():
    """
    باز کردن پنجره انتخاب فایل و استخراج تصاویر از فایل PDF انتخاب‌شده
    """
    # پنهان کردن پنجره اصلی Tkinter
    Tk().withdraw()

    # باز کردن دیالوگ انتخاب فایل
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not pdf_path:
        print("هیچ فایلی انتخاب نشد.")
        return

    # تعیین پوشه خروجی برای ذخیره تصاویر
    output_folder = os.path.join(os.path.dirname(pdf_path), "extracted_images")

    # استخراج تصاویر از فایل PDF
    extract_images_from_pdf(pdf_path, output_folder)

if __name__ == "__main__":
    # اجرای اصلی برنامه
    select_pdf_and_extract_images()
