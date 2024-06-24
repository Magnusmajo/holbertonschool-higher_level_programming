#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
     db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
     
     # Create a cursor object
     cursor = db.cursor()
     
     # Execute the query
     cursor.execute("SELECT * FROM states ORDER BY id ASC")

     # Fetch all results
     results = cursor.fetchall()

     # Display results
     for row in results:
         print(row)

     # Close cursor and database connection
     cursor.close()
     db.close()
