# 🤖 AI Customer Support Chatbot

A context-aware AI chatbot designed for customer support use cases.  
This system can handle multi-turn conversations, understand user intent, and provide order-based responses.

---

## 🚀 Features

- 🧠 Context-aware conversation
- 📦 Order-based chatbot (each order handled separately)
- 🎯 Intent recognition (order status, refund, complaint)
- ⚡ Quick action buttons
- 🎤 Voice input support
- 💬 Multi-turn conversation handling
- 🧩 Modular architecture (UI + AI + optional DB)

---

## 🛠️ Tech Stack

- Python
- Streamlit (UI)
- Google Gemini API (AI)
- SpeechRecognition (voice input)
- streamlit-mic-recorder

---

## 📂 Project Structure
# 🤖 AI Customer Support Chatbot

A context-aware AI chatbot designed for customer support use cases.  
This system can handle multi-turn conversations, understand user intent, and provide order-based responses.

---

## 🚀 Features

- 🧠 Context-aware conversation
- 📦 Order-based chatbot (each order handled separately)
- 🎯 Intent recognition (order status, refund, complaint)
- ⚡ Quick action buttons
- 🎤 Voice input support
- 💬 Multi-turn conversation handling
- 🧩 Modular architecture (UI + AI + optional DB)

---

## 🛠️ Tech Stack

- Python
- Streamlit (UI)
- Google Gemini API (AI)
- SpeechRecognition (voice input)
- streamlit-mic-recorder

---

## 📂 Project Structure
ai-chatbot/
│
├── app.py # Main Streamlit UI
├── chatbot.py # AI + intent logic
├── db.py # (Optional) MongoDB integration
├── .env # API keys
├── requirements.txt
└── README.md

---

## ▶️ How to Run

### 1. Clone the repository

### 2. Install dependencies
pip install -r requirements.txt
### 3. Add API key
Create a `.env` file:


GEMINI_API_KEY=your_api_key_here

### 4. Run the app

streamlit run app.py


---

## 💬 Sample Queries

- "Where is my order?"
- "I want a refund"
- "I have a complaint"
- "Track my order"

---

## 🧠 How It Works

- Detects user intent using rule-based logic
- Uses Gemini API for intelligent responses
- Maintains conversation context
- Supports voice + text input
- Handles different orders separately

---

## 🗄️ Database (Optional)

The project includes MongoDB integration (`db.py`) for persistent chat storage.

Currently:
- Uses session-based memory by default
- Can be extended to use MongoDB Atlas for production

---

## 🎯 Use Case

Customer support automation system that can:
- Answer user queries
- Track orders
- Handle complaints
- Process refund requests

---

## 📌 Future Improvements

- User authentication
- Deployment (Streamlit Cloud)
- Analytics dashboard
- Multi-language support

---

## 👨‍💻 Author

Developed as part of cerevyn campus drive assignment.