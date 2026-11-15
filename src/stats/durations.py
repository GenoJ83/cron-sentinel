import numpy as np
def summarize_durations(runs: list):
    durs = [r['duration_sec'] for r in runs if 'duration_sec' in r]
    return {'avg_duration': float(np.mean(durs))} if durs else {}
