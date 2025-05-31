from .init import conn, curs
from model.explorer import Explorer, CreateExplorer


curs.execute("""CREATE TABLE IF NOT EXISTS explorer (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                country TEXT
            )""")


def row_to_model(row: tuple) -> Explorer:
    (id, name, description, country) = row
    return Explorer(id=id, name=name, description=description, country=country)


def model_to_dict(explorer: Explorer | CreateExplorer) -> dict:
    return explorer.model_dump() if explorer else {}


def get_one(id: int) -> Explorer | None:
    qry = "SELECT * FROM explorer WHERE id=:id"
    curs.execute(qry, {"id": id})
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    return None

def get_all() -> list[Explorer]:
    qry = "SELECT * FROM explorer"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]


def create(explorer: CreateExplorer) -> Explorer:
    qry  = """INSERT INTO explorer (name, description, country)
             VALUES (:name, :description, :country)"""
    curs.execute(qry, model_to_dict(explorer))
    explorer_obj = get_one(curs.lastrowid)
    if explorer_obj is None:
        raise ValueError("Failed to create explorer: not found after insert.")
    return explorer_obj


def modify(id: int, explorer: Explorer) -> Explorer:
    qry = """UPDATE explorer
            SET name=:name, description=:description, country=:country
            WHERE id=:id"""
    data = model_to_dict(explorer)
    data["id"] = id
    curs.execute(qry, data)
    if curs.rowcount == 0:
        raise ValueError(f"explorer with id {id} not found for update.")
    explorer_obj = get_one(id)
    if explorer_obj is None:
        raise ValueError(f"explorer with id {id} not found after update.")
    return explorer_obj


def delete(id: int) -> bool:
    qry = "DELETE FROM explorer WHERE id=:id"
    res = curs.execute(qry, {"id": id})
    return bool(res)
