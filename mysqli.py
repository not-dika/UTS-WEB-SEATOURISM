import pymysql
from pymysql import MySQLError

class MySQLInterface:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def _connect(self):
        """Establish a connection to the MySQL database."""
        if self.connection is None:
            try:
                self.connection = pymysql.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                    cursorclass=pymysql.cursors.DictCursor
                )
                print("Successfully connected to the database")
            except MySQLError as e:
                print(f"Error: {e}")
                self.connection = None

    def _disconnect(self):
        """Close the connection to the MySQL database."""
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Connection closed")

    def execute_query(self, query, params=None):
        """Execute a single query."""
        self._connect()  # Ensure connection is established
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
                print("Query executed successfully")
        except MySQLError as e:
            print(f"Error: {e}")
        finally:
            self._disconnect()  # Close the connection after executing the query

    def fetch_all(self, query, params=None):
        """Fetch all results from a query."""
        self._connect()  # Ensure connection is established
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                results = cursor.fetchall()
                return results
        except MySQLError as e:
            print(f"Error: {e}")
            return None
        finally:
            self._disconnect()  # Close the connection after fetching results

    def fetch_one(self, query, params=None):
        """Fetch a single result from a query."""
        self._connect()  # Ensure connection is established
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                result = cursor.fetchone()
                return result
        except MySQLError as e:
            print(f"Error: {e}")
            return None
        finally:
            self._disconnect()  # Close the connection after fetching results