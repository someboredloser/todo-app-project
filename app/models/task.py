from uuid import uuid4

from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class TaskORM(Base):
    __tablename__ = "tasks"
        
    id: Mapped[str] = mapped_column(
        primary_key=True,
        default=lambda: str(uuid4())
    )
    title: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)