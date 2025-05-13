from model.creature import Creature


_creatures = [
    Creature(
        name="Dragon",
        description="A large, serpent-like legendary creature that appears in the folklore of many cultures around the world.",
        country="Various"
    ),
    Creature(
        name="Unicorn",
        description="A legendary horse-like creature with a single horn on its forehead.",
        country="Various"
    ),
    Creature(
        name="Phoenix",
        description="A mythical bird that regenerates or is reborn from its ashes after dying.",
        country="Various"
    ),
]

def get_all() -> list[Creature]:
    """
    Get all creatures.
    """
    return _creatures

def get(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

def create(creature: Creature) -> Creature:
    """
    Add a new creature.
    """
    return creature

def modify(id, creature: Creature) -> Creature:
    """
    Replace an existing creature.
    """
    return creature

def replace(id, creature: Creature) -> Creature:
    """
    Update an existing creature.
    """
    return creature
def delete(id) -> bool:
    """
    Delete a creature.
    """
    return False