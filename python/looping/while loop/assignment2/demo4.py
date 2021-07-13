# 4. Input any 10 numbers find the  first biggest and second biggest number
number1 = 0
number2 = 0
for x in range(5):
    number = int(input("enter a number:"))
    if number > number1:
        number1 = number
print(number1, "1st biggest no")
#print(number, "2nd biggest no")

