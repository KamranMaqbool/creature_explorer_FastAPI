from .init import conn, curs
from model.creature import Creature, CreateCreature


curs.execute("""CREATE TABLE IF NOT EXISTS creature (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                country TEXT,
                area TEXT,
                aka TEXT)""")

def row_to_model(row: tuple) -> Creature:
    (id, name, description, country, area, aka) = row
    return Creature(id=id, name=name, description=description, country=country, area=area, aka=aka)

from typing import Union

def model_to_dict(creature: Creature | CreateCreature) -> dict:
    return creature.model_dump() if creature else {}

def get_one(id: int) -> Creature | None:
    qry = "SELECT * FROM creature WHERE id=:id"
    curs.execute(qry, {"id": id})
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    return None

def get_all() -> list[Creature]:
    qry = "SELECT * FROM creature"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(creature: CreateCreature) -> Creature:
    qry  = """INSERT INTO creature (name, description, country, area, aka)
             VALUES (:name, :description, :country, :area, :aka)"""
    curs.execute(qry, model_to_dict(creature))
    creature_obj = get_one(curs.lastrowid)
    if creature_obj is None:
        raise ValueError("Failed to create creature: not found after insert.")
    return creature_obj

def modify(id: int, creature: Creature) -> Creature:
    qry = """UPDATE creature
            SET name=:name, description=:description, country=:country, area=:area, aka=:aka
            WHERE id=:id"""
    data = model_to_dict(creature)
    data["id"] = id
    curs.execute(qry, data)
    if curs.rowcount == 0:
        raise ValueError(f"Creature with id {id} not found for update.")
    creature_obj = get_one(id)
    if creature_obj is None:
        raise ValueError(f"Creature with id {id} not found after update.")
    return creature_obj

def delete(id: int) -> bool:
    qry = "DELETE FROM creature WHERE id=:id"
    res = curs.execute(qry, {"id": id})
    return bool(res)
