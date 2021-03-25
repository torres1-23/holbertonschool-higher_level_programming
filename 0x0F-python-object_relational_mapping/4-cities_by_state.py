#!/usr/bin/python3

"""This module takes in an argument and displays all values.

Usage:
    Takes 3 arguments: 'mysql username', 'mysql password' 'database name'
    and lists all states from a table in a database using MYSQLdb module.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name"
                   "  FROM cities"
                   "  INNER JOIN states"
                   "    ON cities.state_id = states.id"
                   "  ORDER BY cities.id")
    for row in cursor.fetchall():
        print(row)
