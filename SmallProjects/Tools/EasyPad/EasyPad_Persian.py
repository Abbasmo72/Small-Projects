import os

# مسیر فایل برای ذخیره یادداشت‌ها
NOTES_FILE = "notes.txt"  # نام فایل برای ذخیره یادداشت‌ها

# تابع برای خواندن یادداشت‌ها از فایل
def read_notes():
    if not os.path.exists(NOTES_FILE):  # اگر فایل وجود نداشته باشد، یک لیست خالی برمی‌گرداند
        return []
    
    with open(NOTES_FILE, "r") as file:  # باز کردن فایل برای خواندن
        notes = file.readlines()  # خواندن تمام خطوط فایل
    return [note.strip() for note in notes]  # حذف فواصل اضافی و برگرداندن یادداشت‌ها

# تابع برای اضافه کردن یادداشت جدید
def add_note(note):
    with open(NOTES_FILE, "a") as file:  # باز کردن فایل برای افزودن یادداشت جدید
        file.write(note + "\n")  # نوشتن یادداشت به فایل
    print("Note added successfully.")  # پیام موفقیت در اضافه کردن یادداشت

# تابع برای نمایش تمام یادداشت‌ها
def display_notes():
    notes = read_notes()  # خواندن یادداشت‌ها
    if not notes:  # اگر هیچ یادداشتی وجود نداشته باشد
        print("No notes available.")  # پیام عدم وجود یادداشت
    else:
        print("\nYour Notes:")  # چاپ عنوان یادداشت‌ها
        for i, note in enumerate(notes, 1):  # شمارش و نمایش هر یادداشت
            print(f"{i}. {note}")

# تابع برای حذف یادداشت
def delete_note(index):
    notes = read_notes()  # خواندن یادداشت‌ها
    if index < 1 or index > len(notes):  # بررسی معتبر بودن شماره یادداشت
        print("Invalid note number.")  # پیام خطا در صورت شماره اشتباه
        return

    del notes[index - 1]  # حذف یادداشت مورد نظر
    with open(NOTES_FILE, "w") as file:  # باز کردن فایل برای نوشتن مجدد لیست یادداشت‌ها
        for note in notes:  # نوشتن باقی‌مانده یادداشت‌ها به فایل
            file.write(note + "\n")
    print("Note deleted successfully.")  # پیام موفقیت در حذف یادداشت

# منوی اصلی برنامه
def main():
    while True:
        print("\nSimple Note Taking App")  # نمایش عنوان برنامه
        print("1. Add Note")  # گزینه افزودن یادداشت
        print("2. View Notes")  # گزینه نمایش یادداشت‌ها
        print("3. Delete Note")  # گزینه حذف یادداشت
        print("4. Exit")  # گزینه خروج از برنامه

        choice = input("Choose an option: ")  # گرفتن ورودی از کاربر برای انتخاب گزینه

        if choice == '1':  # در صورت انتخاب گزینه 1
            note = input("Enter your note: ")  # گرفتن یادداشت جدید از کاربر
            add_note(note)  # افزودن یادداشت به فایل
        elif choice == '2':  # در صورت انتخاب گزینه 2
            display_notes()  # نمایش تمام یادداشت‌ها
        elif choice == '3':  # در صورت انتخاب گزینه 3
            display_notes()  # نمایش یادداشت‌ها
            try:
                index = int(input("Enter the note number to delete: "))  # گرفتن شماره یادداشت برای حذف
                delete_note(index)  # حذف یادداشت با شماره مشخص
            except ValueError:  # در صورت وارد کردن شماره نامعتبر
                print("Please enter a valid number.")  # پیام خطا
        elif choice == '4':  # در صورت انتخاب گزینه 4
            print("Exiting the program.")  # پیام خروج از برنامه
            break
        else:  # در صورت وارد کردن گزینه اشتباه
            print("Invalid option. Please try again.")  # پیام خطا برای گزینه اشتباه

if __name__ == "__main__":  # اطمینان از اینکه کد تنها در صورت اجرا شدن به عنوان اسکریپت اجرا شود
    main()
