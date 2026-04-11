#!/usr/bin/python3
"""
izah

"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    """
    izah
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                ORDER BY states.id ASC")
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)