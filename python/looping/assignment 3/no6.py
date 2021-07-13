# 0 1 2 3 4
# 5 6 7 8 9
# 0 1 2 3 4
# 5 6 7 8 9

def rosy():
    counter=0
    for rows in range(1,3):
        for col in range(0, 5):
            print(counter,end=' ')
            counter += 1
        print()
rosy()
rosy()



