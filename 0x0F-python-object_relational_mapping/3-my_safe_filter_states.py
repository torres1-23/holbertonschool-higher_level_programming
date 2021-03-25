#!/usr/bin/python3

"""This module takes in an argument and displays all values
where name matches the argument, safe from SQL injections.

Usage:
    Takes 4 arguments: 'mysql username', 'mysql password' 'database name'
    and 'state name searched' and lists all states from a table in a database
    using MYSQLdb module.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT *"
                   "  FROM states"
                   "  WHERE name = %s"
                   "  ORDER BY states.id", (sys.argv[4], ))
    for row in cursor.fetchall():
        print(row)
