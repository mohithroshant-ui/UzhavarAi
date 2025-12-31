import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import os

st.write("History Dashboard page loaded")

st.title("📊 Profit Dashboard")

db_path = os.path.join(os.getcwd(), "database", "history.db")
conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM history", conn)

if st.button("Clear History"):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM history")
    conn.commit()
    st.success("History cleared!")
    st.rerun()

if df.empty:
    st.info("No data yet")
else:
    st.dataframe(df)
    fig = px.bar(df, x="crop", y="profit", text="profit")
    st.plotly_chart(fig)
