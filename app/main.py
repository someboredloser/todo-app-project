from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.task import router as task_router
from app.core.config import settings


app = FastAPI(
    title="TASK-MANAGER",
    debug=settings.debug
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_router)