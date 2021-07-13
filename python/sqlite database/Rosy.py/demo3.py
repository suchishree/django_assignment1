import sqlite3 as sql
conn = sql.connect("customer.db")
curs = conn.cursor()
curs.execute("Delete from Employee_update Where idno = 102")
conn.commit()
print("deleted")
conn.close()