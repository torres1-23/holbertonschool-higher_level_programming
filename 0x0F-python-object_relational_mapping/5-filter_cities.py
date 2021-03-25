#!/usr/bin/python3

"""This module takes in arguments and displays all cities of a given state
from a database.

Usage:
    Takes 4 arguments: 'mysql username', 'mysql password' 'database name'
    and 'state name' and lists all cities of the 'state name'
    from a table in a database using MYSQLdb module.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    myList = []
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name"
                   "  FROM cities"
                   "  INNER JOIN states"
                   "    ON cities.state_id = states.id"
                   "  WHERE states.name = %s"
                   "  ORDER BY cities.id", (sys.argv[4], ))
    for row in cursor.fetchall():
        myList.append(row[0])
    print(', '.join(myList))
