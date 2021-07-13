# Write a Script to sum of 5 divisible in a given number
number = int(input("Enter a no:"))
sum = 0
while number != 0:
    rem = number % 10
    number = number // 10
    if rem % 5 == 0:
        sum = sum + rem

print("the sum is:", sum)


