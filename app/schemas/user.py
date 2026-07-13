from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    full_name: str
    email: EmailStr
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    username: str
    role: str
    is_active: bool

    class Config:
        from_attributes = True