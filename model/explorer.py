from pydantic import BaseModel


class Explorer(BaseModel):
    name: str
    description: str
    country: str
    aka: str
    area: str
