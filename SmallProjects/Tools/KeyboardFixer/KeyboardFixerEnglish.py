import re
import string
import pyperclip
from collections import Counter

# Mapping from English keyboard characters to Persian
eng_to_fa = {
    "q": "ض", "w": "ص", "e": "ث", "r": "ق", "t": "ف", "y": "غ", "u": "ع", "i": "ه", "o": "خ", "p": "ح",
    "[": "ج", "]": "چ", "a": "ش", "s": "س", "d": "ی", "f": "ب", "g": "ل", "h": "ا", "j": "ت",
    "k": "ن", "l": "م", ";": "ک", "'": "گ", "z": "ظ", "x": "ط", "c": "ز", "v": "ر", "b": "ذ",
    "n": "د", "m": "پ", ",": "و", "x": "ژ", "?": "/", "~": "÷", "@": "٬", "#": "٫", "$": "﷼",
    "%": "٪", "^": "×", "&": "،", "*": "÷", "_": "ـ", "=": "+", "{": "»", "}": "«", "<": "‹", ">": "›",
    "|": "¦", "0": "۰", "1": "۱", "2": "۲", "3": "۳", "4": "۴", "5": "۵", "6": "۶", "7": "۷", "8": "۸", "9": "۹"
}

# Create a mapping for uppercase characters as well
eng_to_fa_upper = {k.upper(): v for k, v in eng_to_fa.items()}
eng_to_fa.update(eng_to_fa_upper)

# Create a reverse mapping from Persian to English
fa_to_eng = {v: k for k, v in eng_to_fa.items()}

# Function to detect the language of the text (English or Persian)
def detect_language(text):
    counter = Counter(text)
    eng_count = sum(counter[ch] for ch in string.ascii_letters)  # Count English characters
    fa_count = sum(counter[ch] for ch in fa_to_eng)  # Count Persian characters
    return "eng" if eng_count > fa_count else "fa"  # Return "eng" if more English characters, else "fa"

# Function to fix the keyboard language based on detected language
def fix_keyboard_language(text):
    if not text:
        return ""
    
    lang = detect_language(text)  # Detect language (English or Persian)
    mapping = eng_to_fa if lang == "eng" else fa_to_eng  # Choose the appropriate mapping based on the language
    
    def translate_match(match):
        return mapping.get(match.group(0), match.group(0))  # Replace each character with its mapped equivalent
    
    return re.sub(r".", translate_match, text)  # Apply the translation to each character in the text

if __name__ == "__main__":
    user_input = input("Enter your text: ")  # Prompt the user to enter text
    corrected_text = fix_keyboard_language(user_input)  # Correct the keyboard input based on the detected language
    print("Corrected text:", corrected_text)  # Print the corrected text
    pyperclip.copy(corrected_text)  # Copy the corrected text to the clipboard
    print("(The text has been copied to the clipboard)")  # Inform the user that the text has been copied
