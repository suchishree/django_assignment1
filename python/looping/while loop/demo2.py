# enter a no and print the sum of the digits of that no
number = int(input("Enter a no:"))
sum = 0
while number != 0:
    rem = number % 10
    number = number // 10
    sum = sum + rem
print("the sum is:", sum)


