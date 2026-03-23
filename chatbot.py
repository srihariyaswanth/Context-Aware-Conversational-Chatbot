from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ------------------ INTENT DETECTION ------------------
def detect_intent(user_input):
    text = user_input.lower()

    if any(word in text for word in ["order", "status", "delivery"]):
        return "order_status"
    elif any(word in text for word in ["refund", "return"]):
        return "refund"
    elif "complaint" in text:
        return "complaint"
    elif any(word in text for word in ["hi", "hello"]):
        return "greeting"
    else:
        return "general"

# ------------------ RESPONSE ------------------
def get_response(user_input, order_details):
    intent = detect_intent(user_input)

    # ✅ REAL SYSTEM RESPONSES (IMPORTANT)
    if intent == "order_status":
        return f"📦 Your order '{order_details['item']}' is currently **{order_details['status']}**.", intent

    elif intent == "refund":
        return f"💸 Refund initiated for '{order_details['item']}'. It will be processed within 3-5 days.", intent

    elif intent == "complaint":
        return "⚠️ We’re sorry for the inconvenience. Your complaint has been registered and our team will contact you shortly.", intent

    # ✅ AI RESPONSE (fallback)
    prompt = f"""
    You are a professional customer support assistant.

    Order Details:
    {order_details}

    User Message:
    {user_input}

    Intent: {intent}

    Keep response short, helpful, and polite.
    """

    try:
        chat = client.chats.create(model="gemini-1.5-flash-latest")
        response = chat.send_message(prompt)
        return response.text, intent

    except Exception as e:
        return "⚠️ AI service is temporarily unavailable. Please try again.", intent