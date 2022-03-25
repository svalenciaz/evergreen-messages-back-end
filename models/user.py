from datetime import datetime
from pydantic import BaseModel
from typing import Literal, Optional

class User(BaseModel):
    _id: Optional[str]
    name: str
    gender: Literal['male', 'female', 'other']
    email: str
    number: Optional[str]
    birth_date: datetime
    sender: bool
    receiver: bool
