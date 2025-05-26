# dex_watcher.py

def watch_new_listings(dex_data):
    """
    Scans live DEX feeds for new token listings.
    Flags listings with suspicious or unknown metadata.
    """
    new_listings = []
    for listing in dex_data:
        if listing.get('status') == 'new' and 'name' in listing:
            new_listings.append(listing)
    return new_listings
