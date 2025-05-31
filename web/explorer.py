from fastapi import APIRouter

# import fake.explorer as service
import services.explorer as service
from model.explorer import Explorer, CreateExplorer


router = APIRouter(prefix="/explorer", tags=["explorer"])


@router.get("/")
async def get_all() -> list[Explorer]:
    """
    Get all explorers.
    """
    return service.get_all()


@router.post("/")
async def create(explorer: CreateExplorer) -> Explorer:
    """
    Create explorer
    """
    return service.create(explorer)
