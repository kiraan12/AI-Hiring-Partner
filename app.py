import streamlit as st
from src.chatbot import TalentScoutBot

# ─── PAGE CONFIG ─────────────────────────

st.set_page_config(
    page_title="TalentScout Hiring Assistant",
    page_icon="🤖",
    layout="centered"
)

# ─── CUSTOM CSS (FIX INCLUDED) ───────────

st.markdown("""
<style>

/* Fix input visibility */
.stChatInput input {
    color: black !important;
    background-color: white !important;
    border-radius: 10px;
    padding: 10px;
}

.stChatInput input::placeholder {
    color: gray !important;
}

/* Chat container */
.chat-container {
    max-width: 700px;
    margin: auto;
}

/* User message */
.user-msg {
    background-color: #DCF8C6;
    color: black;
    padding: 10px 15px;
    border-radius: 12px;
    margin: 8px 0;
    text-align: right;
}

/* Bot message */
.bot-msg {
    background-color: #F1F0F0;
    color: black;
    padding: 10px 15px;
    border-radius: 12px;
    margin: 8px 0;
    text-align: left;
}

/* Header */
.header {
    text-align: center;
    margin-bottom: 20px;
}

/* Footer */
.footer {
    text-align: center;
    font-size: 12px;
    color: gray;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# ─── HEADER ─────────────────────────────

st.markdown("""
<div class="header">
    <h1>🤖 TalentScout AI Hiring Assistant</h1>
    <p>AI-powered technical candidate screening</p>
</div>
""", unsafe_allow_html=True)

# ─── INIT SESSION ───────────────────────

if "bot" not in st.session_state:
    st.session_state.bot = TalentScoutBot()

if "history" not in st.session_state:
    st.session_state.history = []

if "started" not in st.session_state:
    st.session_state.started = False

# ─── START BUTTON ───────────────────────

if not st.session_state.started:
    if st.button("🚀 Start Screening"):
        st.session_state.started = True
        greeting = st.session_state.bot.get_greeting()
        st.session_state.history.append({
            "role": "assistant",
            "content": greeting
        })
        st.rerun()

# ─── INPUT FIRST (IMPORTANT) ────────────

if st.session_state.started:

    user_input = st.chat_input("Type your response here...")

    if user_input:
        # Add user message
        st.session_state.history.append({
            "role": "user",
            "content": user_input
        })

        # Get bot response
        bot_response, extracted = st.session_state.bot.chat(
            user_input,
            st.session_state.history
        )

        # Add bot response
        st.session_state.history.append({
            "role": "assistant",
            "content": bot_response
        })

        st.rerun()

# ─── DISPLAY CHAT ───────────────────────

st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state.history:
    if msg["role"] == "user":
        st.markdown(
            f'<div class="user-msg">👤 {msg["content"]}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="bot-msg">🤖 {msg["content"]}</div>',
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)

# ─── FOOTER ─────────────────────────────

st.markdown("""
<div class="footer">
    © 2026 TalentScout | AI Hiring Assistant
</div>
""", unsafe_allow_html=True)