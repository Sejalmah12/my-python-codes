# WAP read three integers and print their maximum
a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))

if a>=b and a>=c:
    print("a is maximum")
elif b>=a and b>=c:
    print("b is maximum")
else:
    print("c is maximum")
    