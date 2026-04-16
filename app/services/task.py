from sqlalchemy.orm import Session
from app.exception.task import TaskNotFound
from app.repositories.task import TaskRepository
from app.schemas.task import TaskCreateSchema, TaskSchema, TaskUpdateSchema


class TaskService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.task_repository = TaskRepository(db=db)
        
    def list_tasks(self) -> list[TaskSchema]:
        tasks_orm = self.task_repository.get_all()
        return [TaskSchema.model_validate(task) for task in tasks_orm]
    
    def create_task(self, task_create: TaskCreateSchema) -> TaskSchema:
        create_tasks_orm = self.task_repository.create_task(title=task_create.title)
        self.db.add(create_tasks_orm)
        self.db.commit()
        return TaskSchema.model_validate(create_tasks_orm)
    
    def update_task(self, task_id: str, task_update: TaskUpdateSchema) -> TaskSchema:
        task_for_update = self.task_repository.get_by_id(task_id=task_id)
        
        if not task_for_update:
            raise TaskNotFound(f"The task with id {task_id} not found.")
        
        if task_update.title is not None:
            task_for_update.title = task_update.title
        if task_update.completed is not None:
            task_for_update.completed = task_update.completed    
            
        self.db.commit()
        
        return TaskSchema.model_validate(task_for_update)
    
    def delete_task(self, task_id: str) -> None:
        task_for_delete = self.task_repository.get_by_id(task_id=task_id)
        if not task_for_delete:
            raise TaskNotFound(f"The task with id {task_id} not found.")
        self.task_repository.delete_task(task_for_delete)
        self.db.commit()