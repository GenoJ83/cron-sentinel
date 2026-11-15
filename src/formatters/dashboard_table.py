def format_job_table(jobs: list) -> str:
    return '\n'.join(f'{j.name} | {j.schedule} | {j.status}' for j in jobs)
