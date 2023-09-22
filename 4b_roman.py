def roman_to_int(roman):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_value = 0

    for symbol in reversed(roman):
        value = roman_dict[symbol]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result

roman_numeral = input("Enter a Roman numeral: ").upper()
integer_value = roman_to_int(roman_numeral)
print(f"The integer value of {roman_numeral} is {integer_value}")
