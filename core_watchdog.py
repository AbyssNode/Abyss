# core_watchdog.py

import time

def monitor_engine(status_callback):
    """
    Monitors the main Abyss engine every 10s and logs heartbeat.
    """
    while True:
        status = status_callback()
        print(f"[WATCHDOG] Engine Status: {status}")
        time.sleep(10)

# Example callback:
# def get_status(): return "OK"
