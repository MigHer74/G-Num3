from pathlib import Path
import src


def database_exists():
    dbFolder = "D:/DBA/SQLite/G-Num3/"
    dbFile = "gnum3.db"

    if not Path(dbFolder).is_dir():
        Path.mkdir(dbFolder)

    if not Path(dbFolder + dbFile).is_file():
        src.create_table()
        src.insert_first_values()
