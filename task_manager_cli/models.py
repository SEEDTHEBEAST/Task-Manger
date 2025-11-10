from datetime import datetime
from typing import Literal, Optional
from dataclasses import dataclass

@dataclass 

class Task: 
    # for learning purposes only this can be used to represent items in a game
    id: int
    taskBio: str
    taskImportance: int
    status: Literal["to-do", "In Progress","Done","Planned","Postponed"] = "to-do"
    created_at: Optional[datetime] = None

    def post_init(self):
        if self.created_at is None:
            self.created_at = datetime.now()