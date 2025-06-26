import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.agent import *
from Dal_Agent.agent_dal import AgentDAL
from menu import *


def main():
    
     menu()
    
    

if __name__ == "__main__":
    main()
