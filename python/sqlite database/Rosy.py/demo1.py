
import sqlite3 as sql
from sqlite3 import IntegrityError


idno = int(input("Enter Employee idno: "))
name = input("Enter Employee name: ")
salary=float(input("Enter Employee salary: "))

#To get the connection
conn = sql.connect("customer.db")
# To perform operation on database
curs = conn.cursor()
try:
    curs.execute("insert into Employee_update values(?,?,?)",(idno,name,salary))
    #To save your modification
    conn.commit()
    print("data inserted")
except IntegrityError:
    print("Given idno already exist")
finally:        
    #To close your connection
    conn.close()
print("thanks")
