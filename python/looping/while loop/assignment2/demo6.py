# 6. Input any 4 digit number and reverse it
# a. i/p:- 4325
# b. o/p:- 5234
number = int(input("Enter a no:"))
reverse = 0
while number != 0:
    rem = number % 10
    number = number // 10
    reverse = reverse * 10 + rem
print("Given no in reverse order is:", reverse)

