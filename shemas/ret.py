from pydantic import BaseModel

class Returns(BaseModel):
    text: str

class Errors(BaseModel):
    error: str
    text: str