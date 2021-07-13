#     *
#    * *
#   * * *
#  * * * *
# * * * * *
for x in range(1, 6):
    for z in range(5, x, -1):
        print(" ", end="")
    for y in range(0, x):
        print('*', end=" ")
    print()