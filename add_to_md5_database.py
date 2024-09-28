import sqlite3
import hashlib
from datetime import datetime

def add_file_info_to_db(filename, md5, formatted_timestamp):
    db_path = "C:/Software/Databases/md5_file_tracker.db"
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO Documents (filename, md5code, datetime) VALUES (?, ?, ?)''', (filename, md5, formatted_timestamp))
    connection.commit()

def get_the_file_md5(filepath):
    md5_hash = hashlib.md5()
    with open(filepath, "rb") as file:
        for chunk in iter(lambda: file.read(4096),b""):
            md5_hash.update(chunk)

    return md5_hash.hexdigest()


filepath = "C:/Software/Python/md5_practice/example2.txt"
md5 = get_the_file_md5(filepath)
now = datetime.now()
formatted_timestamp = now.strftime("%Y/%m/%d_%H:%M:%S")
filename = filepath.strip().split('/')[-1]

print(filename, md5, formatted_timestamp)

add_file_info_to_db(filename, md5, formatted_timestamp)