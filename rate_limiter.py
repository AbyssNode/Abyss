# rate_limiter.py
import time

class RateLimiter:
    def __init__(self, delay=1.0):
        self.delay = delay
        self.last_call = 0

    def wait(self):
        now = time.time()
        elapsed = now - self.last_call
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)
        self.last_call = time.time()
