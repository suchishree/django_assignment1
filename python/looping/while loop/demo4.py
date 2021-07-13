# enter a no and print the sum of the digits of that no until u get a
# single digit

number = int(input("Enter a no:"))
sum = number % 9
if sum == 0:
    print("the sum is 9")
else:
    print("the sum is:", sum)


