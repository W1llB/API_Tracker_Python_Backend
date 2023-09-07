from pydantic import BaseModel
from datetime import datetime


class APIBase(BaseModel):
    name: str
    endpoint_url: str | None = None
    docs_url: str | None = None
    tags: str | None = None
    status: bool = False
    response_code: int | None = None
    last_downtime: datetime | None = None

class APICreate(APIBase):
    pass

class API(APIBase):
    api_id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str | None = None


class UserCreate(UserBase):
    user_id: int


class User(UserBase):
    id: int
    apis: list[API] = []

    class Config:
        orm_mode = True
