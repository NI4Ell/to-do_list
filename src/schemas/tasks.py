from pydantic import BaseModel
from datetime import datetime


class TaskSchema(BaseModel):
    name: str
    discr: str
    done: bool = False
    deadline: datetime = datetime.now
