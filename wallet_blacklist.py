# wallet_blacklist.py

BLACKLISTED_WALLETS = {
    "0xdeadbeef1234567890abcdef1234567890abcdef",
    "0x000badwallet456789abcdef456789abcdef1111"
}

def is_blacklisted(wallet_address):
    return wallet_address.lower() in BLACKLISTED_WALLETS
