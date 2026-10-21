import os
def fast_file_mtime(path: str) -> int:
    return int(os.path.getmtime(path)) if os.path.exists(path) else 0
