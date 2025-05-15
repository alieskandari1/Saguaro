from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.sql import func

from .database import Base


class Task(Base):
    __tablename__ = "tasks"


    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    modified_at = Column(DateTime(timezone=True), onupdate=func.now())
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    is_completed = Column(Boolean, default=False)
