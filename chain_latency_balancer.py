# chain_latency_balancer.py

import time

class LatencyBalancer:
    """
    Rotates through chain RPC endpoints and backs off on slow responders.
    """

    def __init__(self, endpoints):
        # endpoints: [{"name": "eth", "url": "...", "latency": 0.0}, ...]
        self.endpoints = endpoints

    def record_latency(self, name, latency):
        for ep in self.endpoints:
            if ep["name"] == name:
                ep["latency"] = 0.7 * ep.get("latency", latency) + 0.3 * latency
                break

    def pick_endpoint(self):
        # Choose the lowest-latency endpoint
        return min(self.endpoints, key=lambda e: e.get("latency", 1e9))

    def backoff(self, name, seconds=2):
        time.sleep(seconds)
        self.record_latency(name, (self._get(name).get("latency", 1.0) + seconds))

    def _get(self, name):
        return next(ep for ep in self.endpoints if ep["name"] == name)
