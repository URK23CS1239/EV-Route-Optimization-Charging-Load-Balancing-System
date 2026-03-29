# ⚡ EV Route Planner with Firebase

A modern web application for Electric Vehicle (EV) owners to plan optimal routes, find nearby charging stations, and track their journey in real-time.

## 🌟 Features

### 🔐 Authentication System
- **User Registration**: Create a new account with email and password
- **Login System**: Secure session-based authentication
- **User Dashboard**: Personalized experience for each user

### 📍 Live GPS Location
- **Current Location Detection**: One-click access to your real-time GPS coordinates
- **Location Tracking**: Automatically save your location to Firebase
- **Map Display**: Visual representation on an interactive map

### 🔍 Real Place Search
- **Autocomplete Search**: Search for any location worldwide
- **Multiple Suggestions**: Get location suggestions as you type
- **Coordinate Resolution**: Convert place names to GPS coordinates

### 🗺️ Smart Route Planning
- **Route Optimization**: Calculate optimal driving routes
- **Distance & Time**: See estimated journey details
- **Real-time Vehicle Movement**: Animated vehicle marker showing route progression

### ⚡ Intelligent Charging System
- **Battery Level Indicator**: Visual slider for current battery percentage
- **Smart Station Selection**: Automatically recommends the best charging station
- **Availability Tracking**: Real-time charging station availability
- **Charging Time Estimates**: Calculate how long you'll need to charge

### 💾 Firebase Database
- **User Profiles**: Secure user data storage
- **Route History**: Keep track of all your journeys
- **Location History**: Access your location history
- **Cloud Backup**: All data backed up in Firebase Firestore

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip
- Firebase account (https://firebase.google.com)

### Installation

1. **Clone/Download the project**
```bash
cd EV_Project
```

2. **Create a virtual environment** (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup Firebase** (See [FIREBASE_SETUP.md](FIREBASE_SETUP.md))
   - Create Firebase project
   - Download service account key
   - Save as `serviceAccountKey.json` in project root

5. **Update Flask secret key**
   Edit `app.py` and change:
   ```python
   app.secret_key = 'your_secret_key_change_this'
   ```

6. **Run the application**
```bash
python -m flask run
# or
python EV_Project/app.py
```

7. **Open in browser**
```
http://localhost:5000
```

## 📁 Project Structure

```
EV_Project/
├── EV_Project/
│   └── app.py                 # Main Flask application
├── templates/
│   ├── login.html             # Login page
│   ├── register.html          # Registration page
│   └── index.html             # Main app interface
├── static/
│   └── style.css              # Styling (if needed)
├── logic.py                   # Business logic & station selection
├── requirements.txt           # Python dependencies
├── FIREBASE_SETUP.md          # Firebase configuration guide
├── README.md                  # This file
└── .gitignore                 # Git ignore rules
```

## 🔄 Application Flow

```
1. User visits http://localhost:5000
   ↓
2. Redirected to login page (if not authenticated)
   ↓
3. User registers or logs in
   ↓
4. Redirected to main dashboard
   ↓
5. User can:
   - Enter start and end locations
   - Click GPS button to auto-fill current location
   - Adjust battery level
   - Click "Plan Route"
   ↓
6. App calculates route and recommends charging station if needed
   ↓
7. Route is displayed on map with animated vehicle
   ↓
8. Data is saved to Firebase for future reference
```

## 🔑 API Endpoints

### Authentication
- `POST /register` - Create new user account
- `POST /login` - Login existing user
- `GET /logout` - Logout current user

### Main Application
- `GET /` - Main dashboard (requires login)
- `POST /route` - Calculate route and find charging station
- `POST /search-place` - Search for a location
- `POST /get-location` - Save current GPS location

## 🗂️ Database Structure

### Firestore Collections

#### Users Collection
```
/users/{uid}
├── email: string
├── created_at: timestamp
└── last_location: object
    ├── lat: number
    ├── lon: number
    └── timestamp: timestamp
```

#### Routes Collection
```
/routes/{document_id}
├── user_id: string
├── start: string
├── end: string
├── battery: number
├── route: array (coordinates)
├── station: string
└── timestamp: timestamp
```

## 🎨 UI Features

### Responsive Design
- Works on desktop, tablet, and mobile
- Side panel for input controls
- Full-screen interactive map

### Interactive Map
- Zoom and pan controls
- Marker for user location
- Polyline showing the route
- Animated vehicle movement

### Modern Interface
- Gradient color scheme (purple to blue)
- Smooth transitions and animations
- Clear visual feedback
- Mobile-friendly layout

## 🔒 Security

- Firebase Authentication for user management
- Secure session handling
- Firestore security rules for data protection
- HTTP-only cookies
- CSRF protection

## 🌐 External APIs Used

1. **Firebase** - Authentication & Database
2. **OpenRouteService** - Route calculation
3. **OpenStreetMap/Nominatim** - Place geocoding
4. **Leaflet** - Interactive maps

## 📊 Charging Station Logic

The app recommends charging stations based on:
- **Load**: Current station load percentage
- **Available Slots**: Number of free charging points
- **Score Calculation**: `load - (slots × 10)`
- **Selection**: Station with lowest score wins

## 🛠️ Troubleshooting

### Location not working?
- Check browser permissions for geolocation
- Ensure HTTPS or localhost (geolocation requires secure context)
- Check browser console for errors

### Firebase errors?
- Verify service account key is in correct location
- Check Firebase Console for API enablement
- Review error messages in Flask console

### Route not calculating?
- Ensure location names are valid
- Check OpenRouteService API is accessible
- Verify coordinates are being returned

## 📝 Configuration

### Change Default Location
Edit `index.html` line with `map.setView()`:
```javascript
var map = L.map('map').setView([28.6139, 77.2090], 12);
// Change [28.6139, 77.2090] to your default coordinates
```

### Update API Keys
- OpenRouteService: Replace API key in `app.py`
- Firebase: Replace with your service account key

## 🚀 Future Enhancements

- [ ] Real-time traffic integration
- [ ] Multi-language support
- [ ] Vehicle type selection (battery capacity)
- [ ] Social features (sharing routes)
- [ ] Payment integration for charging
- [ ] Real charging station API integration
- [ ] Push notifications
- [ ] Advanced analytics

## 📞 Support

For issues or questions:
1. Check [FIREBASE_SETUP.md](FIREBASE_SETUP.md)
2. Review error messages in browser console
3. Check Flask console for backend errors
4. Verify all files are in correct locations

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Developer Notes

- Uses Flask as web framework
- Leaflet.js for mapping
- Firebase for backend services
- OpenRouteService for route optimization
- Responsive design with CSS Grid

---

**Made with ⚡ for EV enthusiasts**
