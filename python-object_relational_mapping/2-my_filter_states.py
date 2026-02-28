#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa that match the user input."""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = '{}' ".format(sys.argv[4])
    query += "ORDER BY id ASC"
    cur.execute(query)

    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)

    cur.close()
    db.close()
