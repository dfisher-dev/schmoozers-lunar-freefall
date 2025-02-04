from backend_db_connector import DatabaseConnector

import sqlite3

class DatabaseManager:
    def __init__(self, backend_db='backend.db'):
        self.conn = sqlite3.connect('backend_db')
        self.cursor = self.connect.cursor()

    # def create_new_mission(self, mass, altitude, start_fuel, thrust_power):