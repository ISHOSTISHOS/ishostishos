import sqlite3

connection = sqlite3.connect('app.db')
cursor = connection.cursor()
print('DB created!')

cursor.execute('''CREATE TABLE drivers_test 
                  (question TEXT, ans1 TEXT, ans2 TEXT, correct TEXT)''')
connection.close()
print('Table created!')

