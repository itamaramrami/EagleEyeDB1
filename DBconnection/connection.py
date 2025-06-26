import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS eagleEyeDB")
cursor.execute("USE eagleEyeDB")

create_table_query = """
CREATE TABLE IF NOT EXISTS agents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codeName VARCHAR(255),
    realName VARCHAR(255),
    location VARCHAR(255),
    status VARCHAR(50),
    missionsCompleted INT
)
"""

cursor.execute(create_table_query)

print("Database and table created successfully.")

cursor.close()
connection.close()
