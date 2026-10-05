def filter_failing_jobs(jobs: list):
    return [j for j in jobs if j.status == 'FAILING']
