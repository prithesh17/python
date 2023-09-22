import re
import os

def find_phone_numbers(text):
    phone_pattern = r'\+\d{12}'  
    phone_numbers = re.findall(phone_pattern, text)
    return phone_numbers

def find_email_addresses(text):
    email_pattern = r'[A-Z a-z 0-9]+@[A-Z a-z]+\.[A-Z a-z]{2,}'
    email_addresses = re.findall(email_pattern, text)
    return email_addresses

file_path = input("Enter the path for file : ")
if not os.path.isfile(file_path):
    print(f"File '{file_path}' not found.")
else:
    with open(file_path, 'r') as file:
        file_contents = file.read()
        phone_numbers = find_phone_numbers(file_contents)
        email_addresses = find_email_addresses(file_contents)

        print("Phone Numbers:")
        for phone_number in phone_numbers:
            print(phone_number)

        print("\nEmail Addresses:")
        for email_address in email_addresses:
            print(email_address)
