# ساخت پسورد امن
این کد یک تابع می‌سازد که رمز عبور تصادفی و قوی تولید می‌کند.

از ابزارهایی استفاده می‌کند که امکان انتخاب تصادفی حروف، اعداد و نمادها را فراهم می‌کنند.
بررسی می‌کند که طول رمز عبور کمتر از ۸ نباشد.
با ترکیب حروف بزرگ، کوچک، اعداد و نمادها، رمز عبور را تولید می‌کند.
در نهایت رمز تولید شده را برمی‌گرداند و چاپ می‌کند.

# کد پایتون
```python
import secrets
import string

def generate_strong_password(length=12):
    """تولید رمز عبور تصادفی قوی با طول مشخص."""
    if length < 8:
        raise ValueError("طول رمز عبور باید حداقل 8 کاراکتر باشد.")

    # مجموعه کاراکترها: حروف بزرگ، حروف کوچک، اعداد و کاراکترهای خاص
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # تولید رمز تصادفی
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

# تست تابع
password = generate_strong_password(16)
print("رمز عبور تصادفی تولید شده:", password)

```
