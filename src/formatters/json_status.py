import json
def export_jobs_json(jobs: list) -> str:
    return json.dumps([j.model_dump() for j in jobs], indent=2)
