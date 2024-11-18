import qrcode  # وارد کردن ماژول qrcode برای تولید کدهای QR

# دریافت آدرس وب‌سایت از کاربر
website = input("Enter the website URL without http or https: ")

# اضافه کردن https:// به ابتدای آدرس وب‌سایت برای ساخت URL معتبر
full_url = f"https://{website}"

# تولید کد QR برای آدرس وب‌سایت وارد شده
qr = qrcode.make(full_url)

# نمایش کد QR تولید شده
qr.show()

# ذخیره کردن کد QR به صورت یک فایل تصویری (فرمت PNG)
qr.save("qrcode.png")
print("QR Code has been successfully saved.")  # نمایش پیامی مبنی بر اینکه کد QR با موفقیت ذخیره شده است
