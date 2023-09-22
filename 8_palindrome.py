class PalindromeChecker:
    def __init__(self):
        self.is_palindrome = False

    def check(self, value):
        return
    
class StringPalindromeChecker(PalindromeChecker):
    def check(self, my_str):
        if my_str==my_str[::-1]:
            return True
        else:
            return False

class IntegerPalindromeChecker(PalindromeChecker):
    def check(self, num):
        temp = num
        rev = 0
        while temp != 0:
            digit = temp % 10
            rev = (rev * 10) + digit
            temp = temp // 10
        if num == rev:
            return True
        else:
            return False

input_str = input("Enter a string: ")
string_palindrome_checker = StringPalindromeChecker()
if string_palindrome_checker.check(input_str):
    print("Given string is a palindrome.")
else:
    print("Given string is not a palindrome.")

input_num = int(input("Enter an integer: "))
integer_palindrome_checker = IntegerPalindromeChecker()
if integer_palindrome_checker.check(input_num):
    print("Given integer is a palindrome.")
else:
    print("Given integer is not a palindrome.")
