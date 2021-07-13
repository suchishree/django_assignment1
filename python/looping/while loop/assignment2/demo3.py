# 3. Input any 10 numbers find out no of positive numbers and no of negative numbers even_count = 0
positive_count = 0
negative_count = 0
for x in range(10):
    no = int(input("enter a number:"))
    if no > 0:
        positive_count += 1
    if no < 0:
        negative_count += 1
print("positive number:", positive_count)
print("negative number:", negative_count)
