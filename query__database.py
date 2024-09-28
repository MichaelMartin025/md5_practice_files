import sqlite3

db_path = "C:/Software/Databases/md5_file_tracker.db"
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

cursor.execute('SELECT * FROM Documents')
rows = cursor.fetchall()

for row in rows:
    print(row)