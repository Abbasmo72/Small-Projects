from faker import Faker

fake = Faker()  # ایجاد یک نمونه از کلاس Faker

# ایجاد و چاپ یک نام تصادفی
print(fake.name()) 

# ایجاد و چاپ یک آدرس تصادفی
print(fake.address()) 

# ایجاد و چاپ یک متن تصادفی (پاراگراف)
print(fake.text()) 

# ایجاد و چاپ یک آدرس ایمیل تصادفی
print(fake.email()) 

# ایجاد و چاپ یک نام کشور تصادفی
print(fake.country()) 

# ایجاد و چاپ مختصات جغرافیایی تصادفی (عرض جغرافیایی و طول جغرافیایی)
print(fake.latitude(), fake.longitude()) 

# ایجاد و چاپ یک URL تصادفی
print(fake.url()) 
