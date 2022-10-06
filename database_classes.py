import os
import sys


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db_path = "./" + db_name
        self.tables = set()

    def create_table(self, table_name, *values):
        try:
            open(table_name, "x")
            self.tables.add(table_name)
            success = "Table " + table_name + " created."
            return success
        except FileExistsError as _:
            error = "!Failed to create table " + table_name \
                    + " because it already exists."
            return error

    def drop_table(self, table_name):
        if self.does_table_exist(table_name):
            pass
        else:
            error_msg = "!Failed to delete table " + table_name + " because it does not exist."
            print(error_msg)

    def update_table(self):
        pass

    def query_table(self):
        pass

    def does_table_exist(self, table_name):
        return table_name in self.tables

    def get_path(self):
        return self.db_path


class DatabaseManager:
    def __init__(self):
        self.curr_db = None
        self.databases = {}

    def create_database(self, db_name):
        try:
            os.mkdir(db_name)
            self.databases[db_name] = Database(db_name)
            success = "Database " + db_name + " created."
            print(success)
        except FileExistsError as _:
            if db_name not in self.databases:
                self.databases[db_name] = Database(db_name)
            error_msg = "!Failed to create database " + db_name + " because it already exist."
            print(error_msg)

    def set_curr_db(self, dest_db: str):
        try:
            self.curr_db = self.databases[dest_db]
            success = "Using database " + dest_db
            print(success)
        except KeyError as _:
            error_msg = "!Failed to use database " + dest_db + " because it does not exist."
            print(error_msg)

    def drop_database(self, db_name):
        try:
            os.rmdir(db_name)
            self.databases.pop(db_name)
            success = "Database " + db_name + " deleted."
            print(success)
        except:
            error_msg = "!Failed to delete database " + db_name + " because it does not exist."
            print(error_msg)

    def get_curr_db(self):
        return self.curr_db


test = DatabaseManager()
test.create_database("t1")
test.set_curr_db("t1")
test.drop_database("t1")
