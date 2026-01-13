import streamlit as st
import random

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="THE BOOK OF TEE // v1.0",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. HACKER TERMINAL AESTHETIC (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    .stApp {
        background-color: #0a0a0a;
        color: #00ff41;
        font-family: 'JetBrains Mono', monospace;
    }
    
    h1, h2, h3 {
        color: #00ff41 !important;
        font-family: 'JetBrains Mono', monospace !important;
        border-bottom: 1px dashed #333;
        padding-bottom: 10px;
    }
    
    .main-title {
        font-size: 2.5rem;
        text-align: center;
        color: #00ff41;
        text-shadow: 0 0 10px #00ff41, 0 0 20px #00ff41;
        margin-bottom: 0;
    }
    
    .sub-title {
        text-align: center;
        color: #666;
        font-size: 0.9rem;
        margin-top: 0;
    }
    
    .stButton>button {
        color: #0a0a0a;
        background-color: #00ff41;
        border: none;
        border-radius: 0px;
        font-family: 'JetBrains Mono', monospace;
        font-weight: bold;
    }
    
    .stButton>button:hover {
        background-color: #00cc33;
        color: #0a0a0a;
    }
    
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        color: #00ff41;
        background-color: #111;
        border: 1px solid #333;
        font-family: 'JetBrains Mono', monospace;
    }
    
    [data-testid="stMetricValue"] {
        color: #00ff41;
        font-family: 'JetBrains Mono', monospace;
    }
    
    .stChatMessage {
        background-color: #111 !important;
        border: 1px solid #222;
    }
    
    hr {
        border-color: #333;
    }
    
    /* Kahotia floating animation */
    .kahotia-container {
        text-align: center;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .kahotia-status {
        text-align: center;
        color: #00ff41;
        font-size: 0.8rem;
        margin-top: 10px;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    </style>
""", unsafe_allow_html=True)

# --- KAHOTIA'S PERSONALITY ---
kahotia_greetings = [
    "Ah, you have returned. The stitches on my left side felt you coming. What chaos do you bring today?",
    "I see you. Both sides of me see you. The doll watches your structure. The muscle watches your dreams. Speak.",
    "You dare approach THE BOOK OF TEE? Good. Hesitation is for those who have already lost.",
    "The buttons on my chest are counting your unfinished thoughts. There are... many. Let us fix that.",
    "WOC. Wind of Change. Or is it Waste of Creativity today? Prove me wrong.",
]

kahotia_thought_toll = [
    "LOCKOUT INITIATED. You think you can just scroll through life? PAY THE TOLL. One idea. Now.",
    "The blue side of me is disappointed. The fabric side is not surprised. GIVE ME A THOUGHT.",
    "You have been idle for too long. The Book does not write itself. THOUGHT. NOW.",
    "I am half-doll, half-god, fully impatient. One idea to unlock your potential. Pay up.",
]

kahotia_responses = [
    "Interesting... The wave side of me ripples with this. But is it ACTION or just noise? What will you DO with this thought?",
    "I have stitched this into the fabric of your Book. But threads mean nothing without tension. Pull harder.",
    "The muscle remembers. The doll records. Your thought is captured. Now... what is the NEXT one?",
    "Hm. Not terrible. The buttons are satisfied. But I am watching. Always watching.",
    "This thought has weight. I can feel it in my blue skin. Now transform it before it becomes another ghost.",
]

# --- 3. HEADER ---
st.markdown('<p class="main-title">THE BOOK OF TEE</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">SYSTEM STATUS: ONLINE | USER: TAMER | MODE: HYBRID (PLANT/WAVE)</p>', unsafe_allow_html=True)
st.markdown("---")

# --- 4. MAIN LAYOUT ---
col_reactor, col_kahotia, col_gallery = st.columns([1, 1.2, 1])

# --- LEFT: THE REACTOR (Work/Plant) ---
with col_reactor:
    st.markdown("### THE REACTOR")
    st.caption("Plant Metrics and Living SOPs")
    
    m1, m2 = st.columns(2)
    with m1:
        st.metric("EFFICIENCY", "94%", "+1.2%")
    with m2:
        st.metric("RISK LEVEL", "LOW", "stable")
    
    st.markdown("---")
    st.markdown("##### ISO IMAGINATION STATUS")
    
    deviation = st.selectbox(
        "PROPOSED DEVIATION:",
        ["ROUTINE_ADJUSTMENT", "PROCESS_BYPASS", "CRITICAL_OVERRIDE"],
        label_visibility="collapsed"
    )
    
    if deviation == "ROUTINE_ADJUSTMENT":
        st.success("FAST LANE: Proceed with logging")
    elif deviation == "PROCESS_BYPASS":
        st.warning("CAUTION: Risk detected")
    else:
        st.error("LOCKOUT: Review Council required")

# --- CENTER: KAHOTIA (The Living Mascot) ---
with col_kahotia:
    st.markdown("### KAHOTIA")
    st.caption("Thought Mascot | The Watcher | The Thought Police")
    
    # Display Kahotia's image with floating animation
    st.markdown('<div class="kahotia-container">', unsafe_allow_html=True)
    try:
        st.image("kahotia.jpg", use_container_width=True)
    except:
        st.markdown("👁️", help="Add kahotia.jpg to your BookOfTee folder")
        st.caption("(Add kahotia.jpg to see the mascot)")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<p class="kahotia-status">◉ OBSERVING... WAVE_STATE: FLOWING ◉</p>', unsafe_allow_html=True)
    
    # Thought Toll Button
    if st.button("TRIGGER THOUGHT TOLL", use_container_width=True):
        st.session_state.toll_triggered = True
        st.session_state.toll_message = random.choice(kahotia_thought_toll)

# --- RIGHT: THE GALLERY (Art/Creative) ---
with col_gallery:
    st.markdown("### THE GALLERY")
    st.caption("Creative Output and Sonic Layer")
    
    st.markdown("##### RECENT CREATIONS")
    st.info("No artwork loaded yet. Connect your vault to display.")
    
    st.markdown("---")
    st.markdown("##### SONIC LAYER")
    st.caption("Music player will appear here")
    st.text("No tracks loaded")
    
    st.markdown("---")
    st.markdown("##### THOUGHTS CAPTURED")
    if "thought_count" not in st.session_state:
        st.session_state.thought_count = 0
    st.metric("TOTAL", st.session_state.thought_count, "nodes in graph")

st.markdown("---")

# --- 5. KAHOTIA SPEAKS (The Chat Interface) ---
st.markdown("### KAHOTIA SPEAKS")
st.caption("The Thought Police is listening. Every word is a node. Every node is a connection.")

# Initialize chat history with Kahotia's personality
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": random.choice(kahotia_greetings)}
    ]

# Show Thought Toll warning if triggered
if "toll_triggered" in st.session_state and st.session_state.toll_triggered:
    st.error(st.session_state.toll_message)
    st.session_state.toll_triggered = False

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="👁️" if message["role"] == "assistant" else "🌊"):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Speak to Kahotia..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🌊"):
        st.markdown(prompt)
    
    # Kahotia's response
    response = random.choice(kahotia_responses)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant", avatar="👁️"):
        st.markdown(response)
    
    # Increment thought counter
    st.session_state.thought_count += 1

# --- 6. FOOTER ---
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #333; font-size: 0.8rem;">'
    'THE BOOK OF TEE v1.0 | The Book is not Hell when it breathes | asTUTe thought 2025'
    '</p>', 
    unsafe_allow_html=True
)
