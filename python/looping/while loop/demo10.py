#  W.a.p to find given number is Magic number or not
# Consider  n value is  9
#  9 → 9 * 9  = 81
#    ➔1 + 8   ➔ 9
number = int(input("enter no:"))
multiply = number*number
sum = 0
while multiply != 0:
    rem = multiply % 10
    multiply = multiply // 10
    sum = sum + rem
if number == sum:
    print(sum, "is a magic number")
else:
    print(number, "is not a magic number")


