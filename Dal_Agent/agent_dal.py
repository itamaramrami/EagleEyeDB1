from model.agent import *
import mysql.connector

class AgentDAL:
    def __init__(self, connection):
        self.connection = connection

    def create_agent(self, agent):
        query = """
        INSERT INTO agents (codeName, realName, location, status, missionsCompleted)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (agent.code_name, agent.real_name, agent.location, agent.status.value, agent.missions_completed)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
        self.connection.commit()

    def get_all_agents(self):
        query = "SELECT * FROM agents"
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def get_agent_by_id(self, agent_id):
        query = "SELECT * FROM agents WHERE id = %s"
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(query, (agent_id,))
            return cursor.fetchone()

    def update_agent(self, agent_id, updated_agent):
        query = """
        UPDATE agents
         codeName = %s,
            realName = %s,
            location = %s,
            status = %s,
            missionsCompleted = %s
        WHERE id = %s
        """
        values = (
            updated_agent.code_name,
            updated_agent.real_name,
            updated_agent.location,
            updated_agent.status.value,
            updated_agent.missions_completed,
            agent_id
        )
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
        self.connection.commit()

    def delete_agent(self, agent_id):
        query = "DELETE FROM agents WHERE id = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (agent_id,))
        self.connection.commit()

    def get_connection():
        return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="eagleEyeDB"
    )

    def display_menu():
        print("\n--- Agent Management ---")
        print("1. Add New Agent")
        print("2. View All Agents")
        print("3. View Agent by ID")
        print("4. Update Agent")
        print("5. Delete Agent")
        print("6. Exit")

    def choose_status():
         print("Choose Status:")
         for i, status in enumerate(AgentStatus, start=1):
              print(f"{i}. {status.value}")
         choice = int(input("Enter choice: "))
         return list(AgentStatus)[choice - 1]
