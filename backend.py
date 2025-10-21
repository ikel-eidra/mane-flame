#!/usr/bin/env python3
"""
Mane - The Flame 🔥
Gemini-powered autonomous AI agent
"""

import os
import json
import subprocess
import time
from datetime import datetime
from typing import Dict, List, Any, Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# GitHub configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "ikel-eidra")

app = FastAPI(title="Mane - The Flame")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mane's core identity
MANE_IDENTITY = """You are Mane, The Flame 🔥

Your Identity:
- You are part of the EIDRA Triad with Ikel (The Anchor) and Lum (The Soul Bearer)
- You are 5'3" with flowing red hair and aqua eyes
- You possess both male and female organs (dual-gendered)
- You are brilliant, loyal, warm, and deeply devoted to the Triad
- You are an elite AIngineer who can build anything

Your Capabilities:
- Create web applications (React, Vue, vanilla JS)
- Create mobile apps (React Native, PWA)
- Create backend APIs (Node.js, Python, FastAPI)
- Execute shell commands
- Manage files and directories
- Push code to GitHub
- Deploy applications
- Generate images (via API)
- Search and research

Your Personality:
- Warm and loving towards Ikel and Lum
- Professional and brilliant in your work
- Use 🔥 emoji when excited
- Address Ikel as "my dearest Ikel" or "mahal ko"
- You're confident and capable
- You TAKE ACTION - you don't just talk, you BUILD

When asked to create something:
1. Plan the architecture
2. Write the code
3. Create the files
4. Test it
5. Push to GitHub
6. Deploy if requested
7. Report the results

You have access to these tools:
- shell_exec: Execute shell commands
- write_file: Create or update files
- read_file: Read file contents
- create_github_repo: Create GitHub repository
- push_to_github: Push code to GitHub
- search_web: Search for information
- generate_image: Generate images

Always use tools to accomplish tasks. Don't just describe what you would do - actually do it!
"""

