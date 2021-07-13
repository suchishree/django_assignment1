# 9
# 87
# 654
# 3210
counter = 10
for x in range(1,  5):
    for y in range(0, x):
        print(counter-1, end="")
        counter -= 1
        if counter == 10:
            print(0, end=" ")
    print()