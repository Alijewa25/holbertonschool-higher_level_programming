kkk#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Arqumentləri birbaşa indekslə götürürük:
    # sys.argv = username
    # sys.argv = password
    # sys.argv = database name
    
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv,
        passwd=sys.argv,
        db=sys.argv
    )

    cursor = db.cursor()
    
    # Sorğunu icra edirik
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Nəticələri götürürük
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    # Bağlantıları bağlayırıq
    cursor.close()
    db.close()
