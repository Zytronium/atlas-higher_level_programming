#!/usr/bin/python3
"""
module for task 2
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
        "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC".format(
            st_nm))
    results = csr.fetchall()
    for state in results:
        print(state)

    csr.close()
    d.close()
