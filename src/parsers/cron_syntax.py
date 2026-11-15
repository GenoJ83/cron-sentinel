def parse_simple_cron_fields(expr: str):
    parts = expr.strip().split()
    return {'minute': parts[0], 'hour': parts[1]} if len(parts) >= 2 else {}
