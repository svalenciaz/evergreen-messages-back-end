from pydantic import BaseModel
from typing import Optional, Literal

class Message(BaseModel):
    _id: Optional[str]
    subject: str
    content: str
    receivers: list[str]
    sender: str
    status: Literal['sent', 'draft']
