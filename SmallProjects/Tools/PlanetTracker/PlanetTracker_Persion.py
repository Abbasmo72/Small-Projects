from astropy.coordinates import get_body, EarthLocation  # وارد کردن ماژول‌های مورد نیاز برای تعیین موقعیت سیارات
from astropy.time import Time  # وارد کردن ماژول زمان برای دریافت زمان کنونی

now = Time.now()  # دریافت زمان کنونی

# دریافت موقعیت زمین از سایت گرینویچ
location = EarthLocation.of_site('greenwich')

# دریافت نام سیاره از کاربر و تبدیل به حروف کوچک
planet_name = input("Enter the name of the planet: ").lower()

# دریافت موقعیت سیاره در زمان کنونی نسبت به مکان زمین (سایت گرینویچ)
planet_position = get_body(planet_name, now, location)

# نمایش موقعیت سیاره شامل مقدار را (RA) و دک (Dec)
print(f"{planet_name.capitalize()} "  # نمایش نام سیاره با اولین حرف بزرگ
      f"Position: RA = {planet_position.ra}, "  # نمایش مقدار را (Right Ascension)
      f"Dec = {planet_position.dec}")  # نمایش مقدار دک (Declination)
