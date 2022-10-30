class CommandManager:
    """
    Command structures:
        Database & Table
            Create:
                - create database database_name;
                - create table table_name values(options*);
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

    def __init__(self, dbms):
        self.dbms = dbms
        self.troubleshooting = False

    def parse_cmd(self, cmd: [str]):
        cmd_name = cmd[0]
        args = cmd[1:]
        if self.troubleshooting:
            print("\t", cmd_name, args)
        match cmd_name:
            case "create":
                self.create_cmd(args)
            case "drop":
                self.drop_cmd(args)
            case "use":
                self.use_cmd(args[0])
            case "alter":
                self.alter_cmd(args)
            case "select":
                self.select_cmd(args)
            case "insert":
                self.insert_cmd(args)
            case "update":
                self.update_cmd(args)
            case "delete":
                self.delete_cmd(args)
            case _:
                print("!Error: Command not recognized")
        if self.troubleshooting:
            print()

    def format_cmd(self, cmds):
        updated_cmds = []
        strip_chars1 = '(\n;,'
        strip_chars2 = '()\n;,'
        split_cmds = cmds.split()
        for i, cmd in enumerate(split_cmds):
            if 'values' in cmd:
                args = cmd.split("(")
                split_cmds[i] = args[0]
                split_cmds.insert(i + 1, args[1])
        for cmd in split_cmds:
            if "(" in cmd and "))" in cmd:
                cmd = cmd.replace("))", ")")
                stripped_cmd = cmd.strip(strip_chars1)
            else:
                stripped_cmd = cmd.strip(strip_chars2)
            lowered_cmds = stripped_cmd.lower()
            updated_cmds.append(lowered_cmds)
        return updated_cmds

    def create_cmd(self, args: [str]):
        type_arg = args[0]
        name_arg = args[1]
        values = args[2:]
        if self.troubleshooting:
            print("\tCreate:", type_arg, name_arg, values)
        match type_arg:
            case "database":
                self.dbms.create_database(name_arg)
            case "table":
                self.dbms.curr_db.create_table(name_arg, values)

    def drop_cmd(self, args: [str]):
        type_arg = args[0]
        name_arg = args[1]
        if self.troubleshooting:
            print("\tDrop:", type_arg, name_arg)
        match type_arg:
            case "database":
                self.dbms.drop_database(name_arg)
            case "table":
                self.dbms.curr_db.drop_table(name_arg)

    def use_cmd(self, arg: str):
        if self.troubleshooting:
            print("\tUse:", arg)
        self.dbms.set_curr_db(arg)

    def alter_cmd(self, args: [str]):
        type_arg = args[0]
        name_arg = args[1]
        function_arg = args[2]
        values = args[3:]
        if self.troubleshooting:
            print("\tAlter:", type_arg, name_arg, function_arg, values)
        match type_arg:
            case "table":
                self.dbms.curr_db.update_table(name_arg, values)
            case _:
                print("!Error: cannot alter ", type_arg, "'s")

    def select_cmd(self, args: [str]):
        from_index = args.index("from")
        values_arg = args[:from_index]
        from_src = args[from_index + 1]
        if self.troubleshooting:
            print("\tSelect:", values_arg, from_src)
        # TODO: update to work for select being its own command separate from 'from','where' commands
        if values_arg[0] == "*":
            self.dbms.curr_db.query_table(from_src, values_arg[0])
        else:
            self.dbms.curr_db.query_table(from_src, values_arg)

    def insert_cmd(self, args: [str]):
        if self.troubleshooting:
            print("\tInsert:", args)
        pass

    def update_cmd(self, args: [str]):
        if self.troubleshooting:
            print("\tUpdate:", args)
        pass

    def delete_cmd(self, args: [str]):
        if self.troubleshooting:
            print("\tDelete", args)
        pass

    def where_cmd(self, args: [str]):
        if self.troubleshooting:
            print("\tWhere:", args)
        pass

    def set_cmd(self, args: [str]):
        if self.troubleshooting:
            print("\tSet:", args)
        pass
