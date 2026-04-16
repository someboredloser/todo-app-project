from fastapi import APIRouter, Depends, HTTPException, status
from app.dependencies.db import get_task_service
from app.exception.task import TaskNotFound
from app.schemas.task import TaskCreateSchema, TaskSchema, TaskUpdateSchema
from app.services.task import TaskService

router = APIRouter(prefix="/tasks")


@router.get("")
def read_task(
    task_services: TaskService = Depends(get_task_service)
) -> list[TaskSchema]:
    return task_services.list_tasks()

@router.post("", status_code=status.HTTP_201_CREATED)
def create_task(
    payload: TaskCreateSchema, 
    task_services: TaskService = Depends(get_task_service)
) -> TaskSchema:
    return task_services.create_task(task_create=payload)
    
@router.patch("/{task_id}")
def update_task(
    task_id: str, payload: TaskUpdateSchema, 
    task_services: TaskService = Depends(get_task_service)
) -> TaskSchema:
    try:
        return task_services.update_task(task_id=task_id, task_update=payload)
    except TaskNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
@router.delete("/{task_id}")
def delete_task(
    task_id: str,
    task_services: TaskService = Depends(get_task_service)
) -> None:
    try:
        task_services.delete_task(task_id=task_id)
    except TaskNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        