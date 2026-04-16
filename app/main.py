from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database.base import Base
from app.database.engine import engine
from fastapi.middleware.cors import CORSMiddleware
from app.routes.task import router as task_router
from app.core.config import settings


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    lifespan=lifespan,
    title="TODO API",
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