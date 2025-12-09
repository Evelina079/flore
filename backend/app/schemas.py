from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class BouquetOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    user_id: int
    delivery_address: str
    total_price: float

class OrderOut(BaseModel):
    id: int
    user_id: int
    total_price: float
    status: str
    class Config:
        orm_mode = True
