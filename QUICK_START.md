# ⚡ EV Project - Quick Setup Guide

## 📋 What's Been Implemented

✅ **Live GPS Location**
- One-click current location detection
- Automatic location saving to Firebase
- Real-time coordinates display

✅ **Real Place Search**
- Search any location worldwide
- Autocomplete suggestions
- Coordinate auto-conversion

✅ **Firebase Database**
- User authentication & storage
- Route history tracking
- Location history records
- Firestore collections ready

✅ **Login System**
- Email/password registration
- Secure authentication
- Session management
- User-specific data storage

## 🚀 Setup in 5 Minutes

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Setup Firebase
1. Go to https://console.firebase.google.com/
2. Create a new project
3. Enable Email/Password Authentication
4. Create Firestore Database (test mode)
5. Generate service account key → Save as `serviceAccountKey.json`
6. Place the JSON file in your project root directory

**Detailed guide**: See [FIREBASE_SETUP.md](FIREBASE_SETUP.md)

### Step 3: Update Secret Key (Security)
Edit `EV_Project/app.py` line 9:
```python
app.secret_key = 'your_secret_key_change_this'
```
⚠️ Change this to a random string for production!

### Step 4: Run The App
```bash
cd EV_Project
python app.py
```
or
```bash
python -m flask run
```

### Step 5: Access the App
Open your browser: **http://localhost:5000**

## 📱 How to Use

1. **Register**: Create an account with email and password
2. **Login**: Enter your credentials
3. **Plan Route**:
   - Enter start location (or click "Use Current Location" 📍)
   - Enter destination
   - Set battery level (%)
   - Click "Plan Route"
4. **View Results**:
   - Route displayed on map
   - Charging station recommended if battery < 30%
   - Vehicle animates along the route

## 🔧 Important Files

| File | Purpose |
|------|---------|
| `EV_Project/app.py` | Main Flask app with routes |
| `templates/login.html` | Login page |
| `templates/register.html` | Registration page |
| `templates/index.html` | Main dashboard with map |
| `logic.py` | Station selection logic |
| `requirements.txt` | Python dependencies |
| `FIREBASE_SETUP.md` | Firebase configuration guide |
| `README.md` | Full documentation |

## 🎯 Key Features Explained

### 📍 GPS Location
```
Click "📍 Use Current Location" button
→ Browser asks for permission
→ Coordinates sent to Firebase
→ Blue marker appears on map
```

### 🔍 Place Search
```
Type in "Starting Location" field
→ Suggestions dropdown appears
→ Click suggestion to select
→ Coordinates auto-converted
```

### ⚡ Smart Charging
```
Move battery slider to set level
If battery < 30%:
→ Nearest charging station recommended
→ Station details shown in result box
→ Station marked on map
```

### 💾 Database Saving
```
Every route is saved to Firebase with:
- User email
- Start & destination
- Battery level
- Route coordinates
- Recommended station
```

## 🔑 Default Credentials

No default accounts exist. You must register first!

### Test Flow:
1. Click "Sign up here" on login page
2. Email: test@example.com
3. Password: Test@123
4. Login with same credentials

## 📊 Charging Stations (Demo Data)

**Current locations:**
- Station A: Bangalore area
- Station B: Bangalore area  
- Station C: Bangalore area

The app dynamically updates availability and recommends the best one!

## 🛠️ Troubleshooting

### "Firebase not configured" message?
```
✓ Make sure serviceAccountKey.json is in project root
✓ Check that Firebase project is created
✓ Verify all APIs are enabled
```

### Location button not working?
```
✓ Check browser geolocation permission
✓ HTTPS required (or localhost is okay)
✓ Allow location access in browser settings
```

### Login not working?
```
✓ Check Firebase authentication is enabled
✓ Verify Firestore is initialized
✓ Check browser console for errors
```

### Route not calculating?
```
✓ Use valid city or place names
✓ Example: "Delhi", "Mumbai", "Bangalore"
✓ Check OpenRouteService is accessible
```

## 📞 Next Steps

1. **Test the basic flow**:
   - Register → Login → Plan a route
   
2. **Check Firebase Console**:
   - Verify users are created
   - Check Firestore for route records
   - Confirm location data is saving

3. **Customize locations**:
   - Add more charging stations in `logic.py`
   - Change default map location in `templates/index.html`

4. **Add your own API keys**:
   - Replace OpenRouteService demo key with your own
   - Add Google Places API if desired

## 📚 Useful Resources

- [Firebase Documentation](https://firebase.google.com/docs)
- [OpenRouteService API](https://openrouteservice.org/)
- [Leaflet Maps](https://leafletjs.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)

## ✨ What's Next?

- [ ] Deploy to production (Heroku, Firebase Hosting, etc.)
- [ ] Add real charging station API integration
- [ ] Implement payment system
- [ ] Add mobile app
- [ ] Add real-time notifications
- [ ] Add social features

---

**Congratulations! Your EV Route Planner is ready to go! 🚗⚡**
