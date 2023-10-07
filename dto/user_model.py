from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    name: str
    balance: int
    registration_time: datetime