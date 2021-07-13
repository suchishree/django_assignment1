# 11. Wap to accept a no from console and check whether given no is Strong no or not?
# a. i/p: - 145
# i. 1!+4!+5!

number = number1 = int(input("Enter your no:"))
sum = 0
while number != 0:
    factorial = 1
    rem = number % 10
    number = number // 10
    for i in range(1, rem+1):
        factorial = factorial * i
    sum = sum + factorial

if number1 == sum:
    print(sum, "is a strong no")
else:
    print(number1, "is not a strong no")


