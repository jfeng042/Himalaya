import sqlite3

database_name = "database.sqlite"


class Database:

    def __init__(self, name):
        self._conn = sqlite3.connect(name)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def query(self, sql, params=None):
        return self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()


def create_database():  # Function: Create database if not exist

    with Database(database_name) as db:

        db.execute("CREATE TABLE IF NOT EXISTS entities (entity_id INTEGER PRIMARY KEY, "
                   "entity_name TEXT NOT NULL, "
                   "tax_form TEXT, "
                   "entity_residence TEXT)")

        db.execute("CREATE TABLE IF NOT EXISTS relationships (relationship_id INTEGER PRIMARY KEY,"
                   "owner_id INTEGER NOT NULL,"
                   "sub_id INTEGER NOT NULL, own_percentage REAL NOT NULL)")


