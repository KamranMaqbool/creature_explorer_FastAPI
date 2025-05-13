from model.creature import Creature
from services import creature as code

sample = Creature(
    name="Dragon",
    description="A large, serpent-like legendary creature that appears in the folklore of many cultures around the world.",
    country="Various"
)


def test_create():
    resp = code.create(sample)
    assert resp == sample


def test_get_exist():
    resp = code.get("Dragon")
    assert resp == sample
    

def test_get_missing():
    resp = code.get("Missing")
    assert resp is None
