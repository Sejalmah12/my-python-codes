#WAP to read three angles o triangles and determine their types(Right triangle, obtuse triangle, acute triangle)
a = int(input("Enter first angle: "))
b = int(input("Enter second angle:"))
c = int(input("Enter third angle: "))
if a>90 and b>90 and c>90:
    print("The angle is obtuse angle")
elif a==90 and b==90 and c==90:
    print("The angle is right angle")
else:
    print("The angle is acute triangle")





