#  Write a Script to find given number is Armstrong Number or not
number = number1 = int(input("enter no:"))
sum = 0
while number != 0:
    rem = number % 10
    number = number // 10
    sum = sum + rem**3
if sum == number1:
    print(sum, "is a armstrong number")
else:
    print(number1, "is not a armstrong number")




