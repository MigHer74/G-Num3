import sqlite3


def connection():
    conn = sqlite3.connect("D:/DBA/SQLite/G-Num3/GNum3.db")
    return conn


def create_table():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS games (
            game_type TEXT,
            game_week TEXT,
            game_number INT,
            game_number_1 INT,
            game_number_2 INT,
            game_number_3 INT,
            game_number_4 INT,
            game_number_5 INT,
            game_number_6 INT,
            CONSTRAINT pk_type_week_number
                PRIMARY KEY (game_type, game_week, game_number)
        );
        """
    )
    conn.commit()
    conn.close()


def insert_first_values():
    conn = connection()
    cursor = conn.cursor()

    for game_number in range(1, 7):
        cursor.execute(
            """
            INSERT INTO games (game_type, game_week, game_number,
            game_number_1, game_number_2, game_number_3, game_number_4,
            game_number_5, game_number_6)
            VALUES ('S', 'W1', ?, 0, 0, 0, 0, 0, 0);
            """,
            (game_number,)
        )

    for game_week in range(1, 7):
        game_week = f"W{game_week}"

        for game_number in range(1, 4):
            cursor.execute(
                """
                INSERT INTO games (game_type, game_week, game_number,
                game_number_1, game_number_2, game_number_3, game_number_4,
                game_number_5, game_number_6)
                VALUES ('L', ?, ?, 0, 0, 0, 0, 0, 0);
                """,
                (game_week, game_number)
            )

    conn.commit()
    conn.close()
