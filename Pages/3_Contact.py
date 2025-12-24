import streamlit as st

st.set_page_config(page_title="💬 Contact & Support", page_icon="💡", layout="centered")

# =============================================================
# 🌙 Global Dark Theme (matches all pages)
# =============================================================
st.markdown("""
    <style>
        body, .stApp, .main, .block-container {
            background-color: #000000 !important;
            color: #ffffff !important;
        }

        h1, h2, h3, h4, h5, p, span, div, label {
            color: #ffffff !important;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #0a0a0a !important;
            border-right: 1px solid #111 !important;
        }
        [data-testid="stSidebarNav"] li a {
            color: #ffffff !important;
            font-weight: 500 !important;
        }
        [data-testid="stSidebarNav"] li a:hover {
            background-color: #1a1a1a !important;
            color: #00bcd4 !important;
        }

        /* Contact Card */
        .contact-card {
            background-color: #0d0d0d !important;
            border-radius: 15px;
            padding: 25px;
            border: 1px solid #1a1a1a;
            box-shadow: 0px 0px 10px rgba(0, 188, 212, 0.15);
            margin-top: 20px;
        }
        .contact-card:hover {
            box-shadow: 0px 0px 20px rgba(0, 188, 212, 0.3);
            background-color: #111111 !important;
        }

        /* Inner info box */
        .inner-box {
            background-color: #1a1a1a !important;
            color: #ffffff !important;
            padding: 20px;
            border-radius: 10px;
            margin-top: 15px;
            border: 1px solid #333333;
        }

        /* Links */
        a {
            color: #00bcd4 !important;
            text-decoration: none !important;
            font-weight: 500 !important;
        }
        a:hover {
            text-decoration: underline !important;
            color: #4a90e2 !important;
        }

        /* Buttons */
        .stButton>button {
            background-color: #1a1a1a !important;
            color: white !important;
            border-radius: 8px !important;
            border: 1px solid #333 !important;
        }
        .stButton>button:hover {
            background-color: #00bcd4 !important;
            color: #000 !important;
            transform: scale(1.05);
        }

        hr { border: 1px solid #222 !important; }
    </style>
""", unsafe_allow_html=True)

# =============================================================
# 💬 Header
# =============================================================
st.markdown("""
    <div style="text-align:center; padding:20px;">
        <h1>💬 Contact & Support</h1>
        <p style="color:#cccccc;">If you have any questions, feedback, or collaboration requests, we’d love to hear from you.</p>
    </div>
""", unsafe_allow_html=True)

# =============================================================
# 📬 Contact Card
# =============================================================
st.markdown("""
    <div class="contact-card">
        <h3>📬 Get in Touch</h3>
        <p><b>Email:</b> <a href="mailto:skincareailab@gmail.com">support@skincareai-labs.com</a></p>
        <p><b>Address:</b> Skin CareAI Labs,Chennai,India</p>
        <p><b>Contact No:</b> 659-624</p>
    </div>
""", unsafe_allow_html=True)

# =============================================================
# 🌐 Social Links Section (not shown as code anymore)
# =============================================================
st.markdown("""
    <div class="inner-box">
        <h4>🌐 Connect With Us</h4>
        <p>
            <a href="https://instagram.com/" target="_blank">📸 Instagram</a>
        </p>
        <p style="color:#aaaaaa;">Follow us on our journey in AI & healthcare innovation.</p>
    </div>
""", unsafe_allow_html=True)

# =============================================================
# ⚠️ Footer
# =============================================================
st.markdown("""
<hr style="border:1px solid #222;">
<p style="text-align:center; color:#aaaaaa; font-size:14px;">
⚠️ This AI tool is for educational purposes only. Always consult a dermatologist.<br>
© 2025 SkinAI Labs — All Rights Reserved
</p>
""", unsafe_allow_html=True)
