def is_binary(binary_number):
    while binary_number != 0:
        i = binary_number % 10
        if i != 0 and i != 1:
            return False
        binary_number = binary_number // 10
    return True


def is_octal(octal_number):
    number = str(octal_number)
    if number.count('8') == 0 and number.count('9') == 0:
        return True
    return False


def binary_to_decimal(binary_number, index=0):
    if binary_number == 0:
        return 0
    else:
        return ( (binary_number % 10) * (2 ** index) + binary_to_decimal(binary_number // 10, index + 1) )

def octal_to_dec(octal_number, index=0):
    if octal_number == 0:
        return 0
    else:
        return (octal_to_dec(octal_number // 10, index + 1) + (octal_number % 10) * (8 ** index))

def hexa_character(number):
    if number < 10:
        return str(number)
    elif number == 10:
        return 'a'
    elif number == 11:
        return 'b'
    elif number == 12:
        return 'c'
    elif number == 13:
        return 'd'
    elif number == 14:
        return 'e'
    else:
        return 'f'


def dec_to_hex(number):
    if number == 0:
        return ''
    return dec_to_hex(number // 16) + hexa_character(number % 16)


def octal_to_hexa(octal_number):
    answer_in_dec = octal_to_dec(octal_number)
    return dec_to_hex(answer_in_dec)


binary_number = int(input("Enter Binary Number "))
octal_number = int(input("Enter octal Number "))
if is_binary(binary_number):
    print("Decimal  Equivalent of ", binary_number, " is ", binary_to_decimal(binary_number))
else:
    print("Input is not a binary Number")

if is_octal(octal_number):
    print("Hexa decimal Equivalent of ", octal_number, " is ", octal_to_hexa(octal_number))
else:
    print("Input is not a octal Number")
