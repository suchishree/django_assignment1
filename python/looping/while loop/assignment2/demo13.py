# 13. Input any 4 digit number and find out the sum of middle digits
number =int (input('enter a 4 digit no:'))
sum = 0
rem1 = 0
if number >= 10000:
    print("you entered max no")
elif number <= 999:
    print("you entered min no")
else:
    while number >= 100:
        rem1 = rem1 // 10
        number = number//10
        rem = number % 100
        rem1 = number % 10
        sum = sum + rem1
    print(sum)