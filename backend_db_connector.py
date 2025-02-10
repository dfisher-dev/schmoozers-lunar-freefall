import sqlite3

class DatabaseConnector:
    def __init__(self, backend_db='backend.db'):
        self.backend_db = backend_db
        self.conn = None
        self.cursor = None

    def connect(self):
        """Establish a connection to the SQLite database."""
        self.conn = sqlite3.connect(self.backend_db)
        self.cursor = self.conn.cursor()
        print("Database connection established.")

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

    def commit(self):
        """Commit the current transaction."""
        if self.conn:
            self.conn.commit()
            print("Changes committed to the database.")

    def execute_query(self, query, params=()):
        """Execute a given SQL query with optional parameters."""
        if self.cursor:
            self.cursor.execute(query, params)
            print(f"Executed query: {query}")

    def fetchall(self):
        """Fetch all rows from the last executed query."""
        if self.cursor:
            return self.cursor.fetchall()

    def fetchone(self):
        """Fetch one row from the last executed query."""
        if self.cursor:
            return self.cursor.fetchone()

# Example usage:
# db = DatabaseConnector()
# db.connect()
# db.execute_query("SELECT * FROM mission_start")
# results = db.fetchall()
# print(results)
# db.close()