# 5
# 10 15
# 20 25 30
# 35 40 40 45
counter = 1
for x in range(1, 5):
    for y in range(0, x):
        print(counter * 5, end=" ")
        counter += 1
        if counter*5 == 45:
            print(40, end=" ")
        if counter*5 == 50:
            break
    print()