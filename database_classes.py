import os
import sys


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db_path = "./" + db_name
        self.tables = {}

    def create_table(self, table_name, *values):

        table_path = self.db_path + '/' + table_name
        try:
            open(table_path, "x")
            self.tables[table_name] = table_path
            # TODO: Implement values into table model
            success = "Table " + table_name + " created."
            print(success)
        except FileExistsError as _:
            if table_name not in self.tables:
                self.tables[table_name] = table_path
            error = "!Failed to create table " + table_name \
                    + " because it already exists."
            print(error)

    def drop_table(self, table_name):
        try:
            os.remove(self.tables[table_name])
            self.tables.pop(table_name)
            success = "Table " + table_name + " deleted."
            print(success)
        except (KeyError, FileNotFoundError):
            error_msg = "!Failed to delete table " + table_name + " because it does not exist."
            print(error_msg)

    def update_table(self):
        pass

    def query_table(self):
        pass

    def does_table_exist(self, table_name: str) -> bool:
        return table_name in self.tables

    def get_db_path(self) -> str:
        return self.db_path

    def get_table_path(self, table_name: str) -> str:
        return self.tables[table_name]


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
        except (KeyError, FileNotFoundError):
            error_msg = "!Failed to delete database " + db_name + " because it does not exist."
            print(error_msg)
        except OSError:
            error_msg = "!Failed to delete database " + db_name + " because it is not empty."
            print(error_msg)

    def get_curr_db(self):
        return self.curr_db


# test = DatabaseManager()
# test.create_database("t1")
# test.set_curr_db("t1")
# test.curr_db.create_table("test.txt")
# test.curr_db.drop_table("test.txt")
# test.drop_database("t1")
