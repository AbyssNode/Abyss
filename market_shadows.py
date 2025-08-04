# market_shadows.py

def track_shadow_activity(transaction_logs):
    """
    Identifies off-chain trades or hidden trades using off-exchange behavior patterns.
    """
    shadow_activities = []
    for log in transaction_logs:
        if log["status"] == "off-chain" and log["amount"] > 10000:
            shadow_activities.append(log)
    return shadow_activities
