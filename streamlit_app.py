import streamlit as st
import teori_dan_konsep
import simulasi
import kuis
import analisis_data

st.set_page_config(
    page_title="Lab Pengukuran Virtual - Cahyadi Ariansah",
    page_icon="⚙️",
    layout="wide"
)

# Sidebar menu
menu = st.sidebar.radio("📌 Menu Utama", [
    "🏠 Home",
    "📏 Teori dan Konsep",
    "📐 Simulasi Alat Ukur",
    "🔢 Kuis",
    "📊 Analisis Data"
])

# Halaman utama
if menu == "🏠 Home":
    st.title("⚙️ Lab Pengukuran Virtual")
    st.markdown("""
    Selamat datang di **Lab Pengukuran Virtual by Cahyadi Ariansah** 🎓  

    Gunakan menu di sebelah kiri untuk mengakses:
    - 📏 Teori dan Konsep  
    - 📐 Simulasi Alat Ukur  
    - 🔢 Kuis  
    - 📊 Analisis Data  

    ✍️ *Didesain dan dikembangkan oleh* **Cahyadi Ariansah**
    """)

elif menu == "📏 Teori dan Konsep":
    teori_dan_konsep.show()

elif menu == "📐 Simulasi Alat Ukur":
    simulasi.show()

elif menu == "🔢 Kuis":
    kuis.show()

elif menu == "📊 Analisis Data":
    analisis_data.show()
