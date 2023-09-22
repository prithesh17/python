num = int(input("Enter an integer: "))
original_num = num
reverse_num = 0

while num > 0:
    remainder = num % 10
    reverse_num = reverse_num * 10 + remainder
    num = num // 10

if original_num == reverse_num:
    print("Given Number is a palindrome.")
else:
    print("Given Number is not a palindrome.")
     
str_num = str(original_num)
for i in range(10):
     if str_num.count(str(i)) > 0:
         print(str(i), "appears", str_num.count(str(i)), "times")
