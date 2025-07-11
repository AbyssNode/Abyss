# silent_wave.py

def detect_silent_waves(wallet_logs):
    """
    Identifies wallets making frequent but low-value moves under radar.
    """
    silent = []
    for wallet in wallet_logs:
        if wallet["tx_count"] > 10 and wallet["avg_value"] < 50:
            silent.append(wallet["address"])
    return silent
