import streamlit as st

def show():
    st.header("🔢 Kuis Pengukuran")
    st.write("Jawablah pertanyaan berikut:")

    q1 = st.radio("1. Apa yang dimaksud dengan pengukuran?", [
        "Membandingkan besaran dengan satuan",
        "Mengira-ngira nilai suatu benda",
        "Menebak panjang atau massa"
    ])

    if q1 == "Membandingkan besaran dengan satuan":
        st.success("✅ Benar!")
    elif q1 != "":
        st.error("❌ Salah, coba lagi.")
