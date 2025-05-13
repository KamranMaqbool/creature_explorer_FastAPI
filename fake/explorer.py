from pydantic import BaseModel

from model.explorer import Explorer

_explorers = [
    Explorer(
        name="Explorer",
        description="A person who explores an unfamiliar area.",
        country="Various",
        aka="Adventurer",
        area="Various"
    ),
    Explorer(
        name="Explorer",
        description="A person who explores an unfamiliar area.",
        country="Various",
        aka="Adventurer",
        area="Various"
    ),
    Explorer(
        name="Explorer",
        description="A person who explores an unfamiliar area.",
        country="Various",
        aka="Adventurer",
        area="Various"
    )
]


def get_all() -> list[Explorer]:
    """
    Get all explorers.
    """
    return _explorers

def get(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None
def create(explorer: Explorer) -> Explorer:
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