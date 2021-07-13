idno = int(input("enter employee id no:"))
name = input("enter employee name:")
salary = float(input("enter employee salary:"))
import sqlite3 as sql
conn = sql.connect("RS.sqlite") #To get the connection
curs = conn.cursor() # To perform operation on database
curs.execute("insert into Employee values(?,?,?)",(idno,name,salary))
conn.commit() # To savee your modification
print("data inserted")
conn.close()
print("thanks")