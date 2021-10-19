import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE users (
        user_id TEXT NOT NULL PRIMARY KEY,
        user TEXT NOT NULL,
        password TEXT NOT NULL
    );
""")

print("Tabela criada com sucesso!")

conn.close()