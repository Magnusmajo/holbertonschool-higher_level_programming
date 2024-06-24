#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Getting command line arguments
    def states(username, password, db_name):
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=db_name)
        
        # Creat a cursor object
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
