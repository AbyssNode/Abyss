# signal_hub.py

class SignalHub:
    """
    Centralized routing system for AI-generated signals.
    All modules send alerts here to unify output.
    """

    def __init__(self):
        self.signals = []

    def push_signal(self, signal_type, message, metadata=None):
        self.signals.append({
            'type': signal_type,
            'message': message,
            'meta': metadata or {}
        })

    def get_all(self):
        return self.signals
