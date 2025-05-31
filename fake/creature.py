from model.creature import Creature


_creatures = [
    Creature(
        id=1,
        name="Dragon",
        description="A large, serpent-like legendary creature that appears in the folklore of many cultures around the world.",
        country="Various",
        area="Mountains",
        aka="Wyrm, Serpent"
    ),
    Creature(
        id=2,
        name="Unicorn",
        description="A legendary horse-like creature with a single horn on its forehead.",
        country="Various",
        area="Forests",
        aka="Monoceros"
    ),
    Creature(
        id=3,
        name="Phoenix",
        description="A mythical bird that regenerates or is reborn from its ashes after dying.",
        country="Various",
        area="Deserts",
        aka="Firebird, Bennu"
    ),
]

def get_all() -> list[Creature]:
    """
    Get all creatures.
    """
    return _creatures

def get_one(id: int) -> Creature | None:
    for _creature in _creatures:
        if _creature.id == id:
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