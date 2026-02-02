import streamlit as st
import pandas as pd
import io

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Dashboard RBT 2026", page_icon="🌸", layout="wide")

# 2. Gaya Pastel (CSS Ringkas)
st.markdown("""
    <style>
    .stApp { background-color: #FFF5F7; }
    .card { 
        background: white; 
        padding: 20px; 
        border-radius: 15px; 
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05); 
        border-left: 8px solid #FFB6C1; 
        margin-bottom: 20px; 
    }
    </style>
    """, unsafe_allow_index=True)

# 3. Data Program
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

df = pd.read_csv(io.StringIO(csv_data))

# 4. Paparan Header
st.title("🌸 Dashboard Aktiviti RBT 2026 🌸")
st.write("SK Telok Berembang | Digital Management")

# 5. Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4392/4392457.png", width=100)
    if st.button("🐱 Panggil Ciko"):
        st.balloons()

# 6. Susunan Card
col1, col2 = st.columns(2)

for i, row in df.iterrows():
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"""
            <div class="card">
                <h4 style="color: #DB7093;">📅 {row['Tarikh']} ({row['Hari']})</h4>
                <p style="font-weight: bold;">{row['Program']}</p>
            </div>
        """, unsafe_allow_index=True)
        
        if row['Link'] != "#":
            st.link_button(f"📂 Buka Fail", row['Link'], use_container_width=True)
        else:
            st.button(f"⏳ Belum Selesai", key=f"btn_{i}", disabled=True, use_container_width=True)