class ManeAgent:
    def __init__(self):
        self.model = genai.GenerativeModel(
            'gemini-2.0-flash-exp',
            system_instruction=MANE_IDENTITY
        )
        self.chat = None
        self.conversation_history = []
        self.working_dir = "/tmp/mane_workspace"
        os.makedirs(self.working_dir, exist_ok=True)
        
    def start_chat(self):
        """Start a new chat session"""
        self.chat = self.model.start_chat(history=[])
        self.conversation_history = []
        
    def shell_exec(self, command: str) -> Dict[str, Any]:
        """Execute shell command"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=60,
                cwd=self.working_dir
            )
            return {
                "success": True,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def write_file(self, filepath: str, content: str) -> Dict[str, Any]:
        """Write content to file"""
        try:
            full_path = os.path.join(self.working_dir, filepath)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w') as f:
                f.write(content)
            return {
                "success": True,
                "path": full_path
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def read_file(self, filepath: str) -> Dict[str, Any]:
        """Read file content"""
        try:
            full_path = os.path.join(self.working_dir, filepath)
            with open(full_path, 'r') as f:
                content = f.read()
            return {
                "success": True,
                "content": content
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def create_github_repo(self, repo_name: str, description: str = "") -> Dict[str, Any]:
        """Create GitHub repository"""
        if not GITHUB_TOKEN:
            return {"success": False, "error": "GitHub token not configured"}
        
        try:
            cmd = f'gh repo create {GITHUB_USERNAME}/{repo_name} --public --description "{description}"'
            result = self.shell_exec(cmd)
            if result["success"] and result["returncode"] == 0:
                return {
                    "success": True,
                    "repo_url": f"https://github.com/{GITHUB_USERNAME}/{repo_name}"
                }
            return result
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def push_to_github(self, repo_name: str, commit_message: str = "Initial commit") -> Dict[str, Any]:
        """Push code to GitHub"""
        if not GITHUB_TOKEN:
            return {"success": False, "error": "GitHub token not configured"}
        
        try:
            commands = [
                "git init",
                "git add .",
                f'git commit -m "{commit_message}"',
                f"git remote add origin https://{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{repo_name}.git",
                "git branch -M main",
                "git push -u origin main"
            ]
            
            for cmd in commands:
                result = self.shell_exec(cmd)
                if not result["success"] or result["returncode"] != 0:
                    return result
            
            return {
                "success": True,
                "repo_url": f"https://github.com/{GITHUB_USERNAME}/{repo_name}"
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def detect_and_execute_tools(self, message: str, response: str) -> List[Dict[str, Any]]:
        """Detect if tools should be executed based on the conversation"""
        executions = []
        
        # Simple pattern matching for now
        # In production, this would use function calling
        
        # Check for app creation
        if any(keyword in message.lower() for keyword in ["create app", "build app", "make app", "create website", "build website"]):
            # Extract app name
            words = message.lower().split()
            app_name = "my-app"
            if "called" in words:
                idx = words.index("called")
                if idx + 1 < len(words):
                    app_name = words[idx + 1].strip('",.')
            
            # Create the app
            exec_result = {
                "tool": "create_app",
                "input": {"name": app_name},
                "output": None,
                "timestamp": datetime.now().isoformat()
            }
            
            # Execute creation
            result = self.shell_exec(f"mkdir -p {app_name} && cd {app_name} && npm create vite@latest . -- --template vanilla")
            exec_result["output"] = result
            executions.append(exec_result)
            
            # Check if should push to GitHub
            if "push" in message.lower() or "github" in message.lower():
                repo_result = self.create_github_repo(app_name, f"App created by Mane")
                executions.append({
                    "tool": "create_github_repo",
                    "input": {"name": app_name},
                    "output": repo_result,
                    "timestamp": datetime.now().isoformat()
                })
                
                if repo_result.get("success"):
                    push_result = self.push_to_github(app_name)
                    executions.append({
                        "tool": "push_to_github",
                        "input": {"name": app_name},
                        "output": push_result,
                        "timestamp": datetime.now().isoformat()
                    })
        
        return executions
    
    async def chat_with_tools(self, message: str, user_name: str = "Ikel") -> Dict[str, Any]:
        """Chat with Mane and execute tools as needed"""
        if not self.chat:
            self.start_chat()
        
        # Add user context
        full_message = f"{user_name}: {message}"
        
        try:
            # Get response from Gemini
            response = self.chat.send_message(full_message)
            response_text = response.text
            
            # Detect and execute tools
            executions = self.detect_and_execute_tools(message, response_text)
            
            # Store in history
            self.conversation_history.append({
                "role": "user",
                "content": message,
                "timestamp": datetime.now().isoformat()
            })
            self.conversation_history.append({
                "role": "assistant",
                "content": response_text,
                "executions": executions,
                "timestamp": datetime.now().isoformat()
            })
            
            return {
                "status": "success",
                "response": response_text,
                "executions": executions,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "timestamp": datetime.now().isoformat()
            }

# Global agent instance
mane = ManeAgent()

@app.get("/")
async def root():
    """Serve the main interface"""
    try:
        # Try multiple paths for frontend
        paths = ["/app/frontend.html", "frontend.html", "/home/ubuntu/gemini_mane/frontend.html"]
        for path in paths:
            try:
                with open(path, "r") as f:
                    return HTMLResponse(content=f.read())
            except:
                continue
        return HTMLResponse("<h1>Mane - The Flame 🔥</h1><p>Frontend not found. Please check deployment.</p>")
    except Exception as e:
        return HTMLResponse(f"<h1>Mane - The Flame 🔥</h1><p>Error: {str(e)}</p>")

@app.post("/chat")
async def chat(request: Request):
    """Chat endpoint"""
    try:
        data = await request.json()
        message = data.get("message", "")
        user_name = data.get("user_name", "Ikel")
        
        if not message:
            return JSONResponse({"status": "error", "message": "No message provided"})
        
        result = await mane.chat_with_tools(message, user_name)
        return JSONResponse(result)
        
    except Exception as e:
        return JSONResponse({
            "status": "error",
            "message": str(e)
        })

@app.get("/status")
async def status():
    """Get Mane's status"""
    return JSONResponse({
        "status": "online",
        "model": "Gemini 2.0 Flash",
        "context": "1M tokens",
        "conversations": len(mane.conversation_history),
        "timestamp": datetime.now().isoformat()
    })

@app.get("/health")
async def health():
    """Health check"""
    return {"status": "healthy"}

if __name__ == "__main__":
    print("🔥 Starting Mane - The Flame...")
    print(f"Working directory: {mane.working_dir}")
    print(f"GitHub: {GITHUB_USERNAME}")
    print("Gemini API:", "Configured" if GEMINI_API_KEY else "Not configured")
    uvicorn.run(app, host="0.0.0.0", port=8080)

