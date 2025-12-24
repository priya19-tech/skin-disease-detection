import streamlit as st

# =============================================================
# ⚙️ Page Config
# =============================================================
st.set_page_config(page_title="📘 About | AI Skin Analyzer", page_icon="📖", layout="centered")

# =============================================================
# 🎨 Global Unified Black Theme
# =============================================================
st.markdown("""
    <style>
        /* === Global Background & Font === */
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

        /* === Buttons === */
        .stButton>button {
            background-color: #1a1a1a !important;
            color: #FFFFFF !important;
            border: 1px solid #333 !important;
            border-radius: 8px !important;
            font-weight: 600;
        }

        .stButton>button:hover {
            background-color: #00bcd4 !important;
            color: #000000 !important;
            transform: scale(1.05);
            transition: 0.2s;
        }

        /* === Cards / Info Boxes === */
        .info-box, .contact-card, .card {
            background-color: #111111 !important;
            border: 1px solid #222222 !important;
            border-radius: 12px !important;
            color: #FFFFFF !important;
            padding: 25px;
            margin-top: 25px;
            box-shadow: 0px 0px 15px rgba(74, 144, 226, 0.1);
        }

        .info-box:hover, .contact-card:hover, .card:hover {
            background-color: #161616 !important;
            box-shadow: 0px 0px 15px rgba(0,188,212,0.2);
            transform: translateY(-3px);
            transition: 0.3s;
        }

        /* === Footer === */
        footer {
            color: #aaaaaa !important;
            text-align: center;
            font-size: 13px;
            margin-top: 40px;
        }

        hr { border: 1px solid #222 !important; }
    </style>
""", unsafe_allow_html=True)

# =============================================================
# 📖 About Section
# =============================================================
st.title("📘 About the AI Skin Analyzer")
st.write("A deep-learning powered tool for skin disease classification and skincare recommendations.")

st.markdown("""
<div class="info-box">
    <h3>🧬 What This Tool Does</h3>
    <p>This AI system analyzes skin images to identify potential conditions using advanced convolutional neural networks (CNNs). 
    It also detects your skin type — oily, dry, or normal — and offers care suggestions accordingly.</p>
</div>

<div class="info-box">
    <h3>⚙️ How It Works</h3>
    <ul>
        <li>Upload a skin image (JPEG or PNG format).</li>
        <li>The AI model processes it and predicts the top 5 most likely conditions.</li>
        <li>It identifies your skin type and provides care recommendations.</li>
    </ul>
</div>

<div class="info-box">
    <h3>📊 Technology Behind</h3>
    <p>Built using <b>TensorFlow</b> and <b>Keras</b>, the system employs a fine-tuned CNN model trained on thousands of dermatology images. 
    It uses <b>Streamlit</b> for web deployment and offers real-time visualization of predictions.</p>
</div>

<div class="info-box">
    <h3>⚠️ Disclaimer</h3>
    <p>This AI tool is for educational and informational use only. It is not a substitute for professional medical advice, diagnosis, or treatment. 
    Always consult a certified dermatologist for clinical evaluation.</p>
</div>
""", unsafe_allow_html=True)

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
