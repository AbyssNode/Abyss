# quorum_filter.py

def confirm_with_quorum(signal_candidates, min_sources=2):
    """
    Groups signals by token and type, confirming only those seen by >= min_sources.
    signal_candidates: [{"token":"ABC","type":"whale","source":"dexA"}, ...]
    """
    bucket = {}
    for s in signal_candidates:
        key = (s["token"], s["type"])
        bucket.setdefault(key, set()).add(s["source"])

    confirmed = []
    for (token, stype), sources in bucket.items():
        if len(sources) >= min_sources:
            confirmed.append({"token": token, "type": stype, "sources": sorted(list(sources))})
    return confirmed
