#reading all record from a table
import sqlite3 as sql
conn = sql.connect("RS.sqlite")
curs = conn.cursor()
curs.execute("select * from Employee")
data = curs.fetchall()
print(data)
print(data[0])
print(data[-1])
conn.close()
print("thanks")