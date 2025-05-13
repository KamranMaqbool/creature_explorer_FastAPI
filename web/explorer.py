from fastapi import APIRouter

import fake.explorer as service
from model.explorer import Explorer


router = APIRouter(prefix="/explorer", tags=["explorer"])


@router.get("/")
async def get_all() -> list[Explorer]:
    """
    Get all explorers.
    """
    return service.get_all()