from pydantic import BaseModel, EmailStr, Field, constr

class User(BaseModel):
    name: constr(min_length=2, max_length=20)
    email: EmailStr
    balance: float