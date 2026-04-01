import sqlite3

connection = sqlite3.connect("phones.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS stores (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS phones (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    brand    TEXT,
    model    TEXT,
    price    REAL,
    storage  INTEGER,
    store_id INTEGER,
    FOREIGN KEY (store_id) REFERENCES stores(id)
)
""")

connection.commit()
connection.close()

print("Table ready!")
