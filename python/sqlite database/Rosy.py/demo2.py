import sqlite3 as sql
conn = sql.connect("customer.db")
curs = conn.cursor()
curs.execute("select * from Employee_update")
data = curs.fetchall()
print(data)
conn.close()
