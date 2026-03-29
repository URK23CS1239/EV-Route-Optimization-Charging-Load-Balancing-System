import random
from datetime import datetime

# EV Charging stations across Tamil Nadu and Karnataka
stations = [
    # Coimbatore area
    {"name": "Station A - Coimbatore Center", "coords": [11.0066, 76.9969]},
    {"name": "Station B - Coimbatore North", "coords": [11.0265, 77.0084]},
    
    # Hosur area
    {"name": "Station C - Hosur Main", "coords": [12.7383, 77.8317]},
    {"name": "Station D - Hosur Highway", "coords": [12.7450, 77.8400]},
    
    # Salem area
    {"name": "Station E - Salem Center", "coords": [11.4668, 78.1437]},
    {"name": "Station F - Salem West", "coords": [11.4580, 78.1200]},
    
    # Erode area
    {"name": "Station G - Erode", "coords": [11.3410, 77.7599]},
    
    # Tiruppur area
    {"name": "Station H - Tiruppur", "coords": [11.1085, 77.3411]},
    
    # Krishnagiri area
    {"name": "Station I - Krishnagiri", "coords": [12.5158, 79.1307]},
]

def generate_dynamic_data():
    for s in stations:
        s["slots"] = random.randint(0, 5)
        s["load"] = random.randint(20, 100)
        s["last_updated"] = datetime.now()
    return stations

def select_best_station():
    """Select the best charging station based on availability and load"""
    best = None
    best_score = float('inf')

    for s in stations:
        # Priority: available slots, then low load
        score = s["load"] - s["slots"] * 10
        if score < best_score:
            best_score = score
            best = s

    return best

def update_station(station):
    """Update station availability when a vehicle arrives"""
    if station and "slots" in station:
        station["slots"] = max(0, station["slots"] - 1)  # One slot taken
        station["last_updated"] = datetime.now()
    
    return station

def get_all_stations():
    """Get all available charging stations with current data"""
    generate_dynamic_data()
    return stations

def calculate_charging_time(battery_level, target_level=100):
    """Calculate estimated charging time in minutes"""
    # Assuming standard charger adds 20% per 30 mins
    percentage_needed = target_level - battery_level
    time_per_percent = 1.5  # minutes per percentage
    return int(percentage_needed * time_per_percent)