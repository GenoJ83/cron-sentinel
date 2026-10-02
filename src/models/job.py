from pydantic import BaseModel
class CronJob(BaseModel):
    name: str
    schedule: str
    last_seen: int = 0
    expected_interval_sec: int = 3600
    status: str = 'HEALTHY'
