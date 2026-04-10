#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa.
The script takes 3 arguments: mysql username, password, and database name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # 1. Connect to the database using arguments from sys.argv
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv,
        passwd=sys.argv,
        db=sys.argv
    )

    # 2. Create the cursor object
    cursor = conn.cursor()

    # 3. Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # 4. Fetch the results
    rows = cursor.fetchall()

    # 5. Print the results (Indented so it knows 'rows' exists)
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
