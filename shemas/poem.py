from pydantic import BaseModel

class PoemS(BaseModel):
    username: str
    name: str
    text: str
