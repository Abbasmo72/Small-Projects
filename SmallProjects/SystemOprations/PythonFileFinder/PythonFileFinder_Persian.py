import os
import tkinter as tk
from tkinter import messagebox

def search_files(directory, file_extension):
    # جستجو در دایرکتوری و زیرشاخه‌ها برای فایل‌های با پسوند خاص
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extension):
                result.append(os.path.join(root, file))
    return result

def on_search_button_click():
    search_term = entry.get()
    if not search_term:
        messagebox.showwarning("ورودی خالی", "لطفاً یک نام فایل وارد کنید")
        return
    results = search_files("/", ".py")  # جستجو در کل سیستم برای فایل‌های .py
    found_files = [file for file in results if search_term in file]
    
    if found_files:
        result_list.delete(0, tk.END)
        for file in found_files:
            result_list.insert(tk.END, file)
    else:
        messagebox.showinfo("نتیجه", "هیچ فایلی یافت نشد.")

# ایجاد پنجره Tkinter
root = tk.Tk()
root.title("جستجوی فایل‌های Python")

# طراحی بخش ورودی
label = tk.Label(root, text="نام فایل را وارد کنید:")
label.pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

search_button = tk.Button(root, text="جستجو", command=on_search_button_click)
search_button.pack(pady=5)

# طراحی بخش نمایش نتایج
result_list = tk.Listbox(root, width=80, height=20)
result_list.pack(pady=5)

root.mainloop()
