from model.explorer import Explorer, CreateExplorer
# import fake.explorer as data
import data.explorer as data

from typing import Optional


def get_all() -> list[Explorer]:
    """
    Get all explorers.
    """
    return data.get_all()

def get(id: int) -> Optional[Explorer]:
    """
    Get an explorer by name.
    """
    return data.get_one(id)

def create(explorer: CreateExplorer) -> Explorer:
    """
    Add a new explorer.
    """
    return data.create(explorer)

def modify(id, explorer: Explorer) -> Explorer:
    """
    Replace an existing explorer.
    """
    return data.modify(id, explorer)

def replace(id, explorer: Explorer) -> Explorer:
    """
    Update an existing explorer.
    """
    return data.modify(id, explorer)

def delete(id, explorer: Explorer) -> bool:
    """
    Delete an explorer by ID.
    """
    return data.delete(id)
