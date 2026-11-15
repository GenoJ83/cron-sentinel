import time
def is_job_overdue(last_seen: int, expected_interval: int, grace: int = 300) -> bool:
    now = int(time.time())
    return (now - last_seen) > (expected_interval + grace)
