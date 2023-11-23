#!/usr/bin/python3
"""
SHows all cities of a particular state from state tableof database
Safe from SQL injections
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `cities` as `c` \
            INNER JOIN `states` as `s` \
                ON `c`.`state_id` = `s`.`id` \
            ORDER BY `c`.`id`")
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
