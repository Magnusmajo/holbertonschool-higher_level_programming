import sys
import MySQLdb

#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""



if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    [print(state) for state in c.fetchall()]

    c.close()
    db.close()