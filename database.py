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
        self.config = config

    def connect(self):
        self.connection = sqlite3.connect(self.config.database_name)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()