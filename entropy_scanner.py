# entropy_scanner.py

import math

def shannon_entropy(distribution):
    """
    distribution: dict like {"addrA": 10, "addrB": 5, ...}
    """
    total = sum(distribution.values()) or 1
    entropy = 0.0
    for v in distribution.values():
        p = v / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def flow_entropy(transfers):
    """
    transfers: [{"to":"0x..","amount":...}, ...]
    Returns entropy over destination distribution.
    """
    dist = {}
    for t in transfers:
        dist[t["to"]] = dist.get(t["to"], 0) + t["amount"]
    return shannon_entropy(dist)
