# Firebase Setup Guide for EV Project

## 🚀 Step-by-Step Setup

### 1. Create Firebase Project
1. Go to https://console.firebase.google.com/
2. Click "Create a project"
3. Enter project name "EV-Project"
4. Accept the terms and click "Create project"
5. Wait for the project to be created

### 2. Enable Authentication
1. In Firebase Console, go to **Build → Authentication**
2. Click "Get started"
3. Select **Email/Password** provider
4. Toggle "Enable" and click "Save"
5. Enable **User sign-up** permission

### 3. Create Firestore Database
1. Go to **Build → Firestore Database**
2. Click "Create database"
3. Select **Start in test mode** (for development)
4. Choose a location (closest to your region)
5. Click "Create"

### 4. Generate Service Account Key
1. Go to **Project Settings** (gear icon)
2. Click **Service Accounts** tab
3. Click "Generate New Private Key"
4. Save the JSON file as `serviceAccountKey.json` in your project root
5. ⚠️ **IMPORTANT**: Add this file to `.gitignore`

### 5. Enable Required APIs
1. Go to **APIs and Services** (in Cloud Console)
2. Enable these APIs:
   - Cloud Firestore API
   - Firebase Authentication API
   - Realtime Database API (optional)

### 6. Update Your Code
```python
# In app.py, verify you have:
from firebase_admin import credentials, auth, firestore

cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
```

### 7. Create Firestore Collections

#### a) Users Collection
Collection: `users`
Document structure:
```json
{
  "uid": "auto-generated",
  "email": "user@example.com",
  "created_at": "timestamp",
  "last_location": {
    "lat": 28.6139,
    "lon": 77.2090,
    "timestamp": "timestamp"
  },
  "routes": []
}
```

#### b) Routes Collection
Collection: `routes`
Document structure:
```json
{
  "user_id": "user_uid",
  "start": "Starting Location",
  "end": "Destination",
  "battery": 80,
  "route": [[lat, lon], ...],
  "station": "Station Name (if charging required)",
  "timestamp": "timestamp"
}
```

### 8. Install Dependencies
```bash
pip install -r requirements.txt
```

### 9. Run the Application
```bash
python -m flask run
# or
python app.py
```

The app will be available at `http://localhost:5000`

## 🔒 Security Rules

### Firestore Security Rules
Go to **Build → Firestore Database → Rules** and paste:

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Users can only read/write their own data
    match /users/{userId} {
      allow read, write: if request.auth.uid == userId;
    }
    
    // Routes: read/write your own routes
    match /routes/{document=**} {
      allow read, write: if request.auth.uid == resource.data.user_id;
      allow create: if request.auth.uid == request.resource.data.user_id;
    }
  }
}
```

## 🔑 Environment Variables (Optional)
Create a `.env` file:
```
FLASK_SECRET_KEY=your_secret_key_here
OPENROUTE_API_KEY=your_api_key
GOOGLE_PLACES_API_KEY=your_api_key
```

## 🚨 Troubleshooting

### Firebase not initializing?
- Check if `serviceAccountKey.json` exists in project root
- Verify all required APIs are enabled in Cloud Console
- Check console for specific error messages

### Authentication not working?
- Ensure Email/Password provider is enabled
- Check that your code is creating users correctly
- Verify Firestore rules allow authentication

### Location not saving?
- Check browser's geolocation permissions
- Verify Firebase is properly initialized
- Check Firestore rules for `/users` and `/routes` collections

## 📱 Features Implemented

✅ **User Authentication**
- Email/password registration
- Login system
- Session management
- Logout functionality

✅ **Live GPS Location**
- Real-time geolocation capture
- Location storage in Firebase
- Map display with user marker

✅ **Place Search**
- Real-world place search using Nominatim
- Route planning with OpenRouteService
- Suggestions dropdown

✅ **Database Integration**
- Firebase Firestore for user data
- Route history storage
- Location tracking
- Station availability

✅ **Smart Charging**
- Battery level indicator
- Automatic charging station recommendation
- Station availability tracking

## 📚 Useful Resources
- https://firebase.google.com/docs
- https://firebase.google.com/docs/auth
- https://firebase.google.com/docs/firestore
- https://firebase-admin-py.readthedocs.io/
