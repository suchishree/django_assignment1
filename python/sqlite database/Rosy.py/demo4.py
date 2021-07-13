import sqlite3 as sql
conn = sql.connect("customer.db")
curs = conn.cursor()
curs.execute("update Employee_update set salary=10000.00 where idno=101")
conn.commit()
print("updated")
conn.close()