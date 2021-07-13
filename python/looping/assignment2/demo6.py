#  W.A.P to print  1 to n Even and Odd Numbers
maximum = int(input("enter your maximum value:"))
for x in range(1, maximum, 2):
    for y in range(x, x+1,2):
        print(y, x+1)