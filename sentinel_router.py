# sentinel_router.py

class SentinelRouter:
    """
    Routes high-priority signals to configured channels (webhook, console, store).
    """

    def __init__(self, channels=None):
        self.channels = channels or {"console": True, "webhook": None, "store": None}

    def route(self, signal):
        """
        signal: {"type":"anomaly","severity":1-5,"message":"...","meta":{...}}
        """
        delivered = []
        if self.channels.get("console"):
            print(f"[ALERT][{signal['type'].upper()}][{signal['severity']}] {signal['message']}")
            delivered.append("console")

        if self.channels.get("webhook"):
            # placeholder: enqueue or send via your HTTP client
            delivered.append("webhook")

        if self.channels.get("store"):
            # placeholder: persist to DB or file
            delivered.append("store")

        return delivered
