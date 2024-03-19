#!/usr/bin/python3
#Lists all states from the database hbtn_0e_0_usa

import MySQLdb
import sys

if __name__ == "__main__":
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_0_usa", charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
    except MySQLdb._exceptions.OperationalError as e:
        print("OperationalError:", e)
        cur.close()
        conn.close()
