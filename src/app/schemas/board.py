from pydantic import BaseModel

class BoardBase(BaseModel):
    title : str
    content : str

class BoardCreate(BoardBase):
    pass

class BoardUpdate(BoardBase):
    pass

