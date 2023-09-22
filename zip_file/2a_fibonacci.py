def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter a positive integer (N > 0): "))
if num > 0:
    for i in range(1,num+1):
        print(f"The {i}th Fibonacci number is: ",fibonacci(i))
else:
    print("Invalid Input")
