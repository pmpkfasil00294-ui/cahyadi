import streamlit as st
import pandas as pd

def show():
    st.header("📊 Analisis Data Pengukuran")
    st.write("Upload data hasil pengukuran (CSV):")

    file = st.file_uploader("Upload file CSV", type=["csv"])
    if file:
        df = pd.read_csv(file)
        st.dataframe(df)
        st.write("📈 Statistik Deskriptif:")
        st.write(df.describe())
