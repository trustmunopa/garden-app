import sqlite3
from pathlib import Path

DB = Path("garden.db")  
# This is a Path object for keeping track of a file loc in a os-independent way.

SCHEMA = """
    CREATE TABLE bed (
        bed_id   INTEGER PRIMARY KEY,
        crop     TEXT NOT NULL,
        location TEXT
    );
    CREATE TABLE bed_log (
        log_id   INTEGER PRIMARY KEY,
        bed_id   INTEGER NOT NULL REFERENCES bed(bed_id),
        log_date TEXT,
        status   TEXT
    );
    INSERT INTO bed VALUES
        (1, 'kale', 'upper garden'),
        (2, 'garlic', 'hoop house'),
        (3, 'tomatoes', 'lower garden');
    INSERT INTO bed_log (bed_id, log_date, status) VALUES
        (1, '2026-09-01', 'seeded'),
        (1, '2026-09-20', 'sprouting'),
        (2, '2026-09-05', 'seeded');
"""


def connect():
    # Build the database the first time (or after a restart wipes it)
    if not DB.exists():  # calls the exists() method on the Path instance
        build = sqlite3.connect(DB)
        build.executescript(SCHEMA)
        build.commit()
        build.close()
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def reset():
    DB.unlink(missing_ok=True)
