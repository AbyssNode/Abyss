# orbit_index.py

def calculate_orbit_index(token_history):
    """
    Scores how 'cyclical' a token behaves based on bounce frequency and range.
    """
    bounces = token_history.get("bounce_events", 0)
    avg_range = token_history.get("avg_range", 0)
    score = (bounces * avg_range) / 10
    return round(score, 2)
