from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Literal

class Message(BaseModel):
    _id: Optional[str]
    subject: str
    content: str
    receivers: list[str]
    sender: str
    status: Optional[Literal['sent', 'draft']]
    send_date: Optional[datetime]
    creation_date: Optional[datetime]
