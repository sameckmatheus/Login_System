import sqlite3

class DatabaseConfig:
    def __init__(self, database_name):
        self.database_name = database_name

class DatabaseConnection:
    def connect(self):
        pass

    def execute_query(self, query):
        pass

class SQLiteConnection(DatabaseConnection):
    def __init__(self, config):
        self.connection = None
        self.config = config

    def connect(self):
        self.connection = sqlite3.connect(self.config.database_name)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()


if __name__ == "__main__":
    database_config = DatabaseConfig(database_name="database.sqlite")

    database_connection = SQLiteConnection(config=database_config)
    database_connection.connect()

    database_connection.execute_query("""
        CREATE TABLE IF NOT EXISTS users (
            Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            UserName TEXT NOT NULL,
            Email TEXT NOT NULL,
            Password TEXT NOT NULL,
            ConfirmPassword TEXT NOT NULL        
        )
    """)

    print("Successful Database Connection...")
