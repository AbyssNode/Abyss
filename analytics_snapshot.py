# analytics_snapshot.py

import datetime

def create_snapshot(tokens):
    timestamp = datetime.datetime.utcnow().isoformat()
    return {
        "timestamp": timestamp,
        "snapshot": tokens
    }
