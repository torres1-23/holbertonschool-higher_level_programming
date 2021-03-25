#!/usr/bin/python3

"""This module list all states from a database.

Usage:
    Takes 3 arguments: 'mysql username', 'mysql password' and 'database name'
    and lists all states from a table in a database using MYSQLdb module.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    for row in cursor.fetchall():
        print(row)
