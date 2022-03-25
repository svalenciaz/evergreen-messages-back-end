from pydantic import BaseModel
from typing import Optional

class Template(BaseModel):
    _id: Optional[str]
    name: str
    subject: str
    content: str
