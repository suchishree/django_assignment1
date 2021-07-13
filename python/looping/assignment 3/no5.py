# 9 8 7
# 6 5 4
# 3 2 1
counter = 9
for rows in range(1, 4):
    for col in range(0, 3):
        print(counter, end=' ')
        counter -= 1
    print()
