# TODO: Update description to include separation of CLI/Command management in command file

"""
Author: Javier Perez
Date: 10/10/22
Compilation: This program was written in pycharm using Python 3.10
and may be run on any machine with this version of python installed using
the command: python3 japerez_pa2.py
    - Optionally, the program may also parse a file containing a list of commands using:
    python3 japerez_pa2.py textfile_name
Description:
    - This file defines our database management systems(DMBS) main function,
    and its associated helper functions, along with the users command line interface(CLI).
    - The main creates and manages a DatabaseManager object from the database_classes file
    and uses its methods in order to create, update, delete, and query databases and their
    respective tables.
    - Databases are organized as directories, and their tables are created as tables within
    their respective database directories. The Database Manager exists within the working
    directory in which the program is called.
    - Table entries are formatted as a string tuple in the associated table text file.
"""

import sys
import database_classes as db_c
from commands import CLI


def main():
    program_args = sys.argv
    dbms = db_c.DatabaseManager()
    dbms_cli = CLI(dbms)
    test_files = program_args[1:]
    if test_files:
        # test files passed - Batch Mode
        dbms_cli.batch_input(test_files)
        dbms_cli.process_cmds()
        pass
    else:
        while True:
            dbms_cli.prompt()
            if dbms_cli.exit_cmd():
                break
            else:
                dbms_cli.process_cmds()
                pass


if __name__ == "__main__":
    main()
