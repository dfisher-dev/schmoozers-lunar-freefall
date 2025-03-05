import sqlite3
import freeFallNew

class ValuesManager:
    def save_mission_data(self, mission_data):
        columnNamesStr = ', '.join(mission_data.keys())
        placeholders = ', '.join(['?'] * len(mission_data))
        query = f'INSERT INTO mission_data ({columnNamesStr}) VALUES ({placeholders})'
        values = tuple(mission_data.values())

        self.cursor.execute(query, values)
        self.connection.commit()

