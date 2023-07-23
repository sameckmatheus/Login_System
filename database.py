import sqlite3

class DatabaseConfig:
    def __init__(self, database_name):
        self.database_name = database_name 

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