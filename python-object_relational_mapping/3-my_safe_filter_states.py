#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    
    query = "SELECT * FROM states WHERE name LIKE BINARY %s \
             ORDER BY states.id ASC"
    
    cursor.execute(query, (sys.argv[4],))

    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
