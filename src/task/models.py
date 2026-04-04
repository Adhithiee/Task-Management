from sqlalchemy import Column, String, Integer, Boolean
from src.utils.db import Base

class TaskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer,primary_key=True)
    title = Column(String)
    desc = Column(String)
    is_completed = Column(Boolean,default = False)