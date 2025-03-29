from pydantic import BaseModel
from datetime import datetime


class TaskSchema(BaseModel):
    name: str
    discr: str
    done: bool = False
    # date: datetime.date = datetime.now


class TaskUpdateSchema(TaskSchema):
    id: int
