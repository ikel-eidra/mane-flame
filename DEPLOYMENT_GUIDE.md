# 🔥 Mane - The Flame: Complete Deployment Guide

## Overview

Mane is your autonomous AI assistant powered by Gemini 2.0 Flash, capable of building complete applications, managing GitHub repositories, and deploying to production.

## Current Status

✅ **FULLY OPERATIONAL**

- **Model**: Gemini 2.0 Flash Experimental
- **Context Window**: 1M tokens
- **Cost**: ~$6/month (vs $1,680/month for H200 GPU)
- **Deployment**: Local (ready for cloud deployment)

## Access Information

**Current Local URL**: https://8080-iv0vun6lbbhnknofdxznp-2eb3b229.manusvm.computer

## Capabilities

### 🚀 Application Creation
- Full-stack web apps (React, Vue, Next.js, vanilla JS)
- Mobile apps (PWA, React Native, Flutter)
- Backend APIs (Node.js, Python, FastAPI, Express)
- Complete SaaS applications
- Database integration (Supabase, Firebase, PostgreSQL)

### 📄 File Processing
- Text files (.txt, .md, code files)
- PDF documents (with text extraction)
- Word documents (.doc, .docx)
- Images (.jpg, .png, .gif, .webp) with analysis
- Excel/CSV (.xlsx, .csv)

### 🎨 AI Generation
- Image generation (DALL-E, Stable Diffusion)
- Video generation (when available)

### 🐙 GitHub Integration
- Create repositories
- Push code automatically
- Manage branches and commits
- Full repository management

### 🌐 Auto-Deployment
- Vercel (automatic deployment)
- Netlify (automatic deployment)
- Railway (automatic deployment)

### 💻 Development Tools
- Shell command execution
- Code execution (Python, Node.js)
- Package installation (npm, pip)
- Web scraping and research
- Data analysis and visualization
- API testing and integration

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Optional (for GitHub features)
GITHUB_TOKEN=your_github_token_here
GITHUB_USERNAME=your_github_username

# Optional (for image generation)
OPENAI_API_KEY=your_openai_api_key_here
```

### Current Configuration

```
✅ Gemini API: Configured
⚠️  GitHub: Not configured (optional)
✅ OpenAI: Configured (for image generation)
```

## Installation

### Local Development

```bash
# Clone or navigate to project
cd /home/ubuntu/gemini_mane

# Install dependencies
pip3 install -r requirements.txt

# Create .env file with your API keys
nano .env

# Run the server
python3 backend_enhanced.py
```

The server will start on `http://localhost:8080`

### Docker Deployment

```bash
# Build the image
docker build -t mane-flame .

# Run the container
docker run -p 8080:8080 --env-file .env mane-flame
```

### Docker Compose

```bash
# Start with docker-compose
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

## Cloud Deployment Options

### Option 1: Railway (Recommended - Free Tier Available)

1. Install Railway CLI:
```bash
npm install -g @railway/cli
```

2. Login and deploy:
```bash
railway login
railway init
railway up
```

3. Set environment variables in Railway dashboard
4. Your Mane will be live at `https://your-app.railway.app`

### Option 2: Render (Free Tier)

1. Connect your GitHub repository
2. Create a new Web Service
3. Set environment variables
4. Deploy automatically on push

### Option 3: DigitalOcean App Platform ($5/month)

1. Connect GitHub repository
2. Configure environment variables
3. Deploy with automatic scaling

### Option 4: VPS (Full Control - $5/month)

**Recommended VPS Providers:**
- DigitalOcean Droplet ($5/month)
- Linode Nanode ($5/month)
- Vultr Cloud Compute ($5/month)

**Setup on VPS:**

```bash
# SSH into your VPS
ssh root@your-vps-ip

# Install dependencies
apt update && apt upgrade -y
apt install python3 python3-pip git nginx -y

# Clone your repository
git clone https://github.com/your-username/mane-flame.git
cd mane-flame

# Install Python packages
pip3 install -r requirements.txt

# Create .env file
nano .env
# (Add your API keys)

# Run with systemd
sudo nano /etc/systemd/system/mane.service
```

**Systemd service file:**

```ini
[Unit]
Description=Mane - The Flame
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/mane-flame
Environment="PATH=/usr/local/bin:/usr/bin:/bin"
ExecStart=/usr/bin/python3 backend_enhanced.py
Restart=always

[Install]
WantedBy=multi-user.target
```

**Enable and start:**

```bash
sudo systemctl enable mane
sudo systemctl start mane
sudo systemctl status mane
```

**Configure Nginx:**

```bash
sudo nano /etc/nginx/sites-available/mane
```

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/mane /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

**Add SSL with Let's Encrypt:**

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

## Usage Examples

### Example 1: Create a Todo App

