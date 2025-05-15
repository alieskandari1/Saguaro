from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from . import models, schemas

async def get_tasks(db: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(models.Task).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

async def get_task(db: AsyncSession, task_id: int):
    query = select(models.Task).filter(models.Task.id == task_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def create_task(db: AsyncSession, task: schemas.TaskCreate):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def update_task(db: AsyncSession, task_id: int, task: schemas.TaskCreate):
    query = select(models.Task).filter(models.Task.id == task_id)
    result = await db.execute(query)
    db_task = result.scalar_one_or_none()
    
    if db_task:
        for key, value in task.model_dump(exclude_unset=True).items():
            setattr(db_task, key, value)
        await db.commit()
        await db.refresh(db_task)
    return db_task

async def delete_task(db: AsyncSession, task_id: int):
    query = select(models.Task).filter(models.Task.id == task_id)
    result = await db.execute(query)
    db_task = result.scalar_one_or_none()
    
    if db_task:
        await db.delete(db_task)
        await db.commit()
        return True
    return False
