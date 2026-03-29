from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from functools import wraps
import requests
import json
import os
from datetime import datetime

# Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials, auth, firestore

# Set up Flask with correct template and static paths
# Get the parent directory (project root)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')

app = Flask(__name__, 
    template_folder=template_dir,
    static_folder=static_dir)

# Use environment variable for secret key in production, fallback to default for development
app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key_change_this_in_production')

# ========== FIREBASE SETUP ==========
# Download your Firebase service account JSON from Firebase Console
# Place it in the project root as 'serviceAccountKey.json'
try:
    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    print("✅ Firebase initialized successfully")
except Exception as e:
    print(f"⚠️ Firebase not configured (optional): {e}")
    db = None

# ========== HELPER FUNCTIONS ==========
# Hardcoded coordinates for common cities (fallback)
CITY_COORDINATES = {
    'coimbatore': [76.9969, 11.0066],
    'hosur': [77.8317, 12.7383],
    'salem': [78.1437, 11.4668],
    'erode': [77.7599, 11.3410],
    'tiruppur': [77.3411, 11.1085],
    'krishnagiri': [79.1307, 12.5158],
    'bangalore': [77.5946, 12.9716],
    'bengaluru': [77.5946, 12.9716],
    'chennai': [80.2707, 13.0827],
    'madras': [80.2707, 13.0827],
    'vellore': [79.1325, 12.9689],
    'kodai': [77.4691, 10.2381],
    'ooty': [76.7114, 11.4102],
    'madurai': [78.1197, 9.9252],
    'trichy': [78.7597, 10.7905],
    'tiruchirappalli': [78.7597, 10.7905],
    'kanyakumari': [77.5470, 8.0883],
    'nagercoil': [77.4268, 8.1833],
    'tirunelveli': [77.7134, 8.7139],
    'nellore': [79.9865, 14.4426],
    'tirupati': [79.4192, 13.1939],
    'vizag': [83.3185, 17.6869],
    'visakhapatnam': [83.3185, 17.6869],
    'hyderabad': [78.4711, 17.3850],
    'pune': [73.8355, 18.5204],
    'mumbai': [72.8479, 19.0760],
    'delhi': [77.1025, 28.7041],
    'goa': [73.8278, 15.2993],
    'kochi': [76.2673, 9.9312],
    'cochin': [76.2673, 9.9312],
    'thrissur': [76.2144, 10.5276],
    'kannur': [75.3704, 12.1816],
    'calicut': [75.7804, 11.2588],
    'kozhikode': [75.7804, 11.2588],
    'mysore': [75.3704, 12.2958],
    'mysuru': [75.3704, 12.2958],
    'belgaum': [75.6270, 15.8497],
    'belagavi': [75.6270, 15.8497],
    'dharwad': [75.0060, 15.4589],
    'davangere': [75.9064, 14.4667],
    'raichur': [77.3564, 16.2118],
    'gulbarga': [77.3386, 17.3373],
    'kalaburagi': [77.3386, 17.3383],
}

def get_coordinates_from_text(place_name):
    """Convert place name to coordinates - tries hardcoded first, then Nominatim API"""
    try:
        # Check if city is in our hardcoded list
        city_lower = place_name.lower().strip()
        for city_key, coords in CITY_COORDINATES.items():
            if city_key in city_lower or city_lower in city_key or city_key in city_lower.split():
                print(f"✅ Found {city_key}: {coords}")
                return coords
        
        # If not found in hardcoded list, try Nominatim API
        print(f"🔍 Searching Nominatim for: {place_name}")
        url = "https://nominatim.openstreetmap.org/search"
        headers = {'User-Agent': 'EVRouteOptimizer/1.0'}
        params = {
            'q': f"{place_name}, India",
            'format': 'json',
            'limit': 1,
            'countrycodes': 'in',
            'timeout': 10
        }
        
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        if data and len(data) > 0:
            lat = float(data[0]['lat'])
            lon = float(data[0]['lon'])
            print(f"✅ Found {place_name} via Nominatim: [{lon}, {lat}]")
            return [lon, lat]
        else:
            print(f"❌ Nominatim found no results for: {place_name}")
            return None
        
    except requests.exceptions.Timeout:
        print(f"⏱️ Nominatim timeout for {place_name}")
        return None
    except Exception as e:
        print(f"❌ Error finding coordinates for {place_name}: {e}")
        return None

