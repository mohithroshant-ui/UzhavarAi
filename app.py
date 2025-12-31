import streamlit as st
from PIL import Image

st.set_page_config(page_title="Uzhavar AI", layout="wide", page_icon="🌾")

if "language" not in st.session_state:
    st.session_state.language = "English"

def home_page():
    lang = st.sidebar.radio("🌐 Language / மொழி", ["English", "தமிழ்"])
    st.session_state.language = lang

    try:
        banner = Image.open("assets/banner.jpg")
        st.image(banner, use_column_width=True)
    except:
        # Farmer-themed text banner
        st.markdown("""
        <div style="background-color: #f0f8e7; padding: 20px; border-radius: 10px; text-align: center;">
            <h1 style="color: #2e7d32; font-size: 3em;">🌾 Farmer's Best Friend 🌾</h1>
            <p style="color: #388e3c; font-size: 1.2em;">Empowering farmers with AI-driven agricultural insights</p>
            <p style="color: #4caf50;">Harvest smarter, farm better! 🚜🌱</p>
        </div>
        """, unsafe_allow_html=True)

    title = "🌾 Uzhavar AI" if lang=="English" else "🌾 உழவர் AI"
    subtitle = "Smart Farming Tools" if lang=="English" else "நவீன வேளாண் உதவியாளர்"
    desc = "Select a feature from the sidebar." if lang=="English" else "பக்க பட்டியலிலிருந்து ஒரு வசதியைத் தேர்வு செய்யவும்"

    st.markdown(f"<h1 style='text-align:center; color:green'>{title}</h1>", unsafe_allow_html=True)
    st.write(f"### 💡 {subtitle}")
    st.write(desc)

# Define pages
home = st.Page(home_page, title="Home" if st.session_state.language == "English" else "முகப்பு", icon="🏠")
crop_advisor = st.Page("pages/1_Crop_Advisor.py", title="Crop Advisor" if st.session_state.language == "English" else "பயிர் ஆலோசனை", icon="🌱")
weather = st.Page("pages/2_Weather_Update.py", title="Weather Update" if st.session_state.language == "English" else "வானிலை புதுப்பித்தல்", icon="☁️")
fertilizer = st.Page("pages/3_Fertilizer_Guide.py", title="Fertilizer Guide" if st.session_state.language == "English" else "உர வழிகாட்டி", icon="🧪")
dashboard = st.Page("pages/4_History_Dashboard.py", title="History Dashboard" if st.session_state.language == "English" else "வரலாறு டாஷ்போர்டு", icon="📊")

pg = st.navigation([home, crop_advisor, weather, fertilizer, dashboard])

pg.run()
