import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Simulasi Bahaya Bahan Kimia", page_icon="🛯", layout="centered")

# Dataset 100 bahan kimia nyata
import random

piktogram_list = ["🧪 Korosif", "🔥 Mudah Terbakar", "☠️ Toksik", "⚠️ Iritasi", "💨 Gas"]
risiko_list = ["Korosif", "Iritasi", "Toksik", "Karsinogenik", "Mudah menguap", "Bahaya kulit", "Reaktif", "Oksidator"]
penanganan_list = [
    "Gunakan APD lengkap.",
    "Jauhkan dari sumber panas.",
    "Simpan dalam wadah tertutup.",
    "Gunakan di tempat berventilasi.",
    "Gunakan lemari asam.",
    "Tambahkan ke air, jangan sebaliknya."
]
apd_list = [
    ["Sarung tangan", "Kacamata", "Masker"],
    ["Masker gas", "Jas lab"],
    ["Sarung tangan nitril", "Kacamata safety"],
    ["Masker uap organik", "Pelindung wajah"],
    ["Kacamata", "Jas lab", "Sarung tangan"]
]

# Nama-nama bahan kimia nyata (100 contoh)
nama_kimia_asli = [
    "asam sulfat", "asam klorida", "asam nitrat", "asam asetat", "asam fosfat",
    "etanol", "metanol", "isopropil alkohol", "benzena", "toluena",
    "xilena", "kloroform", "asetaldehida", "formaldehida", "aseton",
    "dietil eter", "etil asetat", "n-heksana", "karbon tetraklorida", "klorin",
    "amonia", "natrium hidroksida", "kalium hidroksida", "natrium hipoklorit", "kalium permanganat",
    "hidrogen peroksida", "tembaga sulfat", "feri klorida", "natrium karbonat", "natrium bikarbonat",
    "kalsium karbonat", "magnesium sulfat", "aluminium klorida", "nitril", "merkuri",
    "timah", "seng", "nikel", "besi", "kromium",
    "plumbum", "arsenik", "selenium", "boron", "litium",
    "barium", "stronsium", "bismut", "fluorin", "iodin",
    "bromin", "oksigen", "karbon dioksida", "sulfur dioksida", "nitrogen dioksida",
    "etanolamin", "dimetilformamida", "asetat amonia", "etanolamina", "trietanolamina",
    "trikloroetilena", "asetonitril", "fenol", "resorsinol", "anilin",
    "pikrins", "hidrazin", "nitrobenzena", "aseton peroksida", "perklorat",
    "natrium azida", "bromat", "iodat", "hipoklorit", "klorat",
    "klorida ferrik", "ferrosianida", "kalium sianida", "n-butanol", "tert-butanol",
    "metil etil keton", "isobutil alkohol", "n-propanol", "dimetil sulfat", "etilena glikol",
    "propilen glikol", "butanon", "aseton oksim", "metil isobutil keton", "etil asetat",
    "tetrahydrofuran", "dimetil sulfoksida", "piridin", "formamida", "karbamat",
    "urea", "gliserol", "aspartam", "sukrosa", "glukosa"
]

# Bangun data_kimia
data_kimia = {}
for nama in nama_kimia_asli:
    data_kimia[nama] = {
        "piktogram": random.sample(piktogram_list, k=random.randint(1, 2)),
        "risiko": random.sample(risiko_list, k=random.randint(2, 4)),
        "penanganan": random.choice(penanganan_list),
        "apd": random.choice(apd_list)
    }

# Navigasi via sidebar
page = st.sidebar.radio("📓 Navigasi Aplikasi", ["🏠 Halaman Utama", "🔍 Simulasi Bahan Kimia"])

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

    st.markdown("### 🌟 Manfaat Aplikasi Ini")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("🔎 Pencarian Bebas\n\nCari bahan kimia dengan nama tanpa harus pilih.")
    with col2:
        st.info("🧪 Tampilan Edukatif\n\nTampilkan piktogram, risiko, penanganan, dan APD.")
    with col3:
        st.warning("👩‍💻 Edukasi K3\n\nCocok untuk siswa, mahasiswa, dan teknisi laboratorium.")

    st.markdown("---")

    st.markdown("""
    <div style='text-align:center'>
        <h3 style='color:#007ACC;'>Sudah siap untuk simulasi?</h3>
        <p>Klik menu <b>🔍 Simulasi Bahan Kimia</b> di sebelah kiri untuk memulai</p>
    </div>
    """, unsafe_allow_html=True)

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

    keyword = st.text_input("Masukkan nama bahan kimia (misal: asam klorida)").lower()

    if keyword:
        if keyword in data_kimia:
            info = data_kimia[keyword]

            st.subheader("💼 Piktogram Bahaya")
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
