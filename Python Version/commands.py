def parse_cmd(cmd_name: str, args: [str]):
    match cmd_name:
        case "create":
            create_cmd(args)


def create_cmd(args: [str]):
    pass


def drop_cmd():
    pass


def use_cmd():
    pass


def alter_cmd():
    pass


def select_cmd():
    pass


def insert_cmd():
    pass


def update_cmd():
    pass


def delete_cmd():
    pass


def where_cmd():
    pass


def set_cmd():
    pass


def format_cmd(cmds):
    updated_cmds = []
    strip_chars1 = '(\n;'
    strip_chars2 = '()\n;'
    split_cmds = cmds.split()
    for cmd in split_cmds:
        if "(" in cmd and "))" in cmd:
            cmd = cmd.replace("))", ")")
            stripped_cmd = cmd.strip(strip_chars1)
        else:
            stripped_cmd = cmd.strip(strip_chars2)
        lowered_cmds = stripped_cmd.lower()
        updated_cmds.append(lowered_cmds)
    return updated_cmds