import streamlit as st
import teori_dan_konsep  # mengimpor file eksternal

st.set_page_config(page_title="Lab Pengukuran Virtual - Cahyadi Ariansah", page_icon="⚙️")

# Sidebar menu
menu = st.sidebar.radio("📌 Menu", [
    "🏠 Home",
    "📏 Teori dan Konsep"
])

# Halaman utama
if menu == "🏠 Home":
    st.title("⚙️ Lab Pengukuran Virtual")
    st.markdown("""
    Selamat datang di **Lab Pengukuran Virtual by Cahyadi Ariansah** 🎓  

    Gunakan menu di sebelah kiri untuk mengakses:
    - 📏 Teori dan Konsep

    ✍️ *Didesain dan dikembangkan oleh* **Cahyadi Ariansah**
    """)

elif menu == "📏 Teori dan Konsep":
    teori_dan_konsep.show()
