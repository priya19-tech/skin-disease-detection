import streamlit as st

# =============================================================
# ⚙️ Page Configuration
# =============================================================
st.set_page_config(page_title="🧬 AI Skin Disease Analyzer", page_icon="🩺", layout="wide")

# =============================================================
# 🎨 Global Black Theme (with Sidebar Matching)
# =============================================================
st.markdown("""
    <style>
        /* === Global Dark Theme === */
        body, .stApp, .main, .block-container {
            background-color: #000000 !important;
            color: #FFFFFF !important;
        }

        h1, h2, h3, h4, h5, p, span, div, label {
            color: #FFFFFF !important;
        }

        /* === Sidebar Styling === */
        section[data-testid="stSidebar"] {
            background-color: #0a0a0a !important;
            border-right: 1px solid #111 !important;
        }

        [data-testid="stSidebarNav"] li a {
            color: #FFFFFF !important;
            font-weight: 500 !important;
            transition: all 0.3s ease;
        }

        [data-testid="stSidebarNav"] li a:hover {
            background-color: #1a1a1a !important;
            color: #00bcd4 !important;
        }

        [data-testid="stSidebarNav"] li a:focus, 
        [data-testid="stSidebarNav"] li a:active {
            color: #4a90e2 !important;
            font-weight: 600 !important;
        }

        /* === Animated Option Cards === */
        .option-card {
            background-color: #111111;
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            border: 1px solid #222222;
            transition: all 0.4s ease;
            box-shadow: 0px 0px 15px rgba(0, 188, 212, 0.1);
            animation: slideUp 0.8s ease forwards;
            opacity: 0;
        }

        .option-card:hover {
            background-color: #161616;
            border: 1px solid #00bcd4;
            transform: translateY(-5px) scale(1.03);
            box-shadow: 0px 0px 25px rgba(0,188,212,0.3);
        }

        /* Animation keyframes */
        @keyframes slideUp {
            0% { transform: translateY(40px); opacity: 0; }
            100% { transform: translateY(0); opacity: 1; }
        }

        /* Buttons */
        .stButton>button {
            background-color: #1a1a1a !important;
            color: #FFFFFF !important;
            border: 1px solid #333 !important;
            border-radius: 8px !important;
            font-weight: 600;
            transition: 0.2s;
        }

        .stButton>button:hover {
            background-color: #00bcd4 !important;
            color: #000000 !important;
            transform: scale(1.05);
        }

        /* Header Animation */
        .main-title {
            text-align: left;
            padding: 20px 0;
            animation: fadeIn 1.2s ease;
        }

        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(-20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        /* Footer */
        hr { border: 1px solid #222 !important; }
        footer { color: #aaaaaa; text-align:center; font-size:13px; margin-top:40px; }
    </style>
""", unsafe_allow_html=True)

# =============================================================
# 🧬 Header
# =============================================================
st.markdown("""
    <div class="main-title">
        <h1>🧬 AI Skin Disease Analyzer</h1>
        <p style="color:#cfcfcf;">Choose what you want to do below</p>
    </div>
""", unsafe_allow_html=True)

# =============================================================
# 📂 Animated Option Cards
# =============================================================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="option-card">
            <h3>🩺 Upload & Detect</h3>
            <p>Analyze skin images using our AI model</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Detection", key="detect"):
        st.switch_page("pages/1_Detect_Skin_Disease.py")

with col2:
    st.markdown("""
        <div class="option-card" style="animation-delay:0.2s;">
            <h3>📖 About</h3>
            <p>Learn how this AI model works</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Go to About", key="about"):
        st.switch_page("pages/2_About.py")

with col3:
    st.markdown("""
        <div class="option-card" style="animation-delay:0.4s;">
            <h3>💬 Contact</h3>
            <p>Reach out for support or feedback</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Contact", key="contact"):
        st.switch_page("pages/3_Contact.py")

# =============================================================
# ⚠️ Footer
# =============================================================
st.markdown("""
<hr>
<footer>
⚠️ For educational use only. Always consult a dermatologist.<br>
© 2025 SkinAI Labs — All Rights Reserved
</footer>
""", unsafe_allow_html=True)
