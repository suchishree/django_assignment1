# enter a no and print the sum of the 1st and last digits of that no
number = int(input("Enter a no:"))
first = number % 10
while number != 0:
    rem = number % 10
    number = number // 10

print("the sum of the 1st and last digits is:", first+rem)


