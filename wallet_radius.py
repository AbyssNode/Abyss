# wallet_radius.py

def compute_radius(wallet_activity):
    """
    Calculates wallet's radius of influence based on transaction spread.
    """
    tx_count = wallet_activity["tx_count"]
    chain_spread = len(wallet_activity.get("chains", []))
    diversity = len(set(wallet_activity["token_ids"]))

    radius = round((tx_count * 0.5 + diversity * 0.8) * chain_spread, 2)
    return {
        "wallet": wallet_activity["address"],
        "radius_score": radius
    }
