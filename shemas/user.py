from pydantic import BaseModel, EmailStr

class UserS(BaseModel):
    username: str
    email: EmailStr
    password: str
