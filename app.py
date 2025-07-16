import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Simulasi Bahaya Bahan Kimia", page_icon="🧯")

# Dataset bahan kimia
data_kimia = {
    "asam sulfat": {"piktogram": ["🧪 Korosif"], "risiko": ["Korosif", "Iritasi"], "penanganan": "Tambahkan ke air, jangan sebaliknya.", "apd": ["Sarung tangan", "Kacamata", "Masker"]},
    "aseton": {"piktogram": ["🔥 Mudah Terbakar"], "risiko": ["Iritasi", "Anestetik"], "penanganan": "Jauhkan dari api.", "apd": ["Masker uap", "Sarung tangan"]},
    "amonia": {"piktogram": ["💨 Gas", "⚠️ Iritasi"], "risiko": ["Toksik", "Korosif"], "penanganan": "Gunakan di tempat berventilasi.", "apd": ["Masker", "Sarung tangan"]},
    "etanol": {"piktogram": ["🔥 Mudah Terbakar"], "risiko": ["Iritasi ringan", "Nyala tak terlihat"], "penanganan": "Tutup rapat wadah.", "apd": ["Sarung tangan", "Masker"]},
    "formaldehida": {"piktogram": ["☠️ Toksik", "⚠️ Iritasi"], "risiko": ["Karsinogenik", "Iritasi mata"], "penanganan": "Gunakan lemari asam.", "apd": ["Masker", "Kacamata"]},
    # tambahkan hingga 20+ bahan lainnya ...
}

# Sidebar untuk navigasi
page = st.sidebar.radio("Navigasi", ["🏠 Halaman Utama", "🔍 Simulasi Bahan Kimia"])

# ========================
# 🏠 HALAMAN 1: INTRO
# ========================
if page == "🏠 Halaman Utama":
    st.markdown("""
        <h1 style='text-align: center; color: crimson;'>🧪 Simulasi Bahaya Bahan Kimia</h1>
        <p style='text-align: center; font-size:18px;'>Aplikasi edukasi K3 untuk mengenal bahan kimia berbahaya di laboratorium.</p>
        <hr>
    """, unsafe_allow_html=True)

    st.image("https://cdn-icons-png.flaticon.com/512/2913/2913461.png", width=200)

    st.markdown("""
    ### 🔎 Apa yang bisa kamu lakukan?
    - Cari bahan kimia berdasarkan **namanya**
    - Lihat **piktogram**, **risiko**, **penanganan**, dan **APD**
    - Cocok untuk edukasi siswa, mahasiswa, dan teknisi lab

    > Klik menu **"Simulasi Bahan Kimia"** di sebelah kiri untuk mulai
    """)

# ========================
# 🔍 HALAMAN 2: SIMULASI
# ========================
elif page == "🔍 Simulasi Bahan Kimia":
    st.header("🔍 Cari Bahan Kimia")

    # Input nama bahan kimia
    keyword = st.text_input("Masukkan nama bahan kimia (contoh: asam sulfat)").lower()

    if keyword:
        if keyword in data_kimia:
            info = data_kimia[keyword]

            st.subheader("📛 Piktogram Bahaya")
            st.markdown(" ".join(info["piktogram"]))

            st.subheader("⚠️ Risiko")
            for r in info["risiko"]:
                st.markdown(f"- {r}")

            st.subheader("🛠️ Cara Penanganan")
            st.markdown(f"🔸 {info['penanganan']}")

            st.subheader("🧤 Alat Pelindung Diri (APD)")
            for a in info["apd"]:
                st.markdown(f"- {a}")
        else:
            st.error("❌ Bahan kimia tidak ditemukan. Coba lagi dengan nama lain.")
