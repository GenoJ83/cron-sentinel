def format_execution_log(run: dict) -> str:
    return f"[{run['job']}] Exit: {run['exit_code']} in {run['duration_sec']}s"
