from pydantic import BaseModel, EmailStr
from typing import Optional, List

# fields for user
class UserBase(BaseModel):
    name: str
    age: int
    gender: str
    email: EmailStr  # ensures email validation
    city: str
    interests: str

# for creating users
class UserCreate(UserBase):
    pass

# for updating users
class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    email: Optional[EmailStr] = None
    city: Optional[str] = None
    interests: Optional[str] = None

# for returning users data
class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

# for returning users matchmaking
class MatchResponse(BaseModel):
    user: UserResponse
    matches: List[UserResponse]