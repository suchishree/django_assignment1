# A
# BB
# CCC
# DDDD
# EEEEE
counter = 65
for x in range(1, 6):
    for y in range(0, x):
        print(chr(counter), end="")
    counter += 1
    print()
