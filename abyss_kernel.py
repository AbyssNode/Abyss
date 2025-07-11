# abyss_kernel.py

from signal_hub import SignalHub
from deep_scan import detect_token_patterns

def run_kernel(token_data):
    hub = SignalHub()
    patterns = detect_token_patterns(token_data)
    for item in patterns:
        hub.push_signal("pattern", f"{item['token']} showing early signal", item)
    return hub.get_all()
