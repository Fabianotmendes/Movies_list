import sqlite3

class Banco:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def select(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def insert(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def close(self):
        self.connection.close()
 