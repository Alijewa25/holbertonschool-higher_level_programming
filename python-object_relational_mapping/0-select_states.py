#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Vacib: İndeksləri DƏQİQ belə yazmalısan
    # sys.argv -> username (məs: root)
    # sys.argv -> password (məs: root)
    # sys.argv -> database (məs: hbtn_0e_0_usa)

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv,     # Burada olmalıdır
        passwd=sys.argv,   # Burada olmalıdır (Səndə səhv buradadır)
        db=sys.argv        # Burada olmalıdır
    )

    cursor = db.cursor()
    
    # İD-yə görə artan sırada sıralayırıq
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    # Bağlantıları təmiz bağlayırıq
    cursor.close()
    db.close()
