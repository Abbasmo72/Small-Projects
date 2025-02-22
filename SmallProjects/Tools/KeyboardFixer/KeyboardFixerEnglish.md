## Fixing Mistyped Text in the Wrong Language
This code is designed to correct text that has been mistyped in the wrong keyboard language. Many users accidentally type Persian text while their keyboard is set to English (or vice versa), resulting in unreadable text. The script detects the language of the input text and converts it into the correct form using a predefined mapping. Finally, it displays the corrected text and copies it to the clipboard for ease of use.
## 1. Defining Character Mappings (English to Persian & Persian to English)
At the beginning of the script, two dictionaries are created to map characters between English and Persian:
- eng_to_fa: Maps English characters to their Persian equivalents. For example, if a user intends to type "سلام" but the keyboard is set to English, the input will be sghl. This dictionary corrects such mistakes by converting sghl to "سلام".
- fa_to_eng: Performs the reverse conversion, turning mistakenly typed Persian text into English.
- Additionally, uppercase English characters are mapped as well to ensure that text with capital letters is properly converted.
## 2. Detecting the Language of the Text
The function detect_language(text) determines whether the input text is in English or Persian based on character frequency.
- If the text contains more English letters, it is classified as English.
- If Persian letters are more frequent, the text is considered Persian.
### How it Works:
- A Counter object counts occurrences of each character in the text.
- It then iterates through the characters to count English letters (using string.ascii_letters) and Persian letters (using the keys from fa_to_eng).
- Finally, it returns "eng" if English characters are dominant; otherwise, it returns "fa".
## 3. Converting the Text to the Correct Language
The fix_keyboard_language(text) function performs the conversion after detecting the language of the text.

<b>Conversion Process:</b>
1. The language is detected using detect_language(text).
2. Based on the detected language, the appropriate mapping (eng_to_fa or fa_to_eng) is selected.
3. A helper function translate_match(match) is defined, which replaces each character with its correct equivalent from the mapping dictionary.
4. The entire text is processed using re.sub(r".", translate_match, text), ensuring that every character is replaced accordingly.
## 4. Taking User Input and Correcting It
In the if __name__ == "__main__": block, the following steps are executed:
1. The script prompts the user to enter text.
2. It processes the input using fix_keyboard_language(user_input).
3. The corrected text is printed.
4. The corrected text is copied to the clipboard using pyperclip.copy(corrected_text), allowing easy pasting.
5. A message is displayed to inform the user that the text has been copied.
### Conclusion
This script is a practical tool for correcting text mistakenly typed in the wrong keyboard language. By detecting the text’s language and replacing characters accordingly, it ensures readability. The feature of copying the corrected text to the clipboard further enhances its usability, making it an efficient solution for this common typing issue.
# Python Code
```python
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
```
