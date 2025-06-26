from Dal_Agent.agent_dal import AgentDAL
from model.agent import *

def menu():
    connection = AgentDAL.get_connection()
    agent_dal = AgentDAL(connection)
    while True:
        AgentDAL.display_menu()
        choice = input("Select an option: ")

        if choice == '1':
            code_name = input("Code Name: ")
            real_name = input("Real Name: ")
            location = input("Location: ")
            status = AgentDAL.choose_status()
            missions = int(input("Missions Completed: "))

            agent = Agent(code_name, real_name, location, status, missions)
            agent_dal.create_agent(agent)
            print(" Agent added successfully.")

        elif choice == '2':
            agents = agent_dal.get_all_agents()
            if agents:
                for a in agents:
                    print(a)
            else:
                print("No agents found.")

        elif choice == '3':
            agent_id = int(input("Enter Agent ID: "))
            agent = agent_dal.get_agent_by_id(agent_id)
            if agent:
                print(agent)
            else:
                print(" Agent not found.")

        elif choice == '4':
            agent_id = int(input("Enter Agent ID to update: "))
            code_name = input("New Code Name: ")
            real_name = input("New Real Name: ")
            location = input("New Location: ")
            status = AgentDAL.choose_status()
            missions = int(input("New Missions Completed: "))

            updated_agent = Agent(code_name, real_name, location, status, missions)
            agent_dal.update_agent(agent_id, updated_agent)
            print("Agent updated.")

        elif choice == '5':
            agent_id = int(input("Enter Agent ID to delete: "))
            agent_dal.delete_agent(agent_id)
            print(" Agent deleted.")

        elif choice == '6':
            print("You went out successfully")
            break

        else:
            print(" Invalid option. Try again.")

    connection.close()