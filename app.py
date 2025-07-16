import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Simulasi Bahaya Bahan Kimia", page_icon="🧯", layout="centered")

# Data kimia (minimal untuk simulasi, bisa ditambah nanti)
data_kimia = {
    "asam sulfat": {"piktogram": ["🧪 Korosif"], "risiko": ["Korosif", "Iritasi"], "penanganan": "Tambahkan ke air, jangan sebaliknya.", "apd": ["Sarung tangan", "Kacamata", "Masker"]},
    "aseton": {"piktogram": ["🔥 Mudah Terbakar"], "risiko": ["Iritasi", "Anestetik"], "penanganan": "Jauhkan dari api.", "apd": ["Masker uap", "Sarung tangan"]},
    # Tambahkan lebih banyak bahan di sini...
}

# Navigasi via sidebar
page = st.sidebar.radio("📚 Navigasi Aplikasi", ["🏠 Halaman Utama", "🔍 Simulasi Bahan Kimia"])

# =========================
# 🏠 HALAMAN AWAL MODERN
# =========================
if page == "🏠 Halaman Utama":
    st.markdown("""
        <div style='text-align:center'>
            <h1 style='color:#FF4B4B;'>🧯 Simulasi Bahaya Bahan Kimia</h1>
            <p style='font-size:18px; color:gray;'>Kenali bahaya bahan kimia di laboratorium, lindungi diri & lingkungan 💡</p>
        </div>
    """, unsafe_allow_html=True)

    # Section 1: Highlight
    st.markdown("### 🎯 Manfaat Aplikasi Ini")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("🔎 **Pencarian Bebas**\n\nCari bahan kimia dengan nama tanpa harus pilih.")
    with col2:
        st.info("🧪 **Tampilan Edukatif**\n\nTampilkan piktogram, risiko, penanganan, dan APD.")
    with col3:
        st.warning("👩‍🔬 **Edukasi K3**\n\nCocok untuk siswa, mahasiswa, dan teknisi laboratorium.")

    st.markdown("---")

    # Section 2: Aksi lanjut
    st.markdown("""
    <div style='text-align:center'>
        <h3 style='color:#007ACC;'>Sudah siap untuk simulasi?</h3>
        <p>Klik menu <b>🔍 Simulasi Bahan Kimia</b> di sebelah kiri untuk memulai</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    # Section 3: Footer
    st.markdown("""
    <hr>
    <div style='text-align:center; font-size:14px; color:gray;'>
        Aplikasi ini dibuat untuk edukasi keselamatan kerja laboratorium.<br>
        Didukung oleh ❤️ Streamlit.io & Komitmen K3
    </div>
    """, unsafe_allow_html=True)

# =========================
# 🔍 HALAMAN SIMULASI
# =========================
elif page == "🔍 Simulasi Bahan Kimia":
    st.header("🔍 Cari Bahan Kimia")

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
