import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Simulasi Bahaya Bahan Kimia", page_icon="🧯", layout="centered")

# Tampilan awal yang menarik
st.markdown("""
<style>
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #FF4B4B;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #6C6C6C;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🧪 Simulasi Bahaya Bahan Kimia</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Edukasi K3 Laboratorium – Kenali Bahaya, Lindungi Diri!</div>', unsafe_allow_html=True)
st.markdown("---")

# Data lebih dari 20 bahan kimia
data_kimia = {
    "Asam Sulfat (H₂SO₄)": {"piktogram": ["🧪 Korosif"], "risiko": ["Korosif", "Iritasi"], "penanganan": "Tambahkan ke air, jangan sebaliknya.", "apd": ["Sarung tangan", "Kacamata", "Masker"]},
    "Aseton (C₃H₆O)": {"piktogram": ["🔥 Mudah Terbakar"], "risiko": ["Iritasi", "Anestetik"], "penanganan": "Jauhkan dari api.", "apd": ["Masker uap", "Sarung tangan"]},
    "Amonia (NH₃)": {"piktogram": ["💨 Gas", "⚠️ Iritasi"], "risiko": ["Toksik", "Korosif"], "penanganan": "Gunakan di tempat berventilasi.", "apd": ["Masker", "Sarung tangan"]},
    "Etanol (C₂H₅OH)": {"piktogram": ["🔥 Mudah Terbakar"], "risiko": ["Iritasi ringan", "Nyala tak terlihat"], "penanganan": "Tutup rapat wadah.", "apd": ["Sarung tangan", "Masker"]},
    "Formaldehida (HCHO)": {"piktogram": ["☠️ Toksik", "⚠️ Iritasi"], "risiko": ["Karsinogenik", "Iritasi mata"], "penanganan": "Gunakan lemari asam.", "apd": ["Masker", "Kacamata"]},
    "NaOH (Natrium Hidroksida)": {"piktogram": ["🧪 Korosif"], "risiko": ["Korosif parah"], "penanganan": "Hindari kontak langsung.", "apd": ["Sarung tangan", "Jas lab"]},
    "HCl (Asam Klorida)": {"piktogram": ["🧪 Korosif"], "risiko": ["Iritasi dan luka bakar"], "penanganan": "Gunakan pelindung lengkap.", "apd": ["Masker", "Kacamata"]},
    "Benzena (C₆H₆)": {"piktogram": ["☠️ Toksik", "🔥"], "risiko": ["Karsinogenik", "Mudah menguap"], "penanganan": "Hindari hirupan.", "apd": ["Masker uap", "Kacamata"]},
    "Toluena (C₇H₈)": {"piktogram": ["🔥", "⚠️"], "risiko": ["Neurotoksin ringan"], "penanganan": "Ventilasi cukup.", "apd": ["Masker", "Sarung tangan"]},
    "Klorin (Cl₂)": {"piktogram": ["☠️", "💨"], "risiko": ["Beracun", "Iritasi saluran nafas"], "penanganan": "Hindari ruangan tertutup.", "apd": ["Masker gas"]},
    "Hidrogen Peroksida (H₂O₂)": {"piktogram": ["🧪", "🔥"], "risiko": ["Oksidator", "Korosif"], "penanganan": "Jauhkan dari bahan mudah terbakar.", "apd": ["Kacamata", "Sarung tangan"]},
    "Nitrobenzena": {"piktogram": ["☠️", "⚠️"], "risiko": ["Toksik", "Darah & hati"], "penanganan": "Ventilasi kuat.", "apd": ["Masker", "Sarung tangan"]},
    "Asam Asetat": {"piktogram": ["🧪", "⚠️"], "risiko": ["Iritasi kulit & mata"], "penanganan": "Gunakan dalam lemari asam.", "apd": ["Sarung tangan", "Masker"]},
    "Asam Nitrat": {"piktogram": ["🧪", "🔥"], "risiko": ["Oksidator", "Korosif tinggi"], "penanganan": "Hindari panas & logam.", "apd": ["Kacamata", "Sarung tangan"]},
    "Isopropil Alkohol": {"piktogram": ["🔥"], "risiko": ["Mudah terbakar"], "penanganan": "Jauhkan dari nyala api.", "apd": ["Masker", "Sarung tangan"]},
    "Kalium Permanganat": {"piktogram": ["🔥", "⚠️"], "risiko": ["Oksidator kuat"], "penanganan": "Simpan jauh dari bahan organik.", "apd": ["Jas lab", "Kacamata"]},
    "Metanol": {"piktogram": ["🔥", "☠️"], "risiko": ["Beracun jika tertelan", "Kebutaan"], "penanganan": "Hindari inhalasi & kontak.", "apd": ["Masker", "Sarung tangan"]},
    "Asam Fosfat": {"piktogram": ["🧪"], "risiko": ["Korosif ringan"], "penanganan": "Simpan dalam wadah tertutup.", "apd": ["Sarung tangan", "Kacamata"]},
    "Karbon Tetraklorida": {"piktogram": ["☠️", "⚠️"], "risiko": ["Bahaya hati", "Uap beracun"], "penanganan": "Ventilasi & masker gas.", "apd": ["Masker uap", "Kacamata"]},
    "Phenol": {"piktogram": ["🧪", "☠️"], "risiko": ["Beracun dan korosif"], "penanganan": "Gunakan APD lengkap.", "apd": ["Masker", "Kacamata", "Sarung tangan"]},
    "Dietil Eter": {"piktogram": ["🔥", "⚠️"], "risiko": ["Mudah meledak", "Uap mudah menyala"], "penanganan": "Jauhkan dari listrik statis.", "apd": ["Kacamata", "Masker"]},
}

# Pilih bahan kimia
pilih = st.selectbox("🔍 Pilih Bahan Kimia:", list(data_kimia.keys()))
info = data_kimia[pilih]

# Tampilkan hasil
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

st.markdown("---")
st.markdown("🧯 *Aplikasi edukasi keselamatan bahan kimia oleh Streamlit.io – versi tanpa gambar.*")
