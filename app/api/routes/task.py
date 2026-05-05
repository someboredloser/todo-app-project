from fastapi import APIRouter, Depends, HTTPException, status
from app.dependencies.auth import get_current_user
from app.dependencies.db import get_task_service
from app.exception.task import TaskNotFound
from app.schemas.task import TaskCreateSchema, TaskSchema, TaskUpdateSchema
from app.services.task import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])



@router.get("", response_model=list[TaskSchema])
def read_task(
    page: int = 1,
    limit: int = 5,
    user = Depends(get_current_user),
    task_services: TaskService = Depends(get_task_service)
) -> list[TaskSchema]:
    
    offset = (page - 1) * limit
    
    return task_services.list_tasks(
        user=user,
        limit=limit,
        offset=offset
    )

@router.post("", status_code=status.HTTP_201_CREATED, response_model=TaskSchema)
def create_task(
    payload: TaskCreateSchema,
    user = Depends(get_current_user),
    task_services: TaskService = Depends(get_task_service)
) -> TaskSchema:
    return task_services.create_task(payload, user)
    
@router.patch("/{task_id}", response_model=TaskSchema)
def update_task(
    task_id: str,
    payload: TaskUpdateSchema,
    user = Depends(get_current_user),
    task_services: TaskService = Depends(get_task_service)
) -> TaskSchema:
    try:
        return task_services.update_task(
            task_id=task_id,
            task_update=payload,
            user=user
        )
    except TaskNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Task not found"
        )
    
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: str,
    user = Depends(get_current_user),
    task_services: TaskService = Depends(get_task_service)
) -> None:
    try:
        task_services.delete_task(task_id=task_id, user=user)
    except TaskNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Task not found"
        )