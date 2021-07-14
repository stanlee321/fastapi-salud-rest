
from pydantic import BaseModel

from typing import List

class PageDataIn(BaseModel):
    table_as_str:str
    index:int

class PageDataOut(BaseModel):
    index:int

class LoggDataIn(BaseModel):
    kind:str
    index:int
    text:str

class LoggDataOut(BaseModel):
    index:int


class UserData(BaseModel):
    ci : str
    birth_date: str

class CreateQueueIn(BaseModel):
    
    data: List[UserData]
