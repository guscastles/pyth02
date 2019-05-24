import sqlite3

connection = sqlite3.connect('example.db')
connection.row_factory = sqlite3.Row # give us dictionary results!
db = connection.cursor()

result = db.execute('SELECT * FROM employees')

# print(result.fetchall())
for r in result.fetchall():
    print(dict(r))

db.execute('INSERT INTO employees(first_name, hire_date) VALUES(?, ?)', ('hhh', 2022))
connection.commit()   # doesn't actually save without this
# connection.close()
