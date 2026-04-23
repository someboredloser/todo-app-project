from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.task import TaskORM


class TaskRepository:
    def __init__(self, db: Session) -> None:
        self.db = db
    
    def get_by_user(self, user_id: str) -> list[TaskORM]:
        stmt = select(TaskORM).where(TaskORM.user_id == user_id)
        return self.db.scalars(stmt).all()
    
    def get_by_id(self, task_id: str) -> TaskORM | None: 
        return self.db.get(TaskORM, task_id)
    
    def create_task(self, title: str, user_id: str) -> TaskORM:
        new_task = TaskORM(title=title, user_id=user_id, completed=False)
        self.db.add(new_task)
        return new_task
    
    def delete_task(self, task: TaskORM) -> None:
        self.db.delete(task)