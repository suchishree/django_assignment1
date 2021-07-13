# pickle(write)

import pickle
id_no = 101
name = "suchishree"
salary = 185000.00
file = open("employee.txt", "wb")
pickle.dump(id_no, file)
pickle.dump(name, file)
pickle.dump(salary, file)
file.close()


