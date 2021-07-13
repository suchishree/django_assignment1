# 10. Wap to accept a no from console and check whether given no is perfect no or not?
# a. Sum of proper divisors
# b. i/p:- 6  1+2+3
# i. 28   1+2+4+7+14
number = int(input("enter a number:"))
sum = 0
for i in range(1, number):
    if number % i == 0:
        sum = sum + i
print(sum)
if sum == number:
    print(number, "is perfect no")
else:
    print(number, "is not a perfect no")




