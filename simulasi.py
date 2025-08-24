import streamlit as st

def show():
    st.header("📐 Simulasi Alat Ukur")
    st.write("Di sini bisa dibuat simulasi penggunaan alat ukur.")
    st.slider("Contoh slider (simulasi panjang benda)", 0, 100, 50)
