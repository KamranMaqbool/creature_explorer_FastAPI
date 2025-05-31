from pydantic import BaseModel


class Explorer(BaseModel):
    id: int
    name: str
    description: str
    country: str


class CreateExplorer(BaseModel):
    name: str
    description: str
    country: str

