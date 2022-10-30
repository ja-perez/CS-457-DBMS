import database_classes as db_c


def parse_cmd(cmd: [str]):
    cmd_name = cmd[0]
    args = cmd[1:]
    print("\t", cmd_name, args, '\n')
    match cmd_name:
        case "create":
            create_cmd(args)
        case "drop":
            drop_cmd(args)
        case "use":
            use_cmd(args)
        case "alter":
            alter_cmd(args)
        case "select":
            select_cmd(args)
        case "insert":
            insert_cmd(args)
        case "update":
            update_cmd(args)
        case "delete":
            delete_cmd(args)


def format_cmd(cmds):
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


def create_cmd(args: [str]):
    pass


def drop_cmd(args: [str]):
    pass


def use_cmd(args: [str]):
    pass


def alter_cmd(args: [str]):
    pass


def select_cmd(args: [str]):
    pass


def insert_cmd(args: [str]):
    pass


def update_cmd(args: [str]):
    pass


def delete_cmd(args: [str]):
    pass


def where_cmd(args: [str]):
    pass


def set_cmd(args: [str]):
    pass
