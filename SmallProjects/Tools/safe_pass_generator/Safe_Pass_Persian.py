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
