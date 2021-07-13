import sqlite3 as sql
conn = sql.connect("RS.sqlite") #To get the connection
curs = conn.cursor() # To perform operation on database
curs.execute("create table Employee(idno number unique,name text,salary real)")
conn.commit()
print("data inserted")
conn.close()
print("thanks")