import os
from pathlib import Path
from sqlite3 import Connection, connect, Cursor, IntegrityError


conn: Connection | None = None
curs: Cursor | None = None

def get_db(name: str | None = None, reset: bool = False):
    global conn, curs
    print("Connection status........................:", conn)
    print("reset...................................:", reset)
    if conn:
        if not reset:
            return
        conn = None
    
    if not name:
        name = os.getenv("CRYPTID_SQLITE_DB")
        top_dir = Path(__file__).resolve().parents[1]
        print("top_dir::::::::::::::::::::", top_dir)
        db_dir = top_dir / "db"
        print("db_dir...................= ", db_dir)
        db_name = "cryptid.db"
        db_path = str(db_dir / db_name)
        print("db_path", db_path)
        name = os.getenv("CRYPTID_SQLITE_DB", db_path)
        print("Final DB name:", name)
    
    conn = connect(name, check_same_thread=False)
    curs = conn.cursor()
    
get_db()