from fastapi import FastAPI
from .routers import tasks
from .database import engine
from . import models
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield


app = FastAPI(
    title="Task Management API",
    description="A simple API for managing tasks using FastAPI and PostgreSQL",
    version="1.0.0",
    debug=False,
    lifespan=lifespan
)

app.include_router(tasks.router, prefix="/api/v1", tags=["tasks"])
