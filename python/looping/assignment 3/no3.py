# A B C
# D E F
# G H I
# J K L
# M N O
counter = 65
for rows in range(1, 6):
    for col in range(0, 3):
        print(chr(counter), end=' ')
        counter += 1
    print()
