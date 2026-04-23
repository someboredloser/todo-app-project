from uuid import uuid4

from sqlalchemy import ForeignKey

from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class TaskORM(Base):
    __tablename__ = "tasks"
        
    id: Mapped[str] = mapped_column(
        primary_key=True,
        default=lambda: str(uuid4())
    )
    title: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    
    user = relationship("UserORM", back_populates="tasks")