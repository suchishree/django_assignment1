# 5. Program to check whether a number is divisible by 5 and 11 or not
number = int(input("enter any number:"))
if number % 5 == 0 and number % 11 == 0:
    print(number, "is divisible by 5 and 11 ")
else:
    print(number, "is not divisible by 5 and 11 ")