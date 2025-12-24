import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import pandas as pd
import time

# =============================================================
# ⚙️ Page Configuration
# =============================================================
st.set_page_config(page_title="🩺 Detect Skin Disease", page_icon="🧬", layout="centered")

# =============================================================
# 🎨 Global Dark Theme Styling
# =============================================================
st.markdown("""
<style>
/* =========================================================
   🌑 GLOBAL DARK THEME + FILE UPLOADER (PERFECT MATCH)
   ========================================================= */

/* === Global Background & Font === */
body, .stApp, .main, .block-container {
    background-color: #000000 !important;
    color: #FFFFFF !important;
}

h1, h2, h3, h4, h5, p, span, div, label {
    color: #FFFFFF !important;
}

/* === Sidebar === */
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

/* =========================================================
   📁 FILE UPLOADER — DARK CYAN GLOW THEME
   ========================================================= */

/* Outer uploader wrapper */
.stFileUploader > div > div,
.stFileUploader > div > div > div {
    background-color: #0b0b0b !important; /* deep dark background */
    border: 1.5px solid #00bcd4 !important;
    border-radius: 12px !important;
    box-shadow: 0 0 12px rgba(0, 188, 212, 0.35) !important;
    color: #ffffff !important;
    transition: all 0.25s ease-in-out;
    padding: 8px 12px !important;
}

/* Hover effect for entire uploader */
.stFileUploader > div > div:hover,
.stFileUploader > div > div > div:hover {
    border-color: #00eaff !important;
    background-color: #151515 !important;
    box-shadow: 0 0 18px rgba(0, 234, 255, 0.45) !important;
}

/* Inner Drop Zone */
div[data-testid="stFileUploadDropzone"],
.stFileUploader div[data-testid="stFileUploadDropzone"] {
    background-color: transparent !important;
    border: 2px dashed #00bcd4 !important;
    border-radius: 10px !important;
    padding: 18px !important;
    text-align: left !important;
}

/* Text & icon color */
div[data-testid="stFileUploadDropzone"] p,
div[data-testid="stFileUploadDropzone"] span,
div[data-testid="stFileUploadDropzone"] svg,
div[data-testid="stFileUploadDropzone"] svg path {
    color: #d9d9d9 !important;
    fill: #d9d9d9 !important;
    opacity: 0.95 !important;
    font-weight: 500;
}

/* Glow hover effect */
div[data-testid="stFileUploadDropzone"]:hover p,
div[data-testid="stFileUploadDropzone"]:hover span,
div[data-testid="stFileUploadDropzone"]:hover svg {
    color: #00eaff !important;
    fill: #00eaff !important;
    filter: drop-shadow(0 0 6px rgba(0, 234, 255, 0.75));
}

/* === Browse Button === */
.stFileUploader button,
.stFileUploader > div > button {
    background-color: #00bcd4 !important;
    color: #000000 !important;
    font-weight: 700 !important;
    border-radius: 8px !important;
    border: none !important;
    padding: 8px 14px !important;
    box-shadow: 0 6px 18px rgba(0,188,212,0.32) !important;
    transition: transform .15s ease, box-shadow .15s ease;
}

.stFileUploader button:hover,
.stFileUploader > div > button:hover {
    background-color: #00eaff !important;
    transform: translateY(-2px) scale(1.02);
    box-shadow: 0 10px 26px rgba(0,234,255,0.40) !important;
}

/* Uploaded file row */
div[role="listitem"], .stFileUploader [role="listitem"] {
    background-color: #111111 !important;
    border: 1px solid #222 !important;
    color: #eaeaea !important;
    border-radius: 8px !important;
    padding: 8px 10px !important;
    margin-top: 10px !important;
    box-shadow: 0 6px 14px rgba(0,0,0,0.45) !important;
}

/* Remove “X” button style */
div[role="listitem"] button, .stFileUploader [role="listitem"] button {
    color: #ffffff !important;
    background: transparent !important;
    border: none !important;
}

/* Ensure text visibility */
.stFileUploader small, .stFileUploader a {
    color: #cfcfcf !important;
}

/* No bright outline on focus */
.stFileUploader :focus {
    outline: none !important;
    box-shadow: 0 0 12px rgba(0,188,212,0.18) !important;
}

/* =========================================================
   💡 Buttons, Info Boxes, and Footer
   ========================================================= */
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

/* Info boxes */
.dark-box {
    background-color: #111111;
    border: 1px solid #222222;
    border-radius: 12px;
    padding: 25px;
    margin-top: 25px;
    box-shadow: 0px 0px 15px rgba(0,188,212,0.2);
}

.dark-box:hover {
    background-color: #161616;
    transform: translateY(-3px);
    transition: 0.3s;
}

/* Footer */
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
# 🧬 Header
# =============================================================
st.title("🩺 AI Skin Disease & Type Detection")
st.write("Upload a skin image to predict possible diseases and get personalized care suggestions.")

# =============================================================
# 🧠 Load Models
# =============================================================
@st.cache_resource
def load_disease_model():
    return load_model("final_skin_model.1.keras", compile=False)

@st.cache_resource
def load_skin_type_model():
    return load_model("skin_type_model.keras", compile=False)

try:
    disease_model = load_disease_model()
    skin_type_model = load_skin_type_model()
    MODELS_LOADED = True
except Exception:
    st.error("⚠️ Could not load model files. Please verify paths.")
    MODELS_LOADED = False

# =============================================================
# 📋 Classes
# =============================================================
disease_classes = [
    'Acne and Rosacea Photos', 'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions',
    'Atopic Dermatitis Photos', 'Cellulitis Impetigo and other Bacterial Infections',
    'Eczema Photos', 'Exanthems and Drug Eruptions', 'Herpes HPV and other STDs Photos',
    'Light Diseases and Disorders of Pigmentation', 'Lupus and other Connective Tissue diseases',
    'Melanoma Skin Cancer Nevi and Moles', 'Poison Ivy Photos and other Contact Dermatitis',
    'Psoriasis pictures Lichen Planus and related diseases', 'Seborrheic Keratoses and other Benign Tumors',
    'Systemic Disease', 'Tinea Ringworm Candidiasis and other Fungal Infections',
    'Urticaria Hives', 'Vascular Tumors', 'Vasculitis Photos', 'Warts Molluscum and other Viral Infections'
]

skin_type_classes = ["Oily", "Dry", "Normal"]

# =============================================================
# 💡 Recommendation Mapping
# =============================================================
recommendations = {
    "Acne and Rosacea Photos": {
        "Oily": "Use salicylic acid or niacinamide serums; avoid comedogenic moisturizers. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Use hydrating serums with hyaluronic acid; avoid harsh cleansers. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Use balanced niacinamide-based serum; maintain gentle cleansing routine. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions": {
        "Oily": "Avoid sun exposure; use gentle sunscreen. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Apply SPF 50 sunscreen; avoid harsh chemicals. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Use broad-spectrum sunscreen daily. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Atopic Dermatitis Photos": {
        "Oily": "Use lightweight moisturizers; avoid alcohol-based products. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Apply thick emollients like CeraVe or Eucerin twice daily. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Use gentle unscented moisturizers; maintain hydration. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Cellulitis Impetigo and other Bacterial Infections": {
        "Oily": "Keep area clean; avoid scratching. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Gently cleanse and moisturize surrounding skin. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Maintain hygiene and monitor for worsening. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Eczema Photos": {
        "Oily": "Use ceramide-based moisturizers; avoid alcohol-based products. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Apply thick moisturizers like CeraVe or Eucerin twice daily. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Use light unscented moisturizer; keep skin hydrated. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Exanthems and Drug Eruptions": {
        "Oily": "Avoid irritants; monitor rash. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Keep skin moisturized; avoid hot water. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Avoid allergenic products; monitor symptoms. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Herpes HPV and other STDs Photos": {
        "Oily": "Avoid touching lesions; maintain hygiene. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Use gentle cleansers; keep area dry. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Avoid scratching; maintain hygiene. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Light Diseases and Disorders of Pigmentation": {
        "Oily": "Apply broad-spectrum sunscreen; avoid harsh bleaching products. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Use moisturizing sunscreen; avoid irritants. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Use sunscreen regularly; maintain gentle skin care. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Lupus and other Connective Tissue diseases": {
        "Oily": "Use gentle skincare; avoid prolonged sun exposure. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Apply moisturizing sunscreen; avoid irritants. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Maintain gentle skin care routine; monitor symptoms. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Melanoma Skin Cancer Nevi and Moles": {
        "Oily": "Avoid sunburn; monitor moles for changes. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Apply SPF 50 sunscreen; avoid irritants. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Check moles regularly; use broad-spectrum sunscreen. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Poison Ivy Photos and other Contact Dermatitis": {
        "Oily": "Wash affected area immediately; avoid scratching. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Apply soothing moisturizers; avoid hot water. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Clean affected area; monitor for spread. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Psoriasis pictures Lichen Planus and related diseases": {
        "Oily": "Use medicated coal tar or salicylic acid creams; mild cleanser. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Use thick emollients; gentle exfoliation; avoid hot water. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Use balanced moisturizing creams; apply prescribed topical corticosteroids. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Seborrheic Keratoses and other Benign Tumors": {
        "Oily": "Avoid harsh scrubs; maintain gentle cleansing. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Use moisturizing creams; monitor growth. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Keep skin clean; avoid irritation. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Systemic Disease": {
        "Oily": "Maintain hygiene; monitor skin changes. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Apply gentle moisturizers; avoid irritants. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Observe symptoms; maintain skincare routine. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Tinea Ringworm Candidiasis and other Fungal Infections": {
        "Oily": "Use antifungal creams (clotrimazole, ketoconazole); keep area dry. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Use antifungal lotion; moisturize surrounding skin lightly. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Apply antifungal ointment; maintain hygiene and dryness. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Urticaria Hives": {
        "Oily": "Avoid triggers; keep skin cool. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Apply soothing moisturizers; avoid harsh soaps. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Monitor symptoms; avoid allergenic products. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Vascular Tumors": {
        "Oily": "Avoid trauma to lesions; maintain hygiene. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Use gentle moisturizers; monitor changes. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Keep skin clean; observe for growth. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Vasculitis Photos": {
        "Oily": "Avoid irritants; monitor affected areas. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Apply moisturizing creams; avoid harsh products. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Observe skin; maintain gentle care. ⚠️ Consult a dermatologist for proper evaluation."
    },
    "Warts Molluscum and other Viral Infections": {
        "Oily": "Avoid picking; maintain hygiene. ⚠️ Consult a dermatologist for proper evaluation.",
        "Dry": "Use gentle cleansing; monitor lesions. ⚠️ Consult a dermatologist for proper evaluation.",
        "Normal": "Keep area clean; avoid scratching. ⚠️ Consult a dermatologist for proper evaluation."
    }
}


# =============================================================
# 📤 Upload and Predict
# =============================================================
if MODELS_LOADED:
    uploaded_file = st.file_uploader("📸 Upload a skin image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption="📸 Uploaded Image", use_container_width=True)

        # === Preprocessing ===
        img_resized = img.resize((192, 192))
        img_array = np.expand_dims(image.img_to_array(img_resized), axis=0) / 255.0

        with st.spinner("🧬 Analyzing image... Please wait"):
            time.sleep(1.5)

        # === Predictions ===
        disease_preds = disease_model.predict(img_array)[0]
        top_indices = disease_preds.argsort()[-5:][::-1]
        top_classes = [disease_classes[i] for i in top_indices]
        top_probs = [disease_preds[i] * 100 for i in top_indices]

        skin_type_preds = skin_type_model.predict(img_array)[0]
        skin_type_result = skin_type_classes[np.argmax(skin_type_preds)]
        skin_type_conf = np.max(skin_type_preds) * 100

        # === Results ===
        st.markdown('<div class="dark-box">', unsafe_allow_html=True)
        st.subheader("🧠 Prediction Results")
        st.write(f"**Skin Type:** {skin_type_result} ({skin_type_conf:.2f}%)")
        st.write(f"**Most Likely Disease:** {top_classes[0]}")
        st.markdown('</div>', unsafe_allow_html=True)

        # === Confidence Chart ===
        st.markdown('<div class="dark-box">', unsafe_allow_html=True)
        st.subheader("📊 Top 5 Predictions")
        st.bar_chart(pd.DataFrame({"Disease": top_classes, "Confidence (%)": top_probs}).set_index("Disease"))
        for cls, prob in zip(top_classes, top_probs):
            st.write(f"- **{cls}** — {prob:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)

        # === 💡 Personalized Recommendation ===
        disease_key = top_classes[0]
        care_text = recommendations.get(disease_key, {}).get(skin_type_result, 
            "⚠️ Consult a dermatologist for personalized care.")

        st.markdown('<div class="dark-box">', unsafe_allow_html=True)
        st.subheader(f"💡 Care Suggestions for {skin_type_result} Skin ({disease_key})")
        st.write(care_text)
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.info("📥 Please upload an image to start detection.")

# =============================================================
# ⚠️ Footer
# =============================================================
st.markdown("""
<hr>
<footer>
⚠️ This AI tool is for educational use only.<br>
Always consult a dermatologist.<br>
© 2025 SkinAI Labs — All Rights Reserved
</footer>
""", unsafe_allow_html=True)
