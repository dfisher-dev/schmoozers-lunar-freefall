import sqlite3

class DatabaseConnector:
    def __init__(self, backend_db='backend.db'):
        self.backend_db = backend_db

    def connect(self):
        return sqlite3.connect(self.backend_db)