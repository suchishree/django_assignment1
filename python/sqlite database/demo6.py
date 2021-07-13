#reading all record from a table
import sqlite3 as sql
conn = sql.connect("RS.sqlite")
curs = conn.cursor()
curs.execute("select * from Employee")
data = curs.fetchone()
print(data)
conn.close()
print("thanks")