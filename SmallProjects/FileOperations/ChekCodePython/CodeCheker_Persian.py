import tkinter as tk
from tkinter import messagebox
import ast

def check_syntax():
    code = code_text.get("1.0", tk.END)
    try:
        # بررسی صحت سینتکس کد پایتون با استفاده از ast
        ast.parse(code)
        messagebox.showinfo("Result", "کد شما صحیح است و هیچ خطای سینتکسی ندارد.")
    except SyntaxError as e:
        messagebox.showerror("Syntax Error", f"خطا در خط {e.lineno}: {e.msg}")

def update_line_numbers(event=None):
    # پاک کردن شماره خطوط در باکس مربوطه
    line_numbers_text.delete("1.0", tk.END)
    # گرفتن تعداد خطوط در باکس متنی کد
    line_count = code_text.index('end').split('.')[0]
    # وارد کردن شماره خطوط برای هر خط
    line_numbers_text.insert(tk.END, "\n".join(str(i) for i in range(1, int(line_count))))

# ایجاد پنجره اصلی برنامه
root = tk.Tk()
root.title("بررسی سینتکس کد پایتون همراه با شماره خطوط")

# ایجاد یک فریم برای نمایش شماره خطوط و کد کنار هم
frame = tk.Frame(root)
frame.pack(pady=10)

# باکس متنی برای شماره خطوط (غیرقابل ویرایش)
line_numbers_text = tk.Text(frame, width=4, height=15, padx=3, takefocus=0, border=0, background="lightgrey", state='disabled')
line_numbers_text.pack(side=tk.LEFT, fill=tk.Y)

# باکس متنی برای ورودی کد
code_text = tk.Text(frame, height=15, width=60)
code_text.insert(tk.END, "# نمونه کد پایتون\nprint('Hello, World!')\n")  # کد پیش‌فرض
code_text.pack(side=tk.LEFT, fill=tk.BOTH)

# اتصال رویدادها برای به‌روزرسانی شماره خطوط هنگام هر تغییر در متن
code_text.bind("<KeyRelease>", update_line_numbers)
update_line_numbers()  # فراخوانی اولیه برای پر کردن شماره خطوط

# دکمه برای بررسی کد
check_button = tk.Button(root, text="بررسی سینتکس", command=check_syntax)
check_button.pack(pady=5)

root.mainloop()
