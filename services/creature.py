from model.creature import Creature
import fake.creature as data

from typing import Optional

def get_all() -> list[Creature]:
    """
    Get all creatures.
    """
    return data.get_all()

def get(name: str) -> Optional[Creature]:
    """
    Get a creature by name.
    """
    return data.get(name)

def create(creature: Creature) -> Creature:
    """
    Add a new creature.
    """
    return data.create(creature)

def replace(id, creature: Creature) -> Creature:
    """
    Replace an existing creature.
    """
    return data.replace(id, creature)

def modify(id, creature: Creature) -> Creature:
    """
    Update an existing creature.
    """
    return data.modify(id, creature)

def delete(id, creature: Creature) -> bool:
    """
    Delete a creature by ID.
    """
    return data.delete(id)