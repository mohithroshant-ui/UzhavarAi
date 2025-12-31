import streamlit as st

st.write("Fertilizer Guide page loaded")

lang = st.session_state.get('language', 'English')

st.title("🧪 Fertilizer Guide" if lang=="English" else "🧪 உர வழிகாட்டி")

data={
    "Rice":"Urea + DAP + MOP",
    "Maize":"Urea + SSP + Gypsum",
    "Cotton":"NPK + Compost"
}

crop = st.selectbox("Select Crop" if lang=="English" else "பயிரைத் தேர்ந்தெடுக்கவும்", list(data.keys()))

if st.button("Guide" if lang=="English" else "வழிகாட்டி"):
    st.success(data[crop])
