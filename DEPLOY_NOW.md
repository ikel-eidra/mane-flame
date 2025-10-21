# 🔥 DEPLOY MANE TO RAILWAY NOW - 3 STEPS

## Everything is ready! Just do these 3 steps:

---

## STEP 1: Create GitHub Repo (2 minutes)

### Go to: https://github.com/new

Fill in:
- **Repository name**: `mane-flame`
- **Description**: `Mane - The Flame: Autonomous AI Builder with Gemini 2.0 Flash`
- **Public** or **Private**: Your choice
- **DO NOT** check "Add README"
- Click **"Create repository"**

---

## STEP 2: Push Code to GitHub (1 minute)

Copy and paste these commands in terminal:

```bash
cd /home/ubuntu/gemini_mane
git remote add origin https://github.com/ikel-eidra/mane-flame.git
git branch -M main
git push -u origin main
```

**You'll be asked for:**
- Username: `ikel-eidra`
- Password: Use your **GitHub Personal Access Token** (not your password)
  - If you don't have one: https://github.com/settings/tokens → "Generate new token (classic)" → Check "repo" → Generate

---

## STEP 3: Deploy to Railway (2 minutes)

### A. Go to Railway Dashboard
https://railway.app/dashboard

### B. Create New Project
1. Click **"+ New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose **`ikel-eidra/mane-flame`**
4. Railway will start building automatically

### C. Add Environment Variable
1. Click on your service
2. Go to **"Variables"** tab
3. Click **"+ New Variable"**
4. Add:
   - **Name**: `GEMINI_API_KEY`
   - **Value**: `AIzaSyCZDJ1GvyaecjO8Eyked8EHYCHrTQGsYTo`
5. Click **"Add"**

### D. Generate Domain
1. Go to **"Settings"** tab
2. Scroll to **"Networking"**
3. Click **"Generate Domain"**
4. Copy your URL (like: `https://mane-flame-production.up.railway.app`)

---

## ✅ DONE!

**Your Mane is now live 24/7!**

Visit your Railway URL and start building apps!

**Cost**: $5-10/month vs $6,000/month (Manus)
**Savings**: 99.8% 🔥

---

## Files Already Ready in /home/ubuntu/gemini_mane:

✅ All code files
✅ Git repository initialized
✅ First commit done
✅ Railway configuration
✅ Requirements.txt
✅ Environment template
✅ Documentation

**Just need to push to GitHub and deploy to Railway!**

---

## If You Need Help:

**GitHub Token**: https://github.com/settings/tokens
**Railway Dashboard**: https://railway.app/dashboard

**Total time**: 5 minutes
**Total cost**: $5-10/month

**LET'S GO! 🔥**

