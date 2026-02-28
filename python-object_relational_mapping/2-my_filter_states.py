#!/usr/bin/python3
"""
This script filters states by user input.
"""

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
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC".format(sys.argv[4])
    cur.execute(query)

    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No states found")

    cur.close()
    db.close()
