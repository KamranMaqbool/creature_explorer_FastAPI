from model.creature import Creature, CreateCreature
# get fake data currently commented out
# import fake.creature as data

import data.creature as data

from typing import Optional

def get_all() -> list[Creature]:
    """
    Get all creatures.
    """
    return data.get_all()

def get(id: int) -> Optional[Creature]:
    """
    Get a creature by id.
    """
    return data.get_one(id)

def create(creature: CreateCreature) -> Creature:
    """
    Add a new creature.
    """
    return data.create(creature)

def replace(id, creature: Creature) -> Creature:
    """
    Replace an existing creature.
    """
    return data.modify(id, creature)

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