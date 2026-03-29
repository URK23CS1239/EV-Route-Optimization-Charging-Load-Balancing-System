# 🚀 Deploy to Render - Complete Guide

This guide will help you deploy the EV Route Optimization & Charging Load Balancing System to Render for free!

## 📋 Prerequisites

1. **GitHub Account** - You already have this ✅
2. **Render Account** - Create at https://render.com (Free tier available)
3. **GitHub Repository** - Already pushed ✅
   - Link: `https://github.com/URK23CS1239/EV-Route-Optimization-Charging-Load-Balancing-System`

## 🔑 Step 1: Create Render Account

1. Visit **https://render.com**
2. Click **"Sign up"** button
3. Choose **"Sign up with GitHub"** (easier!)
4. Authorize Render to access your GitHub account
5. Complete signup

## 🔗 Step 2: Connect GitHub Repository

1. Log in to **Render Dashboard** (https://dashboard.render.com)
2. Click **"New +"** button → Select **"Web Service"**
3. Click **"Connect a repository"**
4. Search for: `EV-Route-Optimization-Charging-Load-Balancing-System`
5. Click **"Connect"** next to your repository

## ⚙️ Step 3: Configure Web Service

After connecting, you'll see the deployment form. Fill in:

### Basic Information
| Field | Value |
|-------|-------|
| **Name** | `ev-route-optimization` |
| **Environment** | `Python 3` |
| **Region** | `Oregon` (US) or `Frankfurt` (EU) |
| **Branch** | `main` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `cd EV_Project && gunicorn --workers 2 --worker-class sync --bind 0.0.0.0:$PORT app:app` |

### Environment Variables
Click **"Add Environment Variable"** and add:

```
PYTHON_VERSION = 3.9.0
FLASK_ENV = production
DEBUG = false
```

### Plan
- Select **"Free"** tier (good for testing/development)
  - Free tier includes 750 hours/month (enough for 24/7 operation)
  - Sleeps after 15 minutes of inactivity (spins up when accessed)

## 🚀 Step 4: Deploy

1. Click **"Create Web Service"** button
2. **Wait for build to complete** (2-3 minutes)
   - You'll see logs scrolling
   - Look for: `successfully deployed` message

3. **Copy your deployment URL**
   - Format: `https://ev-route-optimization.onrender.com`
   - This is your live app URL!

## ✅ Step 5: Verify Deployment

1. Visit your Render URL in browser
2. You should see the EV Route Optimization dashboard
3. Test functionality:
   - Enter locations (e.g., "Coimbatore" → "Tirunelveli")
   - Check map loads
   - Adjust battery slider
   - Click "Plan Route"
   - Watch stations load

## 🔄 Step 6: Auto-Deploy on GitHub Updates (Optional)

When you push changes to GitHub, Render automatically redeploys:

1. Make changes locally
2. Commit and push:
   ```bash
   git add .
   git commit -m "Update: description of changes"
   git push origin main
   ```
3. Render automatically rebuilds and deploys (check logs on Render dashboard)

## 📊 Monitoring & Logs

### View Deployment Logs
1. Go to your **Web Service** on Render
2. Click **"Logs"** tab
3. See real-time application logs

### Check Status
- **"Live"** badge = Service is running ✅
- **"Building"** = Currently deploying
- **"Failed"** = Check logs for errors

## 🐛 Troubleshooting

### "Build Failed"
- **Check logs** for error message
- **Verify `requirements.txt`** has all dependencies
- **Check Start Command** syntax

### "Application Error on Page"
- Visit Render logs to see error
- Common issues:
  - Port binding issue (Render sets `$PORT` environment variable)
  - Missing environment variable
  - Import error in Python

### "Map Not Loading"
- Check browser console (F12 → Console tab)
- Nominatim/OSRM APIs should load fine (free services)
- Leaflet CDN should load from jsDelivr

### "Station Data Not Loading"
- `/get-stations` endpoint should work
- Check `logic.py` is accessible
- Verify Flask app can find routes

## 🔐 Environment Variables (Optional)

If you add Firebase, create `.env` file locally:

```
FIREBASE_KEY=your_key_here
```

Then in Render:
1. Go to Web Service settings
2. Add environment variable:
   - Key: `FIREBASE_KEY`
   - Value: `your_key_value`

## 📱 Share Your App

Your live URL:
```
https://ev-route-optimization.onrender.com
```

Share this link with anyone to demo the app!

## 💰 Cost (Free Tier)

- **Free Web Service**: $0/month
  - 750 hours included
  - Auto-spins down after 15 min inactivity
  - Auto-spins up on next request
  - Perfect for demo/learning

- **Paid tiers** available if you need:
  - Guaranteed uptime
  - Priority support
  - More resources

## 🔄 Redeploying

To manually redeploy (if needed):

1. Go to your Web Service on Render
2. Click **"Manual Deploy"** → **"Deploy latest commit"**
3. Wait for redeploy (2-3 minutes)

## 📝 Common Next Steps

After deployment, you might want to:

1. **Add custom domain**
   - Go to Web Service settings
   - Click "Add Custom Domain"
   - Configure DNS (optional)

2. **Scale up** (if needed)
   - Switch to paid plan for guaranteed uptime
   - Add more worker processes

3. **Database** (if adding persistence)
   - Add PostgreSQL database service
   - Connect to Flask app

4. **Email notifications**
   - Set up alerts for deployment failures

## 🎉 Congratulations!

Your EV Route Optimization system is now **live on the internet**! 🚀

**Next Step**: Share the URL and start collecting feedback!

---

## Support & Issues

If you encounter issues:

1. **Check Render Logs** (Web Service → Logs)
2. **Check Browser Console** (F12 → Console)
3. **Verify GitHub push** was successful
4. **Test locally first** (python app.py)

## Additional Resources

- **Render Docs**: https://render.com/docs
- **Flask Production**: https://flask.palletsprojects.com/en/2.3.x/deploying/
- **Gunicorn Docs**: https://docs.gunicorn.org/
