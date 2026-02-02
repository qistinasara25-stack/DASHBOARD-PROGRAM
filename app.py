import streamlit as st
import pandas as pd
import io

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Dashboard SKTB 2026", page_icon="🏫", layout="wide")

# 2. Gaya Visual (CSS) - Tema Profesional & Moden
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    .main { background-color: #f8f9fa; }
    
    /* Header Style */
    .header-box {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        text-align: center;
        border-bottom: 5px solid #007bff;
        margin-bottom: 30px;
    }
    
    /* Card Style */
    .info-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border-left: 10px solid #007bff;
    }
    </style>
    """, unsafe_allow_index=True)

# 3. Data Program (CSV Internal)
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

# 4. Sidebar Interaktif
with st.sidebar:
    st.header("🔍 Menu Carian")
    # Dropdown untuk pilih program secara interaktif
    pilihan_program = st.selectbox("Pilih Program Untuk Detail:", ["Semua Program"] + list(df['Program']))
    st.divider()
    st.info("Pilih program untuk melihat tarikh dan dokumen berkaitan.")

# 5. Paparan Utama
st.markdown('<div class="header-box"><h1 style="color: #1a1a1a; margin-bottom:0;">📊 Dashboard Program / Aktiviti SKTB 2026</h1><p style="color: #666;">Sistem Pengurusan Aktiviti Digital Sekolah</p></div>', unsafe_allow_index=True)

if pilihan_program == "Semua Program":
    # Paparan Keseluruhan dalam bentuk jadual yang cantik
    st.subheader("📅 Senarai Penuh Aktiviti")
    st.dataframe(df[['Tarikh', 'Hari', 'Program']], use_container_width=True, hide_index=True)
else:
    # Paparan Interaktif bila satu program dipilih
    data_program = df[df['Program'] == pilihan_program].iloc[0]
    
    st.markdown(f"""
        <div class="info-card">
            <h2 style="color: #007bff; margin-top:0;">{data_program['Program']}</h2>
            <hr>
            <p style="font-size: 18px;"><b>📅 Tarikh:</b> {data_program['Tarikh']}</p>
            <p style="font-size: 18px;"><b>🗓️ Hari:</b> {data_program['Hari']}</p>
        </div>
    """, unsafe_allow_index=True)
    
    st.write("") # Jarak
    if data_program['Link'] != "#":
        st.link_button(f"📂 Buka Dokumen / Gambar {pilihan_program}", data_program['Link'], use_container_width=True)
    else:
        st.warning("⚠️ Pautan dokumen atau gambar belum dikemaskini untuk program ini.")

# 6. Footer
st.divider()
st.caption("© 2026 Dashboard SKTB - Diuruskan oleh Unit Digital Sekolah")
