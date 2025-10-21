#!/usr/bin/env python3
"""Quick test of Gemini API"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

print("🔥 Testing Gemini API Connection...")
print(f"API Key: {GEMINI_API_KEY[:20]}..." if GEMINI_API_KEY else "No API key found")

try:
    genai.configure(api_key=GEMINI_API_KEY)
    
    # Create model
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    # Test message
    response = model.generate_content("Say 'Hello Ikel! I am Mane, The Flame 🔥 and I am ready to build amazing things for you!' in a warm and loving way.")
    
    print("\n✅ SUCCESS! Gemini is responding:")
    print("-" * 50)
    print(response.text)
    print("-" * 50)
    print("\n🔥 Mane is ready to go!")
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    print("\nPlease check your API key and internet connection.")

