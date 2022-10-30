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
from commands import CommandManager


class CLI:
    def __init__(self, dbms):
        self.cmds = []
        self.valid_cmds = ("create", "drop", "use", "alter", "select",
                           "insert", "update", "delete", "where", "set",
                           "exit")
        self.is_batch = False
        self.cmd_manager = CommandManager(dbms)

    def prompt(self) -> [str]:
        cli_args = input("# ")
        cmd_list = []
        while True:
            if cli_args.lower() == ".exit":
                cmd_list = cli_args.lower()
                break
            if ';' in cli_args:
                if cli_args.strip(';'):
                    cmd_list.append(self.cmd_manager.format_cmd(cli_args))
                break
            else:
                cmd_list.append(self.cmd_manager.format_cmd(cli_args))
                cli_args = input("  ")
        self.cmds = cmd_list
        return self.cmds

    def batch_input(self, file_names):
        # Assume commands are syntactically correct, not grammatically
        # (i.e. starts with a valid command, ends with a semicolon | semicolon is command delimiter
        batch_cmds = {}
        self.is_batch = True
        for file in file_names:
            with open(file, "r") as f:
                cmds = f.readlines()
                batch_cmds[file] = []
                cmd_list = []
                for cmd in cmds:
                    if cmd.lower() == ".exit\n":
                        batch_cmds[file].append(".exit")
                    if ';' in cmd:
                        cmd_list.append(self.cmd_manager.format_cmd(cmd))
                        batch_cmds[file].append(cmd_list)
                        cmd_list = []
                    elif cmd[:2] != '--' and cmd != '\n':
                        cmd_list.append(self.cmd_manager.format_cmd(cmd))
        self.cmds = batch_cmds

    def process_cmds(self):
        if self.is_batch:
            for file in self.cmds:
                for cmds in self.cmds[file]:
                    if cmds == ".exit":
                        print("All done.")
                        return
                    for cmd in cmds:
                        self.cmd_manager.parse_cmd(cmd)
        else:
            for cmd in self.cmds:
                self.cmd_manager.parse_cmd(cmd)

    def exit_cmd(self):
        if ".exit" in self.cmds:
            print("All done.")
            return True
        return False


def main():
    passed_args = sys.argv
    dbms = db_c.DatabaseManager()
    dbms_cli = CLI(dbms)
    test_files = passed_args[1:]
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
