from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username : Optional[str] = None
    is_superuser : bool = False

class UserCreate(UserBase):
    password: str

class User(UserCreate):
    id : Optional[int] = None
