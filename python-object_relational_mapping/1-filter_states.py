#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to the database
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()

    # Obtain states starting 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    states = cursor.fetchall()

    # Show the result
    for state in states:
        print(state)

    # Close connection
    cursor.close()
    db.close()
