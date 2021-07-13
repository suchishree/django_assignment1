#     1
#    12
#   123
#  1234
# 12345
for x in range(1, 6):
    for z in range(5, x, -1):
        print(" ", end="")
    for y in range(0, x):
        print(y+1, end="")
    print()