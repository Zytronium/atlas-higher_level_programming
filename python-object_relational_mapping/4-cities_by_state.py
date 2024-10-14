#!/usr/bin/python3
"""
module for task 4
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    un = argv[1]
    pw = argv[2]
    db = argv[3]

    d = MySQLdb.connect(host="localhost", user=un, passwd=pw, db=db, port=3306)
    csr = d.cursor()
    csr.execute(
        "SELECT cities.id, cities.name, states.name "
        + "FROM cities JOIN states ON cities.state_id = states.id "
        + "ORDER BY cities.id ASC;"
    )
    results = csr.fetchall()
    for state in results:
        print(state)

    csr.close()
    d.close()
