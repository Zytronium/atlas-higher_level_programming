#!/usr/bin/python3
"""
module for task 1
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    un = argv[1]
    pw = argv[2]
    db = argv[3]

    d = MySQLdb.connect(host="localhost", user=un, passwd=pw, db=db, port=3306)
    cursor = d.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    results = cursor.fetchall()
    for state in results:
        print(state)

    cursor.close()
    d.close()
