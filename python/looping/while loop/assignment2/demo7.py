# 7. Wap to extract the Digits from the given number?
# a. i/p:- 4321
# b. o/p:- 4 3 2 1
number = int(input("Enter a no:"))
sum = 0
while number != 0:
    rem = number % 10
    number = number // 10
    sum = rem
    print(sum, end=" ")


