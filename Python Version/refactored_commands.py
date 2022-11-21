"""
Author: Javier Perez
Date: 11/21/22
Description:
    This file defines the classes: CLI, CommandManager
    The CLI in this case will be the only object that we explicitly call in the
    main and serves as the users guide and interface when interacting with the
    database management system(DBMS).
    The database manager in this case will be the only object that we explicitly
    call in the main and serves as the users guide and access point into the
"""


# TODO:
#   Update description ^^^ with refactored changes
#   Make parser not case-sensitive for table names
#   Update format method to accept Table_Name(values*) (only set for Table_Name (values*))
#       Idea: Split on ( -> Join -> Split on spaces -> join -> Split on ',' -> Strip ");'"
#   Update FOR parameter to include join functionality

def is_command(line):
    return line and line[:2] != "--"


class CLI:
    def __init__(self, dbms):
        self.cmds = ""
        self.cmd_manager = CommandManager(dbms)

    def prompt(self):
        cli_args = input("# ")
        curr_cmd = []
        while True:
            if ';' in cli_args or '.exit' in cli_args:
                curr_cmd.append(cli_args)
                break
            curr_cmd.append(cli_args)
            cli_args = input("  ")
        self.cmds = ' '.join(curr_cmd)
        self.parse_cmds()

    def batch_mode(self, batch_files):
        files_to_cmds = {}
        for file in batch_files:
            file_cmds = []
            with open(file, "r") as f:
                f_lines = f.readlines()
                curr_cmd = []
                for line in f_lines:
                    line = line.strip('\n')
                    if is_command(line) and (';' in line or '.exit' in line):
                        curr_cmd.append(line)
                        file_cmds.append(' '.join(curr_cmd))
                        curr_cmd = []
                    elif is_command(line):
                        curr_cmd.append(line)
            files_to_cmds[file] = file_cmds
        self.parse_cmds(files_to_cmds)

    def parse_cmds(self, batch_files=None):
        if batch_files:
            for file in batch_files:
                for cmd in batch_files[file]:
                    self.cmd_manager.process_cmd(cmd)
        else:
            self.cmd_manager.process_cmd(self.cmds)

    def is_exit(self):
        return self.cmd_manager.exit_flag


class CommandManager:
    def __init__(self, dbms):
        self.primary_cmds = ("create", "drop", "use", "select", "alter",
                             "insert", "update", "delete", "exit")
        self.dbms = dbms
        self.exit_flag = 0
        self.TS = 0

    def process_cmd(self, command):
        commands = command.split()
        primary_cmd, args = commands[0].lower(), commands[1:]
        if self.TS:
            print("processing:", command)
            print("primary command:", primary_cmd)
        match primary_cmd:
            case "create":
                self.create_cmd(args)
            case "drop":
                self.drop_cmd(args)
            case "use":
                self.use_cmd(args[0])
            case "select":
                self.select_cmd(args)
            case "alter":
                self.alter_cmd(args)
            case "insert":
                self.insert_cmd(args)
            case "update":
                self.update_cmd(args)
            case "delete":
                self.delete_cmd(args)
            case ".exit":
                self.exit_cmd()
            case _:
                print("!Error: Command not recognized")

    def create_cmd(self, args):
        pass

    def drop_cmd(self, args):
        pass

    def use_cmd(self, args):
        pass

    def select_cmd(self, args):
        pass

    def alter_cmd(self, args):
        pass

    def insert_cmd(self, args):
        pass

    def update_cmd(self, args):
        pass

    def delete_cmd(self, args):
        pass

    def exit_cmd(self):
        print("All done.")
        self.exit_flag = 1
