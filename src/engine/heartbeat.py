import time
def record_heartbeat(job_name: str) -> dict:
    return {'job': job_name, 'timestamp': int(time.time()), 'status': 'OK'}
