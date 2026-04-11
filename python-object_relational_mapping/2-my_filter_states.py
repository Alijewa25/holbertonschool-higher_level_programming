#!/usr/bin/python3
"""
izah var burda ele tesevvur edin
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="Localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".format(sys.argv[4]))
    states = c.fetchall()
    for state in states:
        print(state)
    c.close()
    db.close()