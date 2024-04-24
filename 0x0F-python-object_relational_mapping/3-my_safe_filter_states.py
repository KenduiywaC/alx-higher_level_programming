#!/usr/bin/python3
#Displays all values in the states table of hbtn_0e_0_usa.

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(sys.argv[4]))
    [print(state) for state in c.fetchall()]
