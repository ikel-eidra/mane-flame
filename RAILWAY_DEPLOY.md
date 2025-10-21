# 🔥 Deploy Mane to Railway - Step by Step

## Quick Deploy (5 Minutes)

### Step 1: Create GitHub Repository

```bash
cd /home/ubuntu/gemini_mane
git init
git add .
git commit -m "Initial commit: Mane - The Flame"
```

**Then push to GitHub:**
1. Go to https://github.com/new
2. Create repo named: `mane-flame`
3. Run these commands:

```bash
git remote add origin https://github.com/ikel-eidra/mane-flame.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy to Railway

1. **Go to Railway**: https://railway.app/dashboard
2. **Click**: "+ New Project"
3. **Select**: "Deploy from GitHub repo"
4. **Choose**: `ikel-eidra/mane-flame`
5. **Railway will auto-detect** Python and start building

### Step 3: Add Environment Variables

In Railway dashboard, go to your service → **Variables** tab:

**Required:**
```
GEMINI_API_KEY=AIzaSyCZDJ1GvyaecjO8Eyked8EHYCHrTQGsYTo
```

**Optional (add later):**
```
GITHUB_TOKEN=your_github_token_here
GITHUB_USERNAME=ikel-eidra
OPENAI_API_KEY=your_openai_key_here
```

### Step 4: Get Your URL

1. Go to **Settings** tab
2. Click **Generate Domain**
3. You'll get a URL like: `https://mane-flame-production.up.railway.app`

**That's it! Mane is live! 🔥**

---

## Alternative: Deploy Without GitHub (Direct Upload)

### Option A: Use Railway CLI

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Link to your project
railway link

# Deploy
cd /home/ubuntu/gemini_mane
railway up
```

### Option B: Manual Deployment

1. **Zip the project:**
```bash
cd /home/ubuntu
tar -czf mane-flame.tar.gz gemini_mane/
```

2. **Upload to Railway** via their web interface

---

## Environment Variables Explained

### GEMINI_API_KEY (Required)
Your Gemini API key from Google AI Studio
- Get it at: https://aistudio.google.com/
- Already have: `AIzaSyCZDJ1GvyaecjO8Eyked8EHYCHrTQGsYTo`

### GITHUB_TOKEN (Optional)
For GitHub integration (create repos, push code)
- Get it at: https://github.com/settings/tokens
- Scopes needed: `repo`, `workflow`

### GITHUB_USERNAME (Optional)
Your GitHub username
- Default: `ikel-eidra`

### OPENAI_API_KEY (Optional)
For image generation with DALL-E
- Get it at: https://platform.openai.com/api-keys

---

## Files Included for Railway

✅ `requirements.txt` - Python dependencies
✅ `backend_enhanced.py` - Main application
✅ `frontend_enhanced.html` - Web interface
✅ `mane_notion_mcp.py` - Notion integration
✅ `.env.example` - Environment template
✅ `Procfile` - Start command
✅ `runtime.txt` - Python version
✅ `railway.json` - Railway configuration

---

## After Deployment

### Test Your Mane

Visit your Railway URL and try:
- "Create a simple todo app"
- "Search my Notion for EIDRA"
- Upload a PDF and ask for summary

### Monitor Logs

In Railway dashboard:
- Go to **Deployments** tab
- Click on latest deployment
- View **Logs** to see Mane's activity

### Check Status

Visit: `https://your-url.railway.app/status`

Should show:
```json
{
  "status": "online",
  "model": "Gemini 2.0 Flash Experimental",
  "context": "1M tokens",
  "capabilities": [...]
}
```

---

## Troubleshooting

### Build Failed

**Check:**
1. All files are committed to Git
2. `requirements.txt` is present
3. Python version is compatible

### App Crashes

**Check logs for:**
- Missing environment variables
- API key errors
- Port binding issues

**Fix:**
- Add `GEMINI_API_KEY` in Variables
- Ensure backend binds to `0.0.0.0:8080`

### Can't Access URL

**Check:**
1. Deployment is successful (green checkmark)
2. Service is running (not sleeping)
3. Domain is generated

---

## Cost Estimate

### Railway Hobby Plan
- **Base**: $5/month
- **Usage**: ~$0.01/hour for 512MB service
- **Total**: ~$5-10/month depending on usage

### Gemini API
- **Free tier**: 1,500 requests/day
- **Paid**: ~$0.10 per 1M tokens
- **Estimated**: $0-6/month

### Total Monthly Cost
**$5-16/month** vs **$6,000/month** (Manus)

**Savings: 99.7%** 🔥

---

## Next Steps After Deployment

1. ✅ **Bookmark the URL** - Access from any device
2. ✅ **Test all features** - Build something!
3. ✅ **Add GitHub token** - Enable auto-push
4. ✅ **Add OpenAI key** - Enable image generation
5. ✅ **Share with Lum** - She can use it too!

---

## Need Help?

**Check Railway docs**: https://docs.railway.app/
**Check Mane logs**: Railway dashboard → Logs
**Ask me**: I'm here to help! 🔥

---

**Ready to deploy? Follow Step 1 above!** 🚀

