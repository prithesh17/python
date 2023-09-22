import re

def isphonenumber_without_regex(text):
    if len(text) != 12:  
        return False
    if text[3] != '-' or text[7]!='-':  
        return False
    for i in range(0, 3):
        if not text[i].isdigit():  
            return False
    for i in range(4, 7):
        if not text[i].isdigit():  
            return False
    for i in range(8, 12):
        if not text[i].isdigit():  
            return False
    return True


def isphonenumber_with_regex(text):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, text))

phone_number = input("Enter a phone number (in the format XXX-XXX-XXXX): ")

if isphonenumber_without_regex(phone_number):
    print(f"{phone_number} is a valid phone number (without regex).")
else:
    print(f"{phone_number} is not a valid phone number (without regex).")

if isphonenumber_with_regex(phone_number):
    print(f"{phone_number} is a valid phone number (with regex).")
else:
    print(f"{phone_number} is not a valid phone number (with regex).")
