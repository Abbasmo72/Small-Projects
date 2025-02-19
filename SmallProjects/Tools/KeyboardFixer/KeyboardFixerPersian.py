import re
import string
import pyperclip
from collections import Counter

# نگاشت کیبورد انگلیسی به فارسی
eng_to_fa = {
    "q": "ض", "w": "ص", "e": "ث", "r": "ق", "t": "ف", "y": "غ", "u": "ع", "i": "ه", "o": "خ", "p": "ح",
    "[": "ج", "]": "چ", "a": "ش", "s": "س", "d": "ی", "f": "ب", "g": "ل", "h": "ا", "j": "ت",
    "k": "ن", "l": "م", ";": "ک", "'": "گ", "z": "ظ", "x": "ط", "c": "ز", "v": "ر", "b": "ذ",
    "n": "د", "m": "پ", ",": "و", "x": "ژ", "?": "/", "~": "÷", "@": "٬", "#": "٫", "$": "﷼",
    "%": "٪", "^": "×", "&": "،", "*": "÷", "_": "ـ", "=": "+", "{": "»", "}": "«", "<": "‹", ">": "›",
    "|": "¦", "0": "۰", "1": "۱", "2": "۲", "3": "۳", "4": "۴", "5": "۵", "6": "۶", "7": "۷", "8": "۸", "9": "۹"
}

# ایجاد نگاشت برای حروف بزرگ
eng_to_fa_upper = {k.upper(): v for k, v in eng_to_fa.items()}
eng_to_fa.update(eng_to_fa_upper)

# ایجاد نگاشت فارسی به انگلیسی
fa_to_eng = {v: k for k, v in eng_to_fa.items()}

# تابع تشخیص زبان
def detect_language(text):
    counter = Counter(text)
    eng_count = sum(counter[ch] for ch in string.ascii_letters)
    fa_count = sum(counter[ch] for ch in fa_to_eng)
    return "eng" if eng_count > fa_count else "fa"

# تبدیل متن بر اساس زبان تشخیص داده شده
def fix_keyboard_language(text):
    if not text:
        return ""
    
    lang = detect_language(text)
    mapping = eng_to_fa if lang == "eng" else fa_to_eng
    
    def translate_match(match):
        return mapping.get(match.group(0), match.group(0))
    
    return re.sub(r".", translate_match, text)

if __name__ == "__main__":
    user_input = input("متن خود را وارد کنید: ")
    corrected_text = fix_keyboard_language(user_input)
    print("متن تصحیح‌شده:", corrected_text)
    pyperclip.copy(corrected_text)
    print("(متن به کلیپ‌بورد کپی شد)")
