from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.core.roles import Role
from app.exception.task import TaskNotFound
from app.models.user import UserORM
from app.repositories.task import TaskRepository
from app.schemas.task import TaskCreateSchema, TaskSchema, TaskUpdateSchema
from sqlalchemy.exc import SQLAlchemyError

class TaskService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.task_repository = TaskRepository(db=db)
        
    def list_tasks(self, user: UserORM) -> list[TaskSchema]:
        tasks_orm = self.task_repository.get_by_user(user_id=user.id)
        return [TaskSchema.model_validate(task) for task in tasks_orm]
    
    def create_task(self, task_create: TaskCreateSchema, user: UserORM) -> TaskSchema:
        create_tasks_orm = self.task_repository.create_task(
            title=task_create.title,
            user_id=user.id
        )
        try:
            self.db.commit()
        except SQLAlchemyError:
            self.db.rollback()
            raise
        return TaskSchema.model_validate(create_tasks_orm)
    
    def update_task(
        self, task_id: str, 
        task_update: TaskUpdateSchema,
        user: UserORM
    ) -> TaskSchema:
        task_for_update = self.task_repository.get_by_id(task_id=task_id)
        
        if not task_for_update:
            raise TaskNotFound(f"The task with id {task_id} not found.")
        
        if task_for_update.user_id != user.id and user.role != Role.admin:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Forbidden"
            )
        
        if task_update.title is not None:
            task_for_update.title = task_update.title
        if task_update.completed is not None:
            task_for_update.completed = task_update.completed    
            
        try:
            self.db.commit()
        except SQLAlchemyError:
            self.db.rollback()
            raise
        
        return TaskSchema.model_validate(task_for_update)
    
    def delete_task(self, task_id: str, user: UserORM) -> None:
        task_for_delete = self.task_repository.get_by_id(task_id=task_id)
        if not task_for_delete:
            raise TaskNotFound(f"The task with id {task_id} not found.")
        
        if task_for_delete.user_id != user.id and user.role != Role.admin:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Forbidden"
            )
            
        self.task_repository.delete_task(task_for_delete)
        try:
            self.db.commit()
        except SQLAlchemyError:
            self.db.rollback()
            raise