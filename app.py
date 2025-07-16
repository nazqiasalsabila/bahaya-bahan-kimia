import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Simulasi Bahaya Bahan Kimia", page_icon="🧯")

st.title("🧪 Simulasi Bahaya Bahan Kimia")
st.markdown("Cocok untuk edukasi **K3 Laboratorium**. Pilih bahan kimia dan lihat informasi bahayanya!")

# Data bahan kimia
bahan_kimia = {
    "Asam Sulfat (H₂SO₄)": {
        "piktogram": ["🧪 Korosif", "⚠️ Iritasi"],
        "risiko": ["Korosif", "Iritasi saluran pernapasan", "Bahaya kulit & mata"],
        "penanganan": "Gunakan APD lengkap. Tambahkan ke air, jangan sebaliknya. Hindari kontak langsung.",
        "apd": ["🧤 Sarung tangan tahan asam", "🕶️ Kacamata safety", "🥼 Jas lab", "😷 Masker"]
    },
    "Amonia (NH₃)": {
        "piktogram": ["💨 Gas Tekan", "⚠️ Iritasi"],
        "risiko": ["Toksik jika terhirup", "Iritasi mata & kulit", "Korosif"],
        "penanganan": "Gunakan di ruang berventilasi. Hindari menghirup uap. Simpan dalam suhu rendah.",
        "apd": ["😷 Masker gas", "🕶️ Kacamata safety", "🧤 Sarung tangan nitril"]
    },
    "Aseton (C₃H₆O)": {
        "piktogram": ["🔥 Mudah Terbakar", "⚠️ Iritasi"],
        "risiko": ["Mudah terbakar", "Iritasi mata", "Efek anestetik"],
        "penanganan": "Jauhkan dari sumber panas. Tutup rapat. Gunakan di ruang berventilasi.",
        "apd": ["😷 Masker uap organik", "🧤 Sarung tangan nitril", "🕶️ Kacamata"]
    },
}

# Pilihan bahan kimia
pilihan = st.selectbox("🔍 Pilih Bahan Kimia:", list(bahan_kimia.keys()))
data = bahan_kimia[pilihan]

# Piktogram (Emoji Label)
st.subheader("📛 Piktogram Bahaya (GHS)")
for ikon in data["piktogram"]:
    st.markdown(f"- {ikon}")

# Risiko
st.subheader("⚠️ Risiko")
for risiko in data["risiko"]:
    st.markdown(f"- {risiko}")

# Penanganan
st.subheader("🛠️ Cara Penanganan")
st.markdown(f"🔸 {data['penanganan']}")

# APD
st.subheader("🧤 Alat Pelindung Diri (APD)")
for item in data["apd"]:
    st.markdown(f"- {item}")

# Footer
st.markdown("---")
st.markdown("🧯 *Aplikasi edukasi K3 laboratorium - Streamlit.io versi ringan tanpa gambar.*")
