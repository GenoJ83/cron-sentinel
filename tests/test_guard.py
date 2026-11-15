from src.security.command_guard import sanitize_cmd
def test_guard():
    cmd = sanitize_cmd('python script.py --arg value')
    assert len(cmd) == 4
