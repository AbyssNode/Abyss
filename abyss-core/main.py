# abyss-core/main.py

"""
Abyss Core — Entry Point

This is the main launcher for the Abyss AI engine.
"""

from engine.deep_scan import run_deep_scan
from engine.whale_tracker import run_whale_tracking

def main():
    print("🌊 Abyss AI Engine Starting...")
    
    # Run token discovery scan
    run_deep_scan()
    
    # Run whale tracking logic
    run_whale_tracking()

    print("Abyss AI tasks complete.")

if __name__ == "__main__":
    main()
