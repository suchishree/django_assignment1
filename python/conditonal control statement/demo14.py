# Write a program input three numbers and find out the biggest number.
no1 = int(input("enter 1st no:"))
no2 = int(input("enter 2nd no:"))
no3 = int(input("enter 3rd no:"))
if no1 > no2 and no1 > no3:
    print(no1, "is big")
if no2 > no1 and no2 > no3:
    print(no2, "is big")
if no3 > no2 and no3 > no1:
    print(no3, "is big")

