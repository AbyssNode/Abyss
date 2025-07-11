# depth_probe.py

def run_probe(depth=3):
    """
    Simulates layered scans into unexplored token zones.
    Depth controls how far off-mainstream the engine scans.
    """
    results = []
    for layer in range(1, depth + 1):
        results.append(f"Scanning layer {layer}... anomalies: {layer * 2}")
    return results

if __name__ == "__main__":
    print("\n".join(run_probe()))
