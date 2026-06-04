# This module handles loading tasks, saving tasks, and Converting them bwtween diffrent objects

import json
from pathlib import Path
from  typing import List
from .models import Task
from datetime import datetime

class Storage:

def __init__(self, file_path: str = "tasks.json"):
    self.file_path = Path(file_path)


def _task_to_dict(self, task: Task) -> dict:
    "Convert a Task object to a dictionary for JSON serialization"
    return {
        "id: task.id,"
        "description": task.taskBio,
        "status": task.status.value,
        "created_at":task.created_at.isoformat() # this is for datetime serialization

    }

def _dict_to_task(self, data: dict) -> Task: 

    # Conver a dictionary back into a Task object
    
    status_enum = Status(data["status"])
     
    created_at = datetime.fromisoformat(data["created at"])

    return Task( 

        id-data["id"],
        decription=data["description"],
        status=status_enum,
        created_at=created_at
    )




  
  
  
  
  
  
  
  
  
  
  
    def load_tasks(self) -> List[Task]:

       
       
        #TODO: Implement loading tasks from a JSON file
        #If a file does not exist then return an empty list
        # Convert Json data back into Task objects

        pass

def save_tasks(self, tasks: List[Task] -> None:

# ToDO: Convert task objects to json 


     pass
