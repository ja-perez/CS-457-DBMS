import sys
import os
import database_classes as db_c

def is_input_valid(cmd: [str]) -> bool:
    pass


def prompt_user() -> str:
    usr_input = input('# ')
    usr_cmds = usr_input.split()
    return usr_input if is_input_valid(usr_cmds) \
        else "error"


def parse_cmd(usr_cmd: str):
    if usr_cmd == "error":
        pass


def main():
    while True:
        usr_cmd = prompt_user()


if __name__ == "__main__":
    main()
