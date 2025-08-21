# WAP to check if a number is divisible by 7 and last digit is 5

a = int(input("Enter a number"))
if a%7==0 and a%10==5:
    print("The number is divisible by 7 and the last digit is 5")
else:
    print("The number is not divisible by 7 and the last digit is 5")
    