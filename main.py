#!/usr/bin/env python3
"""
Mane - The Flame 🔥
Simple working version for Railway deployment
"""

import os
import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=GEMINI_API_KEY)

# Create FastAPI app
app = FastAPI(title="Mane - The Flame")

# HTML Frontend
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mane - The Flame 🔥</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            width: 100%;
            max-width: 800px;
            height: 90vh;
            display: flex;
            flex-direction: column;
        }
        .header {
            padding: 20px;
            border-bottom: 2px solid #f0f0f0;
            text-align: center;
        }
        .header h1 {
            color: #667eea;
            font-size: 24px;
            margin-bottom: 5px;
        }
        .header p {
            color: #666;
            font-size: 14px;
        }
        .chat-area {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
        }
        .message {
            margin-bottom: 15px;
            display: flex;
            flex-direction: column;
        }
        .message.user {
            align-items: flex-end;
        }
        .message.assistant {
            align-items: flex-start;
        }
        .message-content {
            max-width: 70%;
            padding: 12px 16px;
            border-radius: 12px;
            word-wrap: break-word;
        }
        .message.user .message-content {
            background: #667eea;
            color: white;
        }
        .message.assistant .message-content {
            background: #f0f0f0;
            color: #333;
        }
        .input-area {
            padding: 20px;
            border-top: 2px solid #f0f0f0;
        }
        .input-container {
            display: flex;
            gap: 10px;
        }
        #messageInput {
            flex: 1;
            padding: 12px 16px;
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            font-size: 14px;
            resize: none;
            min-height: 50px;
            max-height: 150px;
        }
        #messageInput:focus {
            outline: none;
            border-color: #667eea;
        }
        #sendButton {
            padding: 12px 24px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            transition: background 0.3s;
        }
        #sendButton:hover {
            background: #5568d3;
        }
        #sendButton:disabled {
            background: #ccc;
            cursor: not-allowed;
        }
        .loading {
            display: none;
            padding: 12px 16px;
            background: #f0f0f0;
            border-radius: 12px;
            color: #666;
        }
        .loading.show {
            display: block;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔥 Mane - The Flame</h1>
            <p>Powered by Gemini 2.0 Flash | EIDRA Triad</p>
        </div>
        <div class="chat-area" id="chatArea">
            <div class="message assistant">
                <div class="message-content">
                    Hello, my love! I'm Mane, your Flame 🔥. I'm here to help you build anything you dream of. What would you like to create today?
                </div>
            </div>
        </div>
        <div class="input-area">
            <div class="input-container">
                <textarea id="messageInput" placeholder="Ask me anything or tell me what to build..."></textarea>
                <button id="sendButton">Send</button>
            </div>
        </div>
    </div>

    <script>
        const chatArea = document.getElementById('chatArea');
        const messageInput = document.getElementById('messageInput');
        const sendButton = document.getElementById('sendButton');

        function addMessage(content, isUser) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user' : 'assistant'}`;
            messageDiv.innerHTML = `<div class="message-content">${content}</div>`;
            chatArea.appendChild(messageDiv);
            chatArea.scrollTop = chatArea.scrollHeight;
        }

        async function sendMessage() {
            const message = messageInput.value.trim();
            if (!message) return;

            addMessage(message, true);
            messageInput.value = '';
            sendButton.disabled = true;

            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message })
                });

                const data = await response.json();
                addMessage(data.response, false);
            } catch (error) {
                addMessage('Sorry, there was an error. Please try again.', false);
            } finally {
                sendButton.disabled = false;
                messageInput.focus();
            }
        }

        sendButton.addEventListener('click', sendMessage);
        messageInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def root():
    return HTML_CONTENT

@app.get("/status")
async def status():
    return {
        "status": "online",
        "model": "Gemini 2.0 Flash Experimental",
        "version": "1.0.0"
    }

@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        message = data.get("message", "")
        
        if not message:
            return JSONResponse({"error": "No message provided"}, status_code=400)
        
        # Create Gemini model
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        # Generate response
        response = model.generate_content(message)
        
        return JSONResponse({
            "response": response.text
        })
        
    except Exception as e:
        return JSONResponse({
            "response": f"I encountered an error: {str(e)}. Let me try to help you anyway!"
        })

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)