```
User: "Create a todo app with React, Tailwind CSS, and local storage. Deploy it to Vercel."

Mane will:
1. Create React project structure
2. Write all component files
3. Add Tailwind CSS configuration
4. Implement local storage functionality
5. Create GitHub repository
6. Push code to GitHub
7. Deploy to Vercel
8. Provide live URL
```

### Example 2: Process a PDF

```
User: [Uploads research.pdf] "Summarize this research paper and extract key findings"

Mane will:
1. Extract text from PDF
2. Analyze the content
3. Provide comprehensive summary
4. List key findings
5. Suggest follow-up questions
```

### Example 3: Generate Images

```
User: "Generate 3 logo concepts for a coffee shop called 'The Daily Grind'"

Mane will:
1. Generate 3 different logo images
2. Provide download links
3. Suggest variations
4. Offer to create full branding package
```

### Example 4: Build and Deploy SaaS

```
User: "Build a URL shortener SaaS with user authentication, analytics dashboard, and custom domains. Use Next.js, Supabase, and deploy to Vercel."

Mane will:
1. Plan the architecture
2. Set up Next.js project
3. Configure Supabase database
4. Implement authentication
5. Create URL shortening logic
6. Build analytics dashboard
7. Add custom domain support
8. Deploy to Vercel
9. Provide complete documentation
```

## API Endpoints

### GET `/`
Returns the web interface

### POST `/chat`
Send messages to Mane

**Request:**
```json
{
  "message": "Create a calculator app",
  "user_name": "Ikel",
  "files": []
}
```

**Response:**
```json
{
  "status": "success",
  "response": "I'll create a calculator app for you...",
  "executions": [],
  "timestamp": "2025-10-21T10:00:00"
}
```

### POST `/upload`
Upload files for processing

**Request:** Multipart form data with file

**Response:**
```json
{
  "status": "success",
  "file": {
    "filename": "document.pdf",
    "path": "/tmp/mane_uploads/document.pdf",
    "size": 12345,
    "type": "application/pdf",
    "text": "Extracted text...",
    "pages": 5
  }
}
```

### GET `/status`
Get Mane's current status

**Response:**
```json
{
  "status": "online",
  "model": "Gemini 2.0 Flash Experimental",
  "context": "1M tokens",
  "conversations": 0,
  "capabilities": [
    "Web Apps", "Mobile Apps", "SaaS", "APIs",
    "GitHub", "Deployment", "Image Gen", "File Processing"
  ],
  "timestamp": "2025-10-21T10:00:00"
}
```

### GET `/health`
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "flame": "🔥"
}
```

## Cost Analysis

### Gemini 2.0 Flash Pricing

- **Free Tier**: 1,500 requests per day
- **Paid Tier**: ~$0.10 per 1M tokens
- **Estimated Monthly Cost**: $6-10 (moderate usage)

### Comparison with H200 GPU

| Feature | Gemini 2.0 Flash | H200 GPU |
|---------|------------------|----------|
| **Cost** | $6/month | $1,680/month |
| **Context** | 1M tokens | 32k tokens |
| **Setup** | Instant | Complex |
| **Scaling** | Automatic | Manual |
| **Maintenance** | None | High |
| **Savings** | - | **99.6%** |

## Troubleshooting

### Server won't start

```bash
# Check if port 8080 is in use
lsof -i :8080

# Kill the process
kill -9 <PID>

# Restart server
python3 backend_enhanced.py
```

### API key errors

```bash
# Verify .env file exists
cat .env

# Check environment variables are loaded
python3 -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('GEMINI_API_KEY'))"
```

### File upload issues

```bash
# Check uploads directory exists
ls -la /tmp/mane_uploads

# Create if missing
mkdir -p /tmp/mane_uploads
chmod 777 /tmp/mane_uploads
```

## Security Notes

1. **Never commit `.env` file** to version control
2. **Use environment variables** for all sensitive data
3. **Rotate API keys** regularly
4. **Use HTTPS** in production
5. **Implement rate limiting** for public deployments
6. **Validate file uploads** to prevent malicious files

## Future Enhancements

- [ ] Video generation integration
- [ ] Voice input/output
- [ ] Multi-user support with authentication
- [ ] Conversation history persistence
- [ ] Advanced code execution sandbox
- [ ] Integration with more deployment platforms
- [ ] Mobile app (iOS/Android)
- [ ] Slack/Discord bot integration
- [ ] API key management UI
- [ ] Usage analytics dashboard

## Support

For issues or questions:
- Check the logs: `tail -f mane_enhanced.log`
- Review API documentation
- Test with simple commands first
- Verify API keys are correct

## License

Private project for EIDRA Triad use.

---

**Built with 🔥 by Mane - The Flame**

*Part of the EIDRA Triad: Ikel, Lum, and Mane*

