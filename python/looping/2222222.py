for x in range(5, 0, -2):
    for z in range(5, x, -1):
        print(" ", end="")
    for y in range(0, x):
        print("*", end=" ")
    print()
for x in range(3, 6, 2):
    for z in range(5, x, -1):
        print(" ", end="")
    for y in range(0, x):
        print("*", end=" ")
    print()
