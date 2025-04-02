from pydantic import BaseModel, Field
from datetime import datetime


class TaskSchema(BaseModel):
    name: str
    discr: str
    done: bool = False
    deadline: datetime = Field(default_factory=datetime.now)
