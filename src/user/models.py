from sqlalchemy import Column, String, Integer,DateTime, Boolean
from src.utils.db import Base

class UserModel(Base):
    __tablename__ = "user_table"

    id = Column(Integer,primary_key=True)
    username = Column(String,nullable=False)
    name = Column(String)
    hashed_password = Column(String, nullable=False)
    email = Column(String)