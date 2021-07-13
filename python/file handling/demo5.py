# next line
file = open("four.txt", "a")
print("enter text to file to close type q")
while True:
    text = input()
    if text != "q":
        file.write(text + "\n")
    else:
        break
file.close()