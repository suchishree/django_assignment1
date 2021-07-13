# readlines mode
file = open("four.txt", "r")
text = file.readlines()
print(text[2])
file.close()