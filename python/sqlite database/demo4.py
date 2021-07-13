import sqlite3 as sql
from sqlite3 import IntegrityError


idno = int(input("enter employee id no:"))
name = input("enter employee name:")
salary = float(input("enter employee salary:"))

conn = sql.connect("RS.sqlite") #To get the connection
curs = conn.cursor() # To perform operation on database
try:
    curs.execute("insert into Employee values(?,?,?)",(idno,name,salary))
    conn.commit() # To savee your modification
    print("data inserted")
except IntegrityError:
    print("The given id no is repeted")  
finally:
    conn.close()
print("thanks")