from countryinfo import CountryInfo

# دریافت نام کشور از کاربر
country = CountryInfo(input("Enter Country Name:"))

# نمایش اطلاعات مختلف درباره کشور
print("نام کشور:", country.name())  # نمایش نام کشور
print("پایتخت:", country.capital())  # نمایش پایتخت کشور
print("جمعیت:", country.population())  # نمایش جمعیت کشور
print("مساحت (به کیلومتر مربع):", country.area())  # نمایش مساحت کشور به کیلومتر مربع
print("منطقه:", country.region())  # نمایش منطقه‌ای که کشور در آن واقع شده است
print("زیرمنطقه:", country.subregion())  # نمایش زیرمنطقه‌ای که کشور در آن واقع شده است
print("نام مردم:", country.demonym())  # نمایش نام مردم کشور
print("ارزها:", country.currencies())  # نمایش ارزهای مورد استفاده در کشور
print("زبان‌ها:", country.languages())  # نمایش زبان‌های صحبت شده در کشور
print("مرزها:", country.borders())  # نمایش کشورهایی که با این کشور مرز دارند
