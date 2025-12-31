import streamlit as st
import pickle
import sqlite3
import os

crop_profit = {
    "rice": {"price": 28, "yield": 2500},
    "maize": {"price": 22, "yield": 1800},
    "banana": {"price": 35, "yield": 30000},
    "mango": {"price": 50, "yield": 10000},
    "cotton": {"price": 65, "yield": 2000},
    "coffee": {"price": 140, "yield": 800},
}

st.write("Crop Advisor page loaded")

lang = st.session_state.get('language', 'English')

model_path = os.path.join(os.getcwd(), "model", "crop_model.pkl")
try:
    model = pickle.load(open(model_path, "rb"))
    st.write("Model loaded successfully")
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()

conn = sqlite3.connect(os.path.join(os.getcwd(), "database", "history.db"))
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS history(crop TEXT, profit INT)")
conn.commit()

st.title("🌾 Crop Advisor" if lang=="English" else "🌾 பயிர் ஆலோசனை")

N = st.slider("Nitrogen (N)", 0, 200, 50)
P = st.slider("Phosphorus (P)", 0, 200, 50)
K = st.slider("Potassium (K)", 0, 200, 50)
temp = st.slider("Temperature (°C)", 0.0, 50.0, 25.0)
hum = st.slider("Humidity (%)", 0.0, 100.0, 50.0)
ph = st.slider("pH", 0.0, 14.0, 6.5)
rain = st.slider("Rainfall (mm)", 0.0, 400.0, 100.0)

if st.button("Predict 🌱"):
    try:
        crop = model.predict([[N,P,K,temp,hum,ph,rain]])[0]
        st.success(f"Best Crop: {crop}")

        profit = crop_profit.get(crop, {"price": 0, "yield": 0})["price"] * crop_profit.get(crop, {"price": 0, "yield": 0})["yield"]
        cursor.execute("INSERT INTO history VALUES(?,?)", (crop, profit))
        conn.commit()
        st.info(f"Estimated Profit: ₹{profit:,}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
