import streamlit as st
import pandas as pd
import io

# 1. Konfigurasi Muka Depan
st.set_page_config(page_title="Dashboard RBT 2026", page_icon="🌸", layout="wide")

# CSS untuk gaya Pastel & Kawaii
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Quicksand', sans-serif; }
    .stApp { background-color: #FFF5F7; } /* Pink pastel sangat cair */
    .title-text { color: #FF69B4; text-align: center; font-size: 40px; font-weight: bold; padding: 20px; }
    .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 5px 5px 15px rgba(0,0,0,0.05); border-left: 8px solid #FFB6C1; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_index=True)

# 2. Data CSV (Bubu dah masukkan siap-siap di sini)
csv_data = """Tarikh,Hari,Program,Link
08/01,Khamis,Taklimat Ibu Bapa Tahun 1 & Prasekolah 2026,#
12/01,Isnin,Pelancaran Amalan Sek. Penyayang 2026,#
12/01 - 06/02,Isnin-Jumaat,Program Transisi 2026,#
14/01,Rabu,Penyerahan Wang BAP 2026,#
15/01,Khamis,RBT / Hari Persekolahan,#
16/01,Jumaat,Program Isra' Mikraj,#
19/01,Isnin,Perjumpaan Permainan / Persatuan,#
20/01,Selasa,Perjumpaan UBB dan Rumah Sukan,#
23/01,Jumaat,Taklimat Guru Besar,#
30/01,Jumaat,Merentas Desa 2026,#"""

# Tukar teks CSV jadi DataFrame (Jadual)
df = pd.read_csv(io.StringIO(csv_data))

# 3. Header Dashboard
st.markdown('<div class="title-text">🌸 Dashboard Aktiviti RBT 2026 🌸</div>', unsafe_allow_index=True)
st.write(f"<p style='text-align: center;'>Selamat Datang Cikgu! Dashboard ini mengandungi <b>{len(df)}</b> program utama.</p>", unsafe_allow_index=True)

# 4. Sidebar dengan Ikon Comel
with st.sidebar:
    st.title("Menu Cikgu")
    st.image("https://cdn-icons-png.flaticon.com/512/4392/4392457.png", width=150)
    search = st.text_input("🔍 Cari Program:", "")
    st.divider()
    if st.button("🐾 Panggil Ciko"):
        st.snow() # Kesan salji/bunga luruh yang comel

# Filter carian jika ada
if search:
    df = df[df['Program'].str.contains(search, case=False)]

# 5. Paparan Utama (Grid Card)
col1, col2 = st.columns(2)

for i, row in df.iterrows():
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"""
            <div class="card">
                <h4 style="color: #DB7093; margin-bottom: 5px;">📅 {row['Tarikh']} ({row['Hari']})</h4>
                <p style="font-size: 18px; font-weight: bold; color: #333;">{row['Program']}</p>
            </div>
        """, unsafe_allow_index=True)
        
        # Butang Link (Hanya aktif kalau ada link selain '#')
        if row['Link'] != "#":
            st.link_button(f"📂 Buka Fail {row['Tarikh']}", row['Link'], use_container_width=True)
        else:
            st.button(f"⏳ Belum Selesai ({row['Tarikh']})", key=f"btn_{i}", disabled=True, use_container_width=True)

st.divider()
st.caption("© 2026 Dashboard Digital Guru RBT - SK Telok Berembang")
