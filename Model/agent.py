from enum import Enum

class AgentStatus(Enum):
    ACTIVE = "Active"
    INJURED = "Injured"
    MISSING = "Missing"
    RETIRED = "Retired"

class Agent:
    def __init__(self, code_name, real_name, location, status: AgentStatus, missions_completed):
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status  
        self.missions_completed = missions_completed

    def __str__(self):
        return f"Agent {self.code_name} name: ({self.real_name}), Location: {self.location}, " \
               f"Status: {self.status.value}, Missions: {self.missions_completed}"
