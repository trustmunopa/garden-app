import sqlite3

import pandas as pd


def crops(conn):
    return pd.read_sql_query("SELECT crop FROM bed ORDER BY crop", conn)["crop"]


def history(conn, crop):
    return pd.read_sql_query(
        """
        SELECT l.log_date, l.status
        FROM bed_log l
        JOIN bed b ON b.bed_id = l.bed_id
        WHERE b.crop = ?
        ORDER BY l.log_date
        """,
        conn,
        params=(crop,),
    )


def orphan_count(conn):
    return pd.read_sql_query(
        "SELECT COUNT(*) AS n FROM bed_log WHERE bed_id NOT IN (SELECT bed_id FROM bed)",
        conn,
    )["n"][0]


def add_visit(conn, crop, visit_date, status):
    conn.execute(
        "INSERT INTO bed_log (bed_id, log_date, status) "
        "SELECT bed_id, ?, ? FROM bed WHERE crop = ?",
        (str(visit_date), status, crop),
    )
    conn.commit()


def fix_crop(conn, old, new):
    conn.execute("UPDATE bed SET crop = ? WHERE crop = ?", (new, old))
    conn.commit()


def remove_bed(conn, crop):
    # True if the bed was removed, False if it still has logs
    try:
        conn.execute("DELETE FROM bed WHERE crop = ?", (crop,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        conn.rollback()
        return False
