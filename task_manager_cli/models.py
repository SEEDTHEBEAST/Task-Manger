from dataclasses import dataclass

@dataclass 

class Task: 
    """ for learning purposes only this can be used to represent items in a game"""
    taskName: str
    taskBio: str
    taskImportance: int
    status: str = "Pending"