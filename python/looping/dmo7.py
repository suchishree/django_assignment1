#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

for x in range(1, 6):
    for z in range(5, x, -1):
        print(" ", end="")
    for y in range(0, x):
        print(y+1, end=" ")
    print()