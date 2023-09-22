a=int(input("Enter Value for a"))
b=int(input("Enter Value for b"))
c=int(input("Enter Value for c"))
if a>c and b>c:
    average=(a+b)/2
elif b>a and c>a:
    average=(b+c)/2
else:
    average=(a+c)/2
print("Average Marks is : ",average)
