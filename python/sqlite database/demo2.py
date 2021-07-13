import sqlite3 as sql
conn = sql.connect("RS.sqlite") #To get the connection
curs = conn.cursor() # To perform operation on database
curs.execute("insert into Employee values(101,'Ravi',185000.00)")
conn.commit()
print("data inserted")
conn.close()
print("thanks")