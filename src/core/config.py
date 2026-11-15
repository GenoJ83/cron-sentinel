from pydantic import BaseModel
class SentinelConfig(BaseModel):
    heartbeat_dir: str = '.heartbeats'
    grace_period_seconds: int = 300
    alert_webhook_url: str = ''
