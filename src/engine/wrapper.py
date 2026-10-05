import subprocess, time
def wrap_command(name: str, cmd: list):
    t0 = time.time()
    res = subprocess.run(cmd, capture_output=True, text=True)
    duration = time.time() - t0
    return {'job': name, 'exit_code': res.returncode, 'duration_sec': round(duration, 2)}
