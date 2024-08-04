import MySQLdb
import sys

def main():
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    mysql_username, mysql_password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", user=mysql_username, passwd=mysql_password, db=database_name)
        cursor = db.cursor()

        # Execute the query to retrieve states starting with 'N'
        cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        # Fetch and display the results
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Close the database connection
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
