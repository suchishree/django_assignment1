# unpickle(read)
import pickle
file = open("employee.txt", "rb")
id_no = pickle.load(file)
name = pickle.load(file)
salary = pickle.load(file)
print(id_no, name, salary)

file.close()



