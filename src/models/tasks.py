from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import DateTime
from datetime import datetime

from src.database import Base


class TaskModel(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    discr: Mapped[str]
    done: Mapped[bool]
    # date: Mapped[datetime] = mapped_column(default=datetime.now)
