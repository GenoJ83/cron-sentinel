from src.engine.watchdog import is_job_overdue
def test_overdue():
    assert is_job_overdue(last_seen=1000, expected_interval=3600, grace=60)