# ========== MAIN ROUTES ==========
@app.route('/')
def index():
    return render_template('index.html', user="Guest")

@app.route('/get-stations', methods=['GET'])
def get_stations():
    """Get all EV charging stations"""
    from logic import get_all_stations
    stations = get_all_stations()
    return jsonify(stations)

@app.route('/search-place', methods=['POST'])
def search_place():
    """Search for places using Nominatim"""
    query = request.json['query']
    coords = get_coordinates_from_text(query)
    if coords:
        return jsonify({'success': True, 'coords': coords, 'place': query})
    return jsonify({'success': False, 'error': 'Place not found'})

@app.route('/route', methods=['POST'])
def route():
    start = request.form.get('start', '').strip()
    end = request.form.get('end', '').strip()
    battery = int(request.form.get('battery', 80))
    
    print(f"\n📍 Route Request: {start} → {end} (Battery: {battery}%)")
    
    # Get coordinates
    start_coords = get_coordinates_from_text(start)
    end_coords = get_coordinates_from_text(end)
    
    print(f"Start Coords: {start_coords}, End Coords: {end_coords}")
    
    if not start_coords:
        return render_template('index.html', 
            result=f"❌ Could not find starting location: {start}",
            user="Guest")
    
    if not end_coords:
        return render_template('index.html', 
            result=f"❌ Could not find destination: {end}",
            user="Guest")

    try:
        # Get route from OSRM (Open Source Routing Machine) - Free, no authentication needed
        url = f"https://router.project-osrm.org/route/v1/driving/{start_coords[0]},{start_coords[1]};{end_coords[0]},{end_coords[1]}"
        params = {
            'overview': 'full',
            'steps': 'true',
            'geometries': 'geojson'
        }
        
        print(f"🔄 Calling OSRM Route Service: {start_coords} → {end_coords}")
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data['code'] != 'Ok' or not data['routes']:
            print(f"⚠️ OSRM Response: {data['code']}")
            return render_template('index.html',
                result="❌ No route found between locations",
                user="Guest")
        
        # Extract coordinates from OSRM geometry
        route_geometry = data['routes'][0]['geometry']
        route = [[coord[1], coord[0]] for coord in route_geometry['coordinates']]
        
        print(f"✅ Route found with {len(route)} waypoints")
        
        # Find best charging station if battery is low
        from logic import select_best_station, update_station
        best = None
        result = "✅ Direct route - Battery sufficient"
        if battery < 30:
            best = select_best_station()
            if best:
                update_station(best)
                result = f"⚡ CHARGING REQUIRED - Recommended Station: {best['name']}"
        
        # Save to database (optional)
        if db:
            try:
                db.collection('routes').add({
                    'start': start,
                    'end': end,
                    'battery': battery,
                    'route': route,
                    'station': best['name'] if best else None,
                    'timestamp': datetime.now()
                })
            except Exception as e:
                print(f"⚠️ Could not save to Firebase: {e}")
        
        return render_template('index.html',
            result=result,
            route=route,
            best_station=best['name'] if best else "",
            user="Guest"
        )
    
    except requests.exceptions.Timeout:
        return render_template('index.html',
            result="❌ Route service timeout - Please try again",
            user="Guest")
    except Exception as e:
        print(f"❌ Error: {e}")
        return render_template('index.html',
            result=f"❌ Could not calculate route: {str(e)[:50]}",
            user="Guest")

@app.route('/get-location', methods=['POST'])
def get_location():
    """Store user's current GPS location"""
    data = request.json
    lat, lon = data.get('lat'), data.get('lon')
    
    if db:
        try:
            db.collection('locations').add({
                'lat': lat,
                'lon': lon,
                'timestamp': datetime.now()
            })
        except:
            pass  # Continue even if Firebase save fails
    
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, port=5000)