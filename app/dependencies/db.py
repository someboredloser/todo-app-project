from typing import Generator
from fastapi import Depends
from app.database.session import SessionLocal
from sqlalchemy.orm import Session
from app.services.task import TaskService


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_task_service(db: Session = Depends(get_db)):
    return TaskService(db)