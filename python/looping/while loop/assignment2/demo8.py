# 8. Input any 4 digit number and find out the sum of the digits
# a. i/p:- 4321
# b. o/p: -  4+3+2+1=10
number = int(input("Enter a no:"))
sum = 0
while number != 0:
    rem = number % 10
    number = number // 10
    sum = sum + rem
print("the sum is:", sum)

