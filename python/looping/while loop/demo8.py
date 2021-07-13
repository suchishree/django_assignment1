# 6) Write a Script to sum of prime numbers in a given number
number = int(input("Enter a no:"))
sum = 0
while number != 0:
    rem = number % 10
    number = number // 10
    if rem != 4 and rem != 6 and rem != 8 and rem != 9:
        sum = sum + rem
print("the sum is:", sum)


