from pydantic import BaseModel

from model.explorer import Explorer, CreateExplorer

_explorers = [
    Explorer(
        id=1,
        name="Explorer",
        description="A person who explores an unfamiliar area.",
        country="Various",
    ),
    Explorer(
        id=2,
        name="Explorer",
        description="A person who explores an unfamiliar area.",
        country="Various",
    ),
    Explorer(
        id=3,
        name="Explorer",
        description="A person who explores an unfamiliar area.",
        country="Various",
    )
]


def get_all() -> list[Explorer]:
    """
    Get all explorers.
    """
    return _explorers

def get_one(id: int) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.id == id:
            return _explorer
    return None

def create(explorer: CreateExplorer) -> Explorer:
    """
    Add a new explorer.
    """
    return explorer
def modify(id, explorer: Explorer) -> Explorer:
    """
    Replace an existing explorer.
    """
    return explorer
def replace(id, explorer: Explorer) -> Explorer:
    """
    Update an existing explorer.
    """
    return explorer
def delete(id) -> bool:
    """
    Delete an explorer.
    """
    return False