# gravity_watcher.py

def detect_gravitational_pull(tokens):
    """
    Flags tokens that are pulling liquidity from other ecosystems rapidly.
    """
    flagged = []
    for token in tokens:
        inflow = token.get("cross_chain_inflow", 0)
        outflow = token.get("native_chain_outflow", 0)
        if inflow > (outflow * 1.5):
            flagged.append(token["symbol"])
    return flagged
