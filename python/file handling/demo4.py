# ask file name from user
file_name = input("enter file name:")
file = open(file_name, 'a')
text = input("enter text:")
file.write(text)
file.close()