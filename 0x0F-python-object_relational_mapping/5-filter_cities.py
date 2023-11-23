#!/usr/bin/python3
"""
SHows all cities of a particular state from state tableof database
Safe from SQL injections
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    query = """
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
    """
    cursor.execute(query, (state_name,))
    result = cursor.fetchone()[0]
    if result:
        print(result)
    cursor.close()
    db.close()
