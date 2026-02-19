import streamlit as st
import ollama

st.set_page_config(page_title="Omnitrix Interface", layout="centered", page_icon="⌚")

st.markdown("""
    <style>
    /* Background & Text */
    .stApp {
        background-color: #050a05;
        color: #39ff14;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #001a00;
        border-right: 2px solid #39ff14;
        box-shadow: 5px 0px 15px rgba(57, 255, 20, 0.3);
    }

    /* Sidebar Title & Items */
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] label, 
    section[data-testid="stSidebar"] .stMarkdown {
        color: #39ff14;
        font-weight: bold;
    }

    /* Buttons */
    div.stButton > button {
        background: radial-gradient(circle, #39ff14 0%, #004400 100%);
        color: black !important;
        border: 2px solid #ffffff;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-radius: 50px;
        height: 3em;
        transition: all 0.3s ease;
    }
    
    div.stButton > button:hover {
        box-shadow: 0px 0px 20px #39ff14;
        color: white !important;
    }

    /* Text inputs and text areas */
    input, textarea {
        background-color: #001100 !important;
        border: 1px solid #39ff14 !important;
        color: #39ff14 !important;
        font-weight: bold;
    }

    /* Chat bubbles */
    .stChatMessage {
        background-color: #002200 !important;
        border: 1px solid #39ff14 !important;
        border-radius: 15px !important;
        box-shadow: 0px 0px 10px rgba(57, 255, 20, 0.2);
        color: #39ff14 !important;
    }

    /* Chat messages reversed container */
    div[data-testid="stVerticalBlock"] > div:nth-child(2) {
        flex-direction: column-reverse;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# 🛠️ Session State Initialization
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# ⚙️ Sidebar: Galactic Settings
# -----------------------------
with st.sidebar:
    st.image("https://img.icons8.com/color/512/ben-10.png", width=100)
    st.title("⌚ OMNI-CORE")

    model = st.selectbox("Alien Species (Model)", ["gemma3:latest", "llama3:latest"])
    intensity = st.slider("Energy Level (Temp)", 0.0, 1.5, 0.9)

    st.markdown("---")

    if st.button("♻️ REBOOT OMNITRIX"):
        st.session_state.messages = []
        st.experimental_rerun()

# -----------------------------
# 🏟️ Main Omni-Interface
# -----------------------------
st.title("🟢 OMNITRIX V.10")
st.subheader("User: Ben Tennyson | Status: Online")

# -----------------------------
# Input Form
# -----------------------------
with st.container():
    system_msg = st.text_area(
        "Interface Protocols:",
        value="Speak as the Omnitrix AI. 4 lines only. Be technical but heroic."
    )

    with st.form("omni_form", clear_on_submit=True):
        user_input = st.text_input("INPUT COMMAND:", placeholder="Scan for lifeforms...")
        submit = st.form_submit_button("⚡ INITIALIZE TRANSFORMATION")

# -----------------------------
# Process User Input & Chat
# -----------------------------
if submit and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Accessing Codon Stream..."):
        full_context = [{"role": "system", "content": system_msg}] + st.session_state.messages
        response = ollama.chat(model=model, messages=full_context, options={"temperature": intensity})

        # Enforce 4 lines max
        raw_text = response["message"]["content"]
        lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
        formatted_reply = "\n\n".join(lines[:4])

        st.session_state.messages.append({"role": "assistant", "content": formatted_reply})

# -----------------------------
# Chat History Display (Newest First)
# -----------------------------
st.markdown("---")
for msg in reversed(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
