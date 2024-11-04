#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

def states(username, userPassword, database_name):
    """
    Connects to a MySQL database and executes a query to retrieve all states.
    Results are sorted in ascending order by states.id.
    """

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=userPassword,
                         db=database_name)

    # Create a cursor object
    cur = db.cursor()

    # Execute the query to select all states ordered by states.id
    cur.execute("SELECT * FROM states ORDER BY states.id")

    # Fetch all results from the executed query
    rows = cur.fetchall()

    # Print each row in the fetched results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()

if __name__ == "__main__":
    # Take command line arguments for username, password, and database name
    user = sys.argv[1]
    passw = sys.argv[2]
    bd = sys.argv[3]

    # Call the states function with the provided arguments
    states(user, passw, bd)