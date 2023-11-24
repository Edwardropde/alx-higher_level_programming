#!/usr/bin/python3
"""
Lists states with name beginning with N from database `hbtn_0e_0_usa`
"""

import sys
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access database and get states
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
