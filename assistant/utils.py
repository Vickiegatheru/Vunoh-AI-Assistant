import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

# OpenAI API configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

def call_openai_api(system_prompt, user_message):
    """Call OpenAI API using requests library, with fallback for demo mode"""
    if not OPENAI_API_KEY:
        # Demo/fallback response when API key is not available
        return get_mock_response(user_message)
    
    try:
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            "temperature": 0.7,
            "max_tokens": 1000
        }
        
        response = requests.post(OPENAI_API_URL, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        # Fallback to mock response on API error
        print(f"Warning: OpenAI API call failed: {str(e)}. Using demo response.")
        return get_mock_response(user_message)

def get_mock_response(user_message):
    """Generate a mock response for demo/testing purposes"""
    # Determine intent from keywords
    user_lower = user_message.lower()
    
    if any(word in user_lower for word in ['verify', 'document', 'title', 'id']):
        intent = "verify_document"
    elif any(word in user_lower for word in ['send', 'money', 'transfer', 'payment']):
        intent = "send_money"
    elif any(word in user_lower for word in ['hire', 'service', 'plumber', 'painter', 'cleaner']):
        intent = "hire_service"
    elif any(word in user_lower for word in ['airport', 'transfer', 'pickup', 'ride']):
        intent = "get_airport_transfer"
    else:
        intent = "check_status"
    
    mock_response = {
        "intent": intent,
        "entities": {
            "amount": "Not specified",
            "location": "Karen, Nairobi",
            "recipient": "User"
        },
        "steps": [
            "Step 1: Verify your identity",
            "Step 2: Provide required documentation",
            "Step 3: Submit request for processing",
            "Step 4: Await confirmation"
        ],
        "messages": {
            "whatsapp": "Hi! 👋 We've received your request. Our team will process it within 24 hours. You'll get updates via SMS. 📱",
            "email": "Your request has been received and is being processed. Please allow 24-48 hours for completion.",
            "sms": "Request received. Processing underway. Check email for updates."
        }
    }
    
    return json.dumps(mock_response)

def analyze_vunoh_request(user_text):
    # System prompt to ensure valid JSON and specific requirements [cite: 37, 58, 62]
    system_prompt = """
    You are an AI for Vunoh Global. Extract data from the user request and return ONLY JSON:
    {
      "intent": "send_money" | "hire_service" | "verify_document" | "get_airport_transfer" | "check_status",
      "entities": {"amount": "...", "location": "...", "recipient": "..."},
      "steps": ["Step 1...", "Step 2...", "Step 3...", "Step 4..."],
      "messages": {
         "whatsapp": "Conversational with emojis",
         "email": "Formal and structured",
         "sms": "Under 160 characters"
      }
    }
    """
    
    response_text = call_openai_api(system_prompt, user_text)
    data = json.loads(response_text)
    
    # Logic for Risk Scoring [cite: 43-48]
    risk = 20
    if "urgent" in user_text.lower(): risk += 30
    if data['intent'] == "verify_document": risk += 40
    
    # Employee Assignment [cite: 72-74]
    teams = {
        "send_money": "Finance Team",
        "verify_document": "Legal Team",
        "hire_service": "Operations Team"
    }
    assigned_to = teams.get(data['intent'], "General Support")
    
    return data, risk, assigned_to