import pandas as pd
import os

def combine_csv_files(input_folder, output_file):
    # بررسی وجود پوشه
    if not os.path.exists(input_folder):
        print(f"مسیر پوشه '{input_folder}' یافت نشد.")
        return

    # لیست کردن فایل‌های CSV
    csv_files = [file for file in os.listdir(input_folder) if file.endswith('.csv')]
    if not csv_files:
        print("هیچ فایل CSV در مسیر مشخص شده یافت نشد.")
        return

    # ترکیب فایل‌های CSV
    combined_data = pd.DataFrame()
    for file in csv_files:
        file_path = os.path.join(input_folder, file)
        try:
            print(f"در حال خواندن فایل: {file}")
            data = pd.read_csv(file_path)
            combined_data = pd.concat([combined_data, data], ignore_index=True)
        except Exception as e:
            print(f"خطا در خواندن فایل '{file}': {e}")

    # ذخیره داده‌های ترکیب‌شده
    try:
        combined_data.to_csv(output_file, index=False)
        print(f"فایل ترکیبی با نام '{output_file}' ذخیره شد.")
    except Exception as e:
        print(f"خطا در ذخیره فایل خروجی: {e}")

# تنظیم مسیر پوشه و فایل خروجی
input_folder_path = "مسیر_پوشه_حاوی_CSV_ها"
output_file_path = "combined_output.csv"

# اجرای تابع
combine_csv_files(input_folder_path, output_file_path)
