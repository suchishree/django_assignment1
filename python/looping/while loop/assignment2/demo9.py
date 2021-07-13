# 9. Wap to accept a no from console and check whether given no is Armstrong no or not?
# a. 153=1**3+5**3+3**3
number = number1 = int(input("enter any number:"))
sum = 0
while number != 0:
    rem = number % 10
    number = number // 10
    sum = sum + rem**3
if sum == number1:
    print(sum, "is a armstrong no.")
else:
    print(number1, "is not a armstrong no.")

