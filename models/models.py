from sqlalchemy import Column, DateTime, Float, Integer, String, func
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    balance = Column(Float, default=0)
    registration_time = Column(DateTime, default=func.now())