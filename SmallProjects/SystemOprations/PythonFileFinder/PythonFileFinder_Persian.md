## ابزار جستجوی فایل‌های پایتون با رابط گرافیکی
## تحلیل کد
برنامه بالا ابزاری گرافیکی برای جستجوی فایل‌های پایتون با پسوند py. در سیستم‌عامل است. این برنامه از کتابخانه Tkinter برای ایجاد رابط کاربری استفاده می‌کند و به کاربر اجازه می‌دهد با وارد کردن بخشی از نام فایل، نتایج جستجو را مشاهده کند. عملکرد بخش‌های مختلف کد به شرح زیر است:
## 1. وارد کردن کتابخانه‌ها
کتابخانه os برای پیمایش دایرکتوری‌ها و زیرشاخه‌ها استفاده می‌شود. کتابخانه Tkinter و بخش messagebox وظیفه ساخت رابط گرافیکی و نمایش پیام‌ها را برعهده دارند.

## 2. تابع جستجوی فایل‌ها
یک تابع برای جستجوی فایل‌هایی با پسوند مشخص در دایرکتوری و زیرشاخه‌های آن تعریف شده است. در این تابع:
  - پیمایش دایرکتوری‌ها و فایل‌ها با کمک حلقه os.walk انجام می‌شود.
  - هر فایلی که پسوند مورد نظر را داشته باشد، به فهرست نتایج اضافه می‌شود.
  - در نهایت، فهرست کامل فایل‌های پیدا شده بازگردانده می‌شود.

## 3. تابع مربوط به کلیک دکمه جستجو
این تابع هنگام کلیک دکمه "جستجو" فعال می‌شود. روند عملکرد آن شامل موارد زیر است:
1. مقدار ورودی کاربر (نام یا بخشی از نام فایل) دریافت می‌شود.
2. در صورتی که ورودی خالی باشد، پیغام هشدار برای کاربر نمایش داده می‌شود.
3. فرآیند جستجو آغاز می‌شود:
   - تمامی فایل‌های پایتون در دایرکتوری اصلی / و زیرشاخه‌ها جستجو می‌شوند.
   - فایل‌هایی که شامل عبارت جستجو شده باشند، فیلتر و به عنوان نتیجه نهایی انتخاب می‌شوند.
4. در صورت وجود نتایج، فهرست موجود در بخش نمایش نتایج پاک شده و فایل‌های جدید اضافه می‌شوند. در غیر این صورت، پیغام "فایلی یافت نشد" نمایش داده می‌شود.

## 4. رابط کاربری برنامه
بخش‌های گرافیکی برنامه با استفاده از ابزارهای موجود در Tkinter طراحی شده‌اند:
- برچسب متنی برای نمایش راهنمای کاربر.
- کادر ورودی برای دریافت نام یا بخشی از نام فایل.
- دکمه جستجو برای آغاز فرآیند جستجو.
- فهرست نمایش نتایج برای نشان دادن مسیر فایل‌های پیدا شده.
ویجت‌های گرافیکی به ترتیب و با کمک دستور pack در پنجره اصلی جای‌گذاری می‌شوند.


## 5. اجرای برنامه
حلقه رویدادهای برنامه با استفاده از دستور mainloop آغاز می‌شود و تا زمانی که کاربر پنجره را نبندد، برنامه فعال می‌ماند.

## عملکرد کلی برنامه
این برنامه امکان جستجوی فایل‌های پایتون را در کل دایرکتوری‌های سیستم‌عامل فراهم می‌کند. کاربر می‌تواند با وارد کردن بخشی از نام فایل مورد نظر، نتایج جستجو را مشاهده کند. مسیر فایل‌های پیدا شده در یک کادر فهرست نمایش داده می‌شوند و به سادگی در دسترس کاربر قرار می‌گیرند.

نکته: استفاده از مسیر / به عنوان دایرکتوری اصلی، برنامه را برای اجرا در سیستم‌های لینوکس یا یونیکس مناسب‌تر می‌کند. در ویندوز ممکن است محدودیت‌های دسترسی یا کاهش سرعت جستجو وجود داشته باشد.

## کد پایتون

```python
import os
import tkinter as tk
from tkinter import messagebox

# Function to search for files with a specific extension in a directory and its subdirectories
def search_files(directory, file_extension):
    result = []
    for root, dirs, files in os.walk(directory):  # Walk through all directories and files
        for file in files:
            if file.endswith(file_extension):  # Check if the file has the specified extension
                result.append(os.path.join(root, file))  # Add the full file path to the result
    return result

# Function to handle the search button click event
def on_search_button_click():
    search_term = entry.get()  # Get the search term from the entry field
    if not search_term:  # If the search term is empty, show a warning message
        messagebox.showwarning("Empty Input", "Please enter a file name")
        return
    # Search for all .py files in the system
    results = search_files("/", ".py")  
    # Filter the results to include only those files that contain the search term
    found_files = [file for file in results if search_term in file]
    
    if found_files:
        result_list.delete(0, tk.END)  # Clear previous results
        for file in found_files:  # Add found files to the listbox
            result_list.insert(tk.END, file)
    else:
        messagebox.showinfo("Result", "No files found.")  # Show message if no files were found

# Create the main Tkinter window
root = tk.Tk()
root.title("Python File Search")

# Create input section
label = tk.Label(root, text="Enter file name:")
label.pack(pady=5)

entry = tk.Entry(root, width=40)  # Create input field for the search term
entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=on_search_button_click)  # Create search button
search_button.pack(pady=5)

# Create result display section
result_list = tk.Listbox(root, width=80, height=20)  # Listbox to display search results
result_list.pack(pady=5)

root.mainloop()  # Start the Tkinter event loop
```
