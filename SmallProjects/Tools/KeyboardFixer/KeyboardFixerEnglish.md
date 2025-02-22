## Fixing Mistyped Text in the Wrong Language
This code is designed to correct text that has been mistyped in the wrong keyboard language. Many users accidentally type Persian text while their keyboard is set to English (or vice versa), resulting in unreadable text. The script detects the language of the input text and converts it into the correct form using a predefined mapping. Finally, it displays the corrected text and copies it to the clipboard for ease of use.
## 1. Defining Character Mappings (English to Persian & Persian to English)
At the beginning of the script, two dictionaries are created to map characters between English and Persian:
- eng_to_fa: Maps English characters to their Persian equivalents. For example, if a user intends to type "سلام" but the keyboard is set to English, the input will be sghl. This dictionary corrects such mistakes by converting sghl to "سلام".
- fa_to_eng: Performs the reverse conversion, turning mistakenly typed Persian text into English.
- Additionally, uppercase English characters are mapped as well to ensure that text with capital letters is properly converted.
## 2. Detecting the Language of the Text
