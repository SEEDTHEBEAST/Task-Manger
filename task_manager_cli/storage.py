# This module handles loading tasks, saving tasks, and Converting them bwtween diffrent objects

import json
from pathlib import Path
from  typing import List
from .models import Task

class Storage:

def __init__(self, file_path: str = "tasks.json"):
    self.file_path = Path(file_path)

    def load_tasks(self) -> List[Task]:

       
       
        #TODO: Implement loading tasks from a JSON file
        #If a file does not exist then return an empty list
        # Convert Json data back into Task objects

        pass

def save_tasks(self, tasks: List[Task] -> None:

# ToDO: Convert task objects to json 


     pass
