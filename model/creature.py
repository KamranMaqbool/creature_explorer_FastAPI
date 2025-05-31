from pydantic import BaseModel


class Creature(BaseModel):
    id: int
    name: str
    description: str
    country: str
    area: str
    aka: str
    
    
class CreateCreature(BaseModel):
    name: str
    description: str
    country: str
    area: str
    aka: str
