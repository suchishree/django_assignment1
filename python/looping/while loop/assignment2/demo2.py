# 2. Input any 10 numbers find out no of even numbers and no of odd number
even_count = 0
odd_count = 0
for x in range(10):
    no = int(input("enter a number:"))
    if no % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("even number:", even_count)
print("odd number:", odd_count)





