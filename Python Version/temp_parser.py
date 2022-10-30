import sys
from commands import parse_cmd, format_cmd


class CLI:
    """
    Command structures:
        Database & Table
            Create:
                - create database_name;
                - create table_name values(options*);
            Drop:
                - drop (database | table) title;
            Use:
                - use title;
        Table
            Alter:
                - alter table table_name (table_values*);
            Select:
                - select options* from table_name (where | lambda);
            Insert:
                - insert into table_name values(options*);
            Update:
                - update title_name (set | lambda) (where | lambda);
            Delete:
                - delete from database_name (where);
        Other
            Where:
                - where var_name (=, >, <, >=, <=, !=) value
            Set:
                - set var_name = value
    """

    def __init__(self):
        self.cmds = []
        self.valid_cmds = ("create", "drop", "use", "alter", "select",
                           "insert", "update", "delete", "where", "set",
                           "exit")
        self.is_batch = False

    def prompt(self) -> [str]:
        cli_args = input("# ")
        cmd_list = []
        while True:
            if cli_args == ".exit":
                cmd_list = cli_args
                break
            if ';' in cli_args:
                if cli_args.strip(';'):
                    cmd_list.append(format_cmd(cli_args))
                break
            else:
                cmd_list.append(format_cmd(cli_args))
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
                    if ';' in cmd:
                        cmd_list.append(format_cmd(cmd))
                        batch_cmds[file].append(cmd_list)
                        cmd_list = []
                    elif cmd[:2] != '--' and cmd != '\n':
                        cmd_list.append(format_cmd(cmd))
        self.cmds = batch_cmds

    def process_cmds(self):
        if self.is_batch:
            print("processing cmds:")
            print("\tcmd_name args")
            for file in self.cmds:
                for cmds in self.cmds[file]:
                    for cmd in cmds:
                        parse_cmd(cmd)
        else:
            print("processing cmds:")
            for cmd in self.cmds:
                parse_cmd(cmd)

    def exit_cmd(self):
        if ".exit" in self.cmds:
            print("All done.")
            return True
        return False


def main():
    passed_args = sys.argv
    dbms_cli = CLI()
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
