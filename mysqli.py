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
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Connection closed")

    def execute_query(self, query, params=None):
        self._connect()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
                print("Query executed successfully")
        except MySQLError as e:
            print(f"Error: {e}")
        finally:
            self._disconnect()

    def fetch_all(self, query, params=None):
        self._connect()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                results = cursor.fetchall()
                return results
        except MySQLError as e:
            print(f"Error: {e}")
            return None
        finally:
            self._disconnect()

    def fetch_one(self, query, params=None):
        self._connect()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                result = cursor.fetchone()
                return result
        except MySQLError as e:
            print(f"Error: {e}")
            return None
        finally:
            self._disconnect()