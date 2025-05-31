from fastapi import APIRouter

# import fake.creature as service
import services.creature as service
from model.creature import Creature, CreateCreature


router = APIRouter(prefix="/creature", tags=["creature"])


@router.get("/")
async def get_all() -> list[Creature]:
    """
    Get all creatures.
    """
    return service.get_all()


@router.post("/")
async def create(creature: CreateCreature) -> Creature:
    """
    Create creature
    """
    return service.create(creature)