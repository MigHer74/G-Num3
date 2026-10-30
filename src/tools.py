from pathlib import Path
import database as db


def database_exists():
    dbFolder = "D:/DBA/SQLite/G-Num3/"
    dbFile = "gnum3.db"

    if not Path(dbFolder).is_dir():
        Path.mkdir(dbFolder)

    if not Path(dbFolder + dbFile).is_file():
        db.create_table()
