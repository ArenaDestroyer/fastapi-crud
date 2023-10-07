from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    name: str
    balance: float
    registration_time: datetime