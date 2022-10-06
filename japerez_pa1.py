import sys
import os
import database_classes as db_c


def is_input_valid(cmds: [str]) -> bool:
    valid_functions = ["CREATE", "DROP", "SELECT", "ALTER", "USE", ".EXIT", "CASE_SENSITIVE"]
    return (";" == cmds[-1][-1] or cmds[0] == ".EXIT") and cmds[0] in valid_functions


def parse_cmd(usr_cmd: str, db_manager: db_c.DatabaseManager):
    usr_cmd = usr_cmd.split()
    cmd_function = usr_cmd[0]
    cmd_storage = usr_cmd[1]
    cmd_target = usr_cmd[2][:-1] if len(usr_cmd) == 3 else usr_cmd[1][:-1]
    match cmd_function:
        case "CREATE":
            if cmd_storage == "DATABASE":
                db_manager.create_database(cmd_target)
            elif cmd_storage == "TABLE":
                # db_manager.curr_db.create_table(cmd_target)
                pass
        case "DROP":
            if cmd_storage == "DATABASE":
                db_manager.drop_database(cmd_target)
            elif cmd_storage == "TABLE":
                db_manager.curr_db.drop_table(cmd_target)
        case "SELECT":
            pass
        case "USE":
            if cmd_storage == "DATABASE":
                db_manager.set_curr_db(cmd_target)
        case "CASE_SENSITIVE":
            db_manager.is_case_sensitive = int(cmd_target)
        case ".EXIT":
            return usr_cmd


def prompt_user(dbms) -> str:
    usr_input = input('# ')
    usr_cmds = usr_input.split()
    if not dbms.is_case_sensitive:
        if len(usr_cmds) == 1:
            usr_cmds[0] = usr_cmds[0].upper()
            usr_input = usr_cmds[0]
        else:
            usr_cmds = [cmd.upper() for cmd in usr_cmds[:-1]]
            usr_cmds.append(usr_input.split()[-1])
            usr_input = ' '.join([cmd.upper() for cmd in usr_cmds[:-1]]) + " " + usr_cmds[-1]
    return usr_input if not usr_input or is_input_valid(usr_cmds) \
        else "error"


def main():
    dbms = db_c.DatabaseManager()
    while True:
        usr_cmd = prompt_user(dbms)
        if "error" in usr_cmd:
            print("!Error: Command not recognized")
        elif ".EXIT" == usr_cmd:
            print("All done.")
            break
        elif usr_cmd:
            parse_cmd(usr_cmd, dbms)


if __name__ == "__main__":
    main()
