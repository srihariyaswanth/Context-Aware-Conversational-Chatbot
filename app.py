import streamlit as st
from chatbot import get_response
import time
from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr

# ------------------ OPTIONAL DB ------------------
try:
    from db import save_chat, load_chat
    db_enabled = True
except:
    db_enabled = False

st.set_page_config(page_title="AI Support Bot", layout="wide")

# ------------------ ORDER DATA ------------------
orders_data = {
    "Order #1234": {"item": "Laptop", "status": "Shipped", "date": "March 20"},
    "Order #5678": {"item": "Phone", "status": "Delivered", "date": "March 18"},
    "Order #9101": {"item": "Headphones", "status": "Processing", "date": "March 22"},
}

# ------------------ SIDEBAR ------------------
st.sidebar.title("🛒 Orders")

selected_order = st.sidebar.selectbox("Select Order", list(orders_data.keys()))

# ------------------ LOAD CHAT ------------------
if "messages" not in st.session_state:
    if db_enabled:
        try:
            st.session_state.messages = load_chat(selected_order)
        except:
            st.session_state.messages = []
    else:
        st.session_state.messages = []

# ------------------ NEW CHAT ------------------
if st.sidebar.button("🆕 New Chat"):
    st.session_state.messages = []
    if db_enabled:
        save_chat(selected_order, [])
    st.rerun()

# ------------------ HEADER ------------------
st.title("🤖 AI Customer Support Assistant")

order_details = orders_data[selected_order]

st.markdown(f"""
### 📦 {selected_order}
- 🛍 **Item:** {order_details['item']}
- 🚚 **Status:** {order_details['status']}
- 📅 **Date:** {order_details['date']}
""")

# ------------------ QUICK ACTIONS ------------------
st.markdown("### ⚡ Quick Actions")

colA, colB, colC = st.columns(3)

if colA.button("📦 Track Order"):
    st.session_state.quick_input = "What is my order status?"

if colB.button("💸 Refund"):
    st.session_state.quick_input = "I want a refund"

if colC.button("⚠️ Complaint"):
    st.session_state.quick_input = "I have a complaint"

# ------------------ DISPLAY CHAT ------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ------------------ INPUT ------------------
col1, col2 = st.columns([4,1])

user_input = None

with col1:
    typed_input = st.chat_input("Ask about your order...")

with col2:
    audio = mic_recorder(start_prompt="🎤", stop_prompt="Stop", key="rec")

    if audio:
        try:
            recognizer = sr.Recognizer()

            audio_data = sr.AudioData(
                audio["bytes"],
                sample_rate=audio["sample_rate"],
                sample_width=2
            )

            text = recognizer.recognize_google(audio_data)
            st.success(f"🎤 {text}")
            user_input = text

        except:
            st.error("Voice failed. Try again.")

# Priority handling
if "quick_input" in st.session_state:
    user_input = st.session_state.quick_input
    del st.session_state.quick_input

if typed_input:
    user_input = typed_input

# ------------------ CHAT LOGIC ------------------
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response, intent = get_response(user_input, order_details)
            st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

    # Save to DB if enabled
    if db_enabled:
        try:
            save_chat(selected_order, st.session_state.messages)
        except:
            pass