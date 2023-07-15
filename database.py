import sqlite3

database_connection = sqlite3.Connection('database')
cursor = database_connection.cursor()

# database table with sqlite3
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        UserName TEXT NOT NULL,
        Email TEXT NOT NULL,
        Password TEXT NOT NULL,
        ConfirmPassword TEXT NOT NULL        
    )
""")

print("Successful Database Connection...")