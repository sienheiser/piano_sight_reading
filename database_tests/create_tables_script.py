import sqlite3

database = "../test2.db"
con = sqlite3.connect(database)
cur = con.cursor()

for i in range(1,89):
    if i < 10:
        table_name = f"0{i}"
    else:
        table_name = f"{i}"

    stmt = f"CREATE TABLE K{table_name}(lesson_ID INT, time REAL)"
    cur.execute(stmt)

con.close()
