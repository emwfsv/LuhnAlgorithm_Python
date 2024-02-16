import pyodbc
import pandas as pd

class DatabaseHandler():
    def __init__(self, connectionString):
        self.connectionString = connectionString

    def readAllRowData(self, tableName):
        conn = pyodbc.connect(self.connectionString)

        with conn.cursor() as cursor:
            # Read data from database
            sql = str.format("SELECT * FROM {}", tableName)
            cursor.execute(sql)

            # Fetch all rows
            rows = cursor.fetchall()

            # Print results
            for row in rows:
                print(row)

        conn.close()
