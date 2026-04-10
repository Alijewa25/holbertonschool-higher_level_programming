#!/usr/bin/python3
"""İzah"""
import MySQLdb
import sys

if __name__ == "__main__":
    """izah"""
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    """İzah"""
    for row in rows:
        print(row)
cursor.close()
conn.close()