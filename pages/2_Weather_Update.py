import streamlit as st
import requests

st.write("Weather Update page loaded")

lang = st.session_state.get('language', 'English')
st.title("🌦 Weather Update" if lang=="English" else "🌦 வானிலை தகவல்")

city = st.text_input("Enter City" if lang=="English" else "நகரத்தை உள்ளீடு செய்யவும்")

if st.button("Check" if lang=="English" else "சரிபார்"):
    try:
        url = f"https://wttr.in/{city}?format=%C+%t+%h"
        response = requests.get(url)
        cond,temp,hum = response.text.split()
        st.info(cond)
        st.success(temp)
        st.warning(hum)
    except Exception as e:
        st.error(f"Failed to get weather: {e}")
