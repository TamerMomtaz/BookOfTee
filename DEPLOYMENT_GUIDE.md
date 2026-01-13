# 🌊 THE BOOK OF TEE - Deployment Guide
## Making Kahotia Live 24/7

---

## 📁 FILE STRUCTURE

```
BookOfTee/
├── kahotia_alive.html    # Frontend (the interface)
├── kahotia_brain.py      # Backend (Flask API)
├── kahotia.jpg           # Your Kahotia artwork
├── start_kahotia.bat     # Windows one-click launcher
├── requirements.txt      # Python dependencies
├── Procfile             # Deployment command
├── railway.json         # Railway config
├── render.yaml          # Render config
└── .gitignore           # Git ignore rules
```

---

## 🖥️ LOCAL SETUP (Windows)

### Option 1: Double-Click Launch
1. Copy all files to `C:\Users\Power of Tee\BookOfTee`
2. Double-click `start_kahotia.bat`
3. Browser opens automatically to Kahotia!

### Option 2: Manual Launch (if bat fails)
```cmd
# Terminal 1 - Start Brain
cd C:\Users\Power of Tee\BookOfTee
python kahotia_brain.py

# Terminal 2 - Start Interface
cd C:\Users\Power of Tee\BookOfTee
python -m http.server 8000

# Browser
http://localhost:8000/kahotia_alive.html
```

---

## ☁️ DEPLOYMENT TO RAILWAY (Recommended - Free Tier)

### Step 1: Get a NEW Claude API Key
1. Go to: https://console.anthropic.com/
2. Create new API key (your old one was exposed)
3. Copy it safely - you'll need it!

### Step 2: Push to GitHub
```bash
# Install Git if not installed
# Create GitHub account if needed

cd C:\Users\Power of Tee\BookOfTee
git init
git add .
git commit -m "Kahotia awakens"

# Create repo on GitHub.com, then:
git remote add origin https://github.com/YOUR_USERNAME/BookOfTee.git
git push -u origin main
```

### Step 3: Deploy to Railway
1. Go to: https://railway.app/
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your BookOfTee repo
5. Railway auto-detects Python!

### Step 4: Add Environment Variables
In Railway dashboard → Your project → Variables:
```
CLAUDE_API_KEY = sk-ant-api03-YOUR-NEW-KEY
SUPABASE_URL = https://pjaxznbcanpbsejrpljy.supabase.co
SUPABASE_KEY = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Step 5: Deploy Frontend
Railway serves Python, but for the HTML we have two options:

**Option A: Static Hosting on Railway**
Add a `staticFiles` folder and configure nginx (more complex)

**Option B: Use Vercel for Frontend (Easier)**
1. Go to: https://vercel.com/
2. Import your GitHub repo
3. It will serve `kahotia_alive.html`

### Step 6: Update Frontend URL
In `kahotia_alive.html`, change:
```javascript
const BACKEND_URL = 'https://your-railway-app.railway.app';
```

---

## 🚀 ALTERNATIVE: RENDER (Also Free)

### Step 1: Deploy to Render
1. Go to: https://render.com/
2. Sign in with GitHub
3. "New" → "Web Service"
4. Connect your BookOfTee repo
5. Render uses `render.yaml` automatically!

### Step 2: Add Environment Variables
In Render dashboard → Environment:
```
CLAUDE_API_KEY = sk-ant-api03-YOUR-NEW-KEY
SUPABASE_KEY = your-supabase-key
```

---

## 📱 ACCESS FROM PHONE

Once deployed, you'll get a URL like:
- Railway: `https://bookoftee-production.up.railway.app`
- Render: `https://kahotia-brain.onrender.com`

Bookmark this on your phone - Kahotia is now always with you!

---

## 🔐 SECURITY NOTES

1. **NEVER** commit API keys to GitHub
2. Your old Claude key was exposed - generate a new one
3. Use environment variables for all secrets
4. The `.gitignore` file helps prevent accidental exposure

---

## 🆘 TROUBLESHOOTING

### "Module not found"
```bash
pip install -r requirements.txt --break-system-packages
```

### "Port already in use"
```bash
# Find and kill the process
netstat -aon | findstr :5000
taskkill /PID <PID_NUMBER> /F
```

### "CORS error in browser"
The backend has CORS enabled. Make sure you're accessing via http://localhost:8000, not by opening the file directly.

### Railway says "build failed"
Check that `requirements.txt` exists and has correct format.

---

## 🎯 NEXT STEPS

After deployment:
1. [ ] Test chat on phone
2. [ ] Add more nodes to Supabase
3. [ ] Customize toll frequency
4. [ ] Add your artwork to the gallery
5. [ ] Connect more data sources

---

>> KAHOTIA IS WATCHING. NO THOUGHT IS WASTED.
