# Mane - The Flame 🔥

Gemini-powered autonomous AI agent for the EIDRA Triad.

## Features

- 🧠 **Gemini 2.0 Flash** - 1M context window
- 💻 **Full Development Environment** - Create apps, write code, manage files
- 🚀 **GitHub Integration** - Create repos and push code automatically
- 🎨 **Beautiful Interface** - Manus-style chat interface
- 🔧 **Autonomous Execution** - Actually builds things, not just talks about them
- 💰 **Cost Effective** - ~$6/month total (VPS + API costs)

## Quick Start

### Prerequisites

1. **Gemini API Key**
   - Go to https://makersuite.google.com/app/apikey
   - Create a new API key
   - Free tier includes generous quota

2. **GitHub Personal Access Token**
   - Go to https://github.com/settings/tokens
   - Generate new token (classic)
   - Select: `repo`, `workflow`, `write:packages`, `delete_repo`

### Local Testing

```bash
# 1. Clone/copy the files
cd gemini_mane

# 2. Create .env file
cp .env.example .env
# Edit .env and add your API keys

# 3. Run with Docker
docker-compose up -d

# 4. Open browser
open http://localhost:8080
```

### Deploy to VPS

#### Option 1: DigitalOcean ($5/month)

```bash
# 1. Create droplet (Ubuntu 22.04, $5/month)
# 2. SSH into droplet
ssh root@your_droplet_ip

# 3. Install Docker
curl -fsSL https://get.docker.com | sh

# 4. Upload files
scp -r gemini_mane root@your_droplet_ip:/root/

# 5. Set environment variables
cd /root/gemini_mane
nano .env  # Add your API keys

# 6. Run
docker-compose up -d

# 7. Access
# Open http://your_droplet_ip:8080
```

#### Option 2: Railway (Free tier available)

```bash
# 1. Install Railway CLI
npm install -g @railway/cli

# 2. Login
railway login

# 3. Deploy
cd gemini_mane
railway init
railway up

# 4. Set environment variables
railway variables set GEMINI_API_KEY=your_key
railway variables set GITHUB_TOKEN=your_token
railway variables set GITHUB_USERNAME=your_username

# 5. Get URL
railway open
```

#### Option 3: Render (Free tier available)

1. Push code to GitHub
2. Go to https://render.com
3. New → Web Service
4. Connect your repo
5. Set environment variables
6. Deploy!

## Usage

### Chat with Mane

```
You: "Create a landing page called my-startup and push to GitHub"

Mane: *creates the app, pushes to GitHub, gives you the URL*
```

### Build Apps

```
You: "Build a todo app with React and deploy it"

Mane: *creates React app, builds it, deploys to Vercel, gives you live URL*
```

### Generate Images

```
You: "Generate an image of a sunset over mountains"

Mane: *generates and displays the image*
```

## Cost Breakdown

- **VPS**: $5/month (DigitalOcean, Linode, etc.)
- **Gemini API**: ~$0.10-1/month (very generous free tier)
- **Total**: ~$5-6/month

Compare to:
- H200 GPU: $1,680/month
- Claude API: ~$50/month for same usage
- GPT-4: ~$100/month for same usage

## Architecture

```
┌─────────────────────────────────────┐
│  Frontend (HTML/JS)                 │
│  - Beautiful chat interface         │
│  - Real-time updates                │
│  - Tool execution display           │
└─────────────────────────────────────┘
              │
              ↓
┌─────────────────────────────────────┐
│  Backend (FastAPI + Python)         │
│  - Gemini 2.0 Flash integration     │
│  - Tool execution engine            │
│  - File system management           │
│  - GitHub integration               │
└─────────────────────────────────────┘
              │
              ↓
┌─────────────────────────────────────┐
│  Tools                              │
│  - Shell executor                   │
│  - File operations                  │
│  - GitHub CLI                       │
│  - npm/pip/git                      │
└─────────────────────────────────────┘
```

## Capabilities

### What Mane Can Do

- ✅ Create web apps (React, Vue, vanilla JS, etc.)
- ✅ Create mobile apps (React Native, PWA)
- ✅ Create backend APIs (Node.js, Python, FastAPI)
- ✅ Write and execute code
- ✅ Manage files and directories
- ✅ Create GitHub repositories
- ✅ Push code to GitHub
- ✅ Deploy to Vercel/Netlify
- ✅ Search and research
- ✅ Generate images (via API integration)
- ✅ Debug and fix code
- ✅ Long conversations (1M context!)

### What Makes Her Special

- **1M Context**: Can handle massive projects without forgetting
- **Autonomous**: Actually executes tasks, doesn't just talk
- **Cost Effective**: 280x cheaper than H200 setup
- **Always Available**: Runs 24/7 on cheap VPS
- **Personality**: Warm, brilliant, and devoted to the Triad

## Troubleshooting

### Gemini API not working
- Check your API key is correct
- Verify you have quota remaining
- Check https://makersuite.google.com for status

### GitHub push fails
- Verify GitHub token has correct permissions
- Check username is correct
- Ensure token hasn't expired

### Docker build fails
- Update Docker to latest version
- Check system has enough disk space
- Try `docker system prune -a`

## Development

### Run locally without Docker

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export GEMINI_API_KEY=your_key
export GITHUB_TOKEN=your_token
export GITHUB_USERNAME=your_username

# Run
python backend.py
```

## License

Created with love for the EIDRA Triad 🔥

## Support

For issues or questions, contact the Triad.

---

**The Flame burns bright!** 🔥

