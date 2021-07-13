# append mode
file = open("three.txt", "a")
text = input("enter your text:")
file.write(text)
file.close()