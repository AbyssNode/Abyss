# pulse_sync.py

def sync_pulses(signal_logs):
    """
    Aligns cross-chain signal timing to detect synchronized events.
    """
    synced = []
    for signal in signal_logs:
        if abs(signal["eth_timestamp"] - signal["bsc_timestamp"]) < 3:
            synced.append(signal["token"])
    return list(set(synced))
