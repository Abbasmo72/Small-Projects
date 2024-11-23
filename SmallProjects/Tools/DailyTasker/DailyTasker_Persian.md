## مدیریت وظایف ساده با استفاده از پایتون و ذخیره‌سازی در فایل JSON
این کد یک سیستم مدیریت وظایف (Task Manager) ساده است که وظایف کاربران را ذخیره و مدیریت می‌کند. وظایف به صورت فایل JSON در سیستم ذخیره شده و با اجرای برنامه قابل دسترسی هستند. این کد شامل امکاناتی برای اضافه کردن، مشاهده، ویرایش و حذف وظایف است. عملکرد آن در چند بخش اصلی سازمان‌دهی شده است:

1. بارگذاری وظایف:
   - تابع load_tasks بررسی می‌کند که آیا فایل tasks.json وجود دارد یا خیر.
   - اگر فایل موجود باشد، داده‌ها را به عنوان یک لیست از وظایف بارگذاری می‌کند. در غیر این صورت، یک لیست خالی بازمی‌گرداند.
2. ذخیره وظایف:
   - تابع save_tasks وظایف موجود را در فایل tasks.json ذخیره می‌کند. وظایف به صورت یک لیست از اشیاء JSON ذخیره می‌شوند و داده‌ها با فرمت خوانا (با تورفتگی) در فایل ذخیره می‌شوند.
3. اضافه کردن وظیفه:
   - در add_task کاربر نام وظیفه و تاریخ انجام آن را وارد می‌کند. وظیفه جدید به صورت یک دیکشنری با سه کلید (name, due_date, completed) تعریف می‌شود.
   - وظایف جدید به لیست اضافه و در فایل ذخیره می‌شوند. همچنین پیامی به کاربر نمایش داده می‌شود که وظیفه با موفقیت اضافه شده است.
4. مشاهده وظایف:
   - تابع view_tasks وظایف موجود را با جزئیات نام، تاریخ انجام و وضعیت (تکمیل‌شده یا نشده) نمایش می‌دهد.
   - اگر هیچ وظیفه‌ای وجود نداشته باشد، پیام "وظیفه‌ای وجود ندارد" نشان داده می‌شود.
5. علامت‌گذاری به عنوان تکمیل‌شده:
   - در complete_task تمامی وظایف همراه با شماره‌هایشان نمایش داده می‌شوند. کاربر می‌تواند شماره وظیفه موردنظر را وارد کند.
   - اگر شماره واردشده معتبر باشد، وظیفه انتخاب‌شده به عنوان تکمیل‌شده علامت‌گذاری و فایل به‌روزرسانی می‌شود.
6. حذف وظیفه:
   - در delete_task کاربر می‌تواند وظیفه‌ای را برای حذف انتخاب کند. وظایف به صورت لیست نمایش داده می‌شوند و کاربر شماره وظیفه موردنظر را وارد می‌کند.
   - وظیفه انتخاب‌شده از لیست حذف و تغییرات در فایل ذخیره می‌شود.
  
  این کد یک ابزار ساده و کاربردی برای مدیریت وظایف روزانه ارائه می‌دهد. ساختار آن ماژولار است و با استفاده از ذخیره‌سازی JSON، داده‌ها بین اجرای مکرر برنامه حفظ می‌شوند. کاربران می‌توانند وظایف خود را به راحتی مدیریت کرده و وضعیت آن‌ها را بررسی کنند.

  ## کد پایتون
```python
import json
import datetime

TASKS_FILE = "tasks.json"

# بارگذاری وظایف از فایل در صورت وجود
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)  # وظایف موجود در فایل را بارگذاری می‌کند
    except FileNotFoundError:
        return []  # اگر فایل وجود نداشت، لیست خالی برمی‌گرداند

# ذخیره وظایف در فایل
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)  # وظایف را در فایل JSON ذخیره می‌کند

# افزودن یک وظیفه جدید
def add_task(tasks):
    task_name = input("Enter the task: ")  # درخواست نام وظیفه از کاربر
    due_date = input("Enter due date (YYYY-MM-DD): ")  # درخواست تاریخ موعد از کاربر
    task = {
        'name': task_name,  # نام وظیفه
        'due_date': due_date,  # تاریخ موعد
        'completed': False  # وضعیت تکمیل (پیش‌فرض: انجام نشده)
    }
    tasks.append(task)  # اضافه کردن وظیفه جدید به لیست
    save_tasks(tasks)  # ذخیره وظایف در فایل
    print(f"Task '{task_name}' added successfully!")  # پیام موفقیت‌آمیز

# مشاهده تمام وظایف
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")  # اگر هیچ وظیفه‌ای وجود نداشته باشد
        return
    
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks):
        status = "✓" if task['completed'] else "✗"  # نمایش وضعیت تکمیل وظیفه
        print(f"{idx + 1}. {task['name']} | Due: {task['due_date']} | Completed: {status}")
    print("\n")

# علامت‌گذاری یک وظیفه به عنوان انجام شده
def complete_task(tasks):
    view_tasks(tasks)  # نمایش تمام وظایف
    task_number = int(input("Enter the task number to mark as completed: "))  # درخواست شماره وظیفه از کاربر
    
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True  # تغییر وضعیت وظیفه به انجام شده
        save_tasks(tasks)  # ذخیره تغییرات
        print(f"Task '{tasks[task_number - 1]['name']}' marked as completed!")  # پیام موفقیت‌آمیز
    else:
        print("Invalid task number.")  # اگر شماره وظیفه نامعتبر باشد

# حذف یک وظیفه
def delete_task(tasks):
    view_tasks(tasks)  # نمایش تمام وظایف
    task_number = int(input("Enter the task number to delete: "))  # درخواست شماره وظیفه برای حذف

    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)  # حذف وظیفه انتخابی
        save_tasks(tasks)  # ذخیره تغییرات
        print(f"Task '{removed_task['name']}' deleted successfully!")  # پیام موفقیت‌آمیز
    else:
        print("Invalid task number.")  # اگر شماره وظیفه نامعتبر باشد

# حلقه اصلی برنامه
def main():
    tasks = load_tasks()  # بارگذاری وظایف از فایل
    while True:
        print("\nTask Manager")  # نمایش منوی مدیریت وظایف
        print("1. Add a Task")  # گزینه برای افزودن وظیفه
        print("2. View Tasks")  # گزینه برای مشاهده وظایف
        print("3. Mark Task as Completed")  # گزینه برای علامت‌گذاری وظیفه به عنوان انجام شده
        print("4. Delete Task")  # گزینه برای حذف وظیفه
        print("5. Exit")  # گزینه برای خروج از برنامه

        choice = input("Choose an option: ")  # درخواست انتخاب از کاربر
        
        if choice == "1":
            add_task(tasks)  # افزودن وظیفه جدید
        elif choice == "2":
            view_tasks(tasks)  # مشاهده وظایف
        elif choice == "3":
            complete_task(tasks)  # علامت‌گذاری وظیفه به عنوان انجام شده
        elif choice == "4":
            delete_task(tasks)  # حذف وظیفه
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")  # پیام خروج از برنامه
            break
        else:
            print("Invalid option. Please try again.")  # در صورت انتخاب گزینه نامعتبر

if __name__ == "__main__":
    main()  # اجرای تابع اصلی

```  
