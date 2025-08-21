# input three numbers and find minimum among them
a=int(input("Enter a "))
b=int(input("Enter b"))
c=int(input("Enter c"))

if a<=b and a<=c:
    print("a is smaller")
elif b<=a and b<=c:
    print("b is smaller")
else:
    print("c is smaller")
