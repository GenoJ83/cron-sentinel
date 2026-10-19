import shlex
def sanitize_cmd(cmd_str: str):
    return shlex.split(cmd_str)
