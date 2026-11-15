def send_discord_alert(job_name: str, reason: str):
    print(f'[DISCORD ALERT] Cron job {job_name} failed: {reason}')
