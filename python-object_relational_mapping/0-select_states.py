#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv
"""Connects to a MySQL database and lists all states in the 'states' table
   in ascending order by id.
   Usage: ./0-select_states.py <username> <password> <database_name>
"""

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()