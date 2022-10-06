import sys
import os
import database_classes as db_c


def is_input_valid(cmd: [str]) -> bool:
    valid_functions = ["CREATE", "DROP", "SELECT", "ALTER", "USE", ".EXIT"]
    return (";" == cmd[-1][-1] or cmd[0] == ".EXIT") and cmd[0] in valid_functions


def prompt_user() -> str:
    usr_input = input('# ')
    usr_cmds = usr_input.split()
    return usr_input if is_input_valid(usr_cmds) \
        else "error"


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
        case ".EXIT":
            return usr_cmd


def main():
    dbms = db_c.DatabaseManager()
    while True:
        usr_cmd = prompt_user()
        if "error" in usr_cmd:
            print("!Error: Command not recognized")
        elif ".EXIT" == usr_cmd:
            print("All done.")
            break
        else:
            parse_cmd(usr_cmd, dbms)


if __name__ == "__main__":
    main()
