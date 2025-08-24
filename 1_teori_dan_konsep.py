import streamlit as st

def show():
    st.header("📏 Teori dan Konsep Pengukuran")
    st.write("""
    Teori pengukuran mencakup:
    - Definisi pengukuran
    - Jenis alat ukur
    - Prinsip kalibrasi
    - Kesalahan pengukuran (systematic & random error)
    """)


Sistem Internasional (SI) digunakan untuk menyamakan acuan satuan di seluruh dunia.
Contoh:
- Panjang: meter (m)
- Massa: kilogram (kg)
- Waktu: sekon (s)
- suhu : kelvin (K)
- Intensitas cahaya : candela (cd)
- Kuat arus : Ampere (A)
- Jumlah zat : Mol (mol)
""")

st.subheader("3. Angka Penting")
st.latex(r"\text{Ketelitian} = \pm \frac{\text{Skala terkecil}}{2}")

st.write("""
**Aturan angka penting:**
1. Semua angka bukan nol adalah penting.
2. Nol di antara angka bukan nol adalah penting.
3. Nol di awal bilangan tidak penting.
4. Nol di akhir bilangan desimal adalah penting.
""")

st.subheader("4. Rumus Dasar Fisika Terkait Pengukuran")
st.latex(r"\text{Kecepatan} \ (v) = \frac{\text{jarak} \ (s)}{\text{waktu} \ (t)}")
st.latex(r"\text{Volume balok} = p \times l \times t")

st.latex(r"\text{Volume silinder} = \pi r^2 t")
