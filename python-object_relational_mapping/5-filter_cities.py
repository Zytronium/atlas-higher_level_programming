#!/usr/bin/python3
"""
module for task 5
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    un = argv[1]
    pw = argv[2]
    db = argv[3]
    st_nm = argv[4]

    d = MySQLdb.connect(host="localhost", user=un, passwd=pw, db=db, port=3306)
    csr = d.cursor()
    csr.execute(
        """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE BINARY states.name = %s
        ORDER BY cities.id ASC
        """, (st_nm,)
    )
    results = csr.fetchall()
    print(", ".join([city[0] for city in results]))

    csr.close()
    d.close()
