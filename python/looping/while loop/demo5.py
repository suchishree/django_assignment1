# 3) Write a Script to sum of even digits in a given number
number = int(input("Enter a no:"))
sum = 0
while number != 0:
    rem = number % 10
    number = number // 10
    if rem % 2 == 0:
        sum = sum + rem

print("the sum is:", sum)



