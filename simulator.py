# simulator.py
# Simulates IoT sensor data for the PlastoFuel system

import threading
import random
import time

_latest = {
    "temperature": 0,
    "pressure": 0,
    "mass_input": 0,
    "mass_output": 0,
    "energy_used": 0
}

_running = False

def _simulate():
    """Background thread to generate fake sensor readings."""
    global _latest, _running
    _running = True

    while _running:
        _latest = {
            "temperature": round(random.uniform(380, 520), 2),
            "pressure": round(random.uniform(1.0, 3.5), 2),
            "mass_input": round(random.uniform(1.0, 10.0), 2),
            "mass_output": round(random.uniform(0.4, 8.0), 2),
            "energy_used": round(random.uniform(2.0, 10.0), 2)
        }
        time.sleep(2)

def start_simulation():
    """Start the IoT simulation in a background thread."""
    thread = threading.Thread(target=_simulate, daemon=True)
    thread.start()

def get_latest_reading():
    """Return the latest simulated sensor readings."""
    return _latest
