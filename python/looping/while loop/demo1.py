# enter any no and print in reverse order
number = int(input("Enter a no:"))
reverse = 0
while number != 0:
    rem = number % 10
    number = number // 10
    reverse = reverse * 10 + rem
print("Given no in reverse order is:", reverse)

