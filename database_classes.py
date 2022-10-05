import os
import sys


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.tables = set()

    def create_table(self, table_name):
        if table_name not in self.tables:
            self.tables.add(table_name)
            os.system("cd ..")
            # Sys command to create file with table name
            success = "Table " + table_name + " create."
            return success
        else:
            error = "!Failed to create table " + table_name \
                    + " because it already exists."
            return error

    def drop_table(self):
        pass

    def update_table(self):
        pass

    def query_table(self):
        pass


class DatabaseManager:
    def __init__(self):
        # Active database
        self.curr_db = None

    def create_database(self):
        pass

    def drop_database(self):
        pass

    def change_curr_db(self, dest_db: str):
        # Linux command to exit current database directory
        # Linux command to enter dest db directory if exists
        pass

test = Database("test")
test.create_table("t1")