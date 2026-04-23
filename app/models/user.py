from uuid import uuid4

from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class UserORM(Base):
    __tablename__ = "users"
    
    id: Mapped[str] = mapped_column(
        primary_key=True,
        default=lambda: str(uuid4())
    )
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str] = mapped_column()
    
    tasks = relationship("TaskORM", back_populates="user")