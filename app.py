import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Dashboard SKTB 2026", page_icon="📊", layout="wide")

# 2. Sambungan Data
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1DOwnN0agNQnV5tMDqdsUgTk_lBu7h-dkLwsdHt_8MYW_r_2XF1cpvWKQuk9N_W4hGP2NTiZ8ADvC/pub?output=csv"

# 3. Sidebar (Sebelah Tepi)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3048/3048122.png", width=80)
    st.header("MENU UTAMA")
    
    try:
        df = pd.read_csv(sheet_url)
        program_list = df['Peristiwa / Program'].dropna().unique().tolist()
        pilihan = st.selectbox("PILIH PROGRAM / AKTIVITI:", ["-- SENARAI PENUH --"] + program_list)
        
    except:
        st.error("Gagal memuatkan senarai program.")
        
    st.divider()
    st.caption("© 2026 Unit Digital SKTB")

# 4. Paparan Utama (Bahagian Tengah)
st.title("📊 Dashboard Program / Aktiviti SKTB 2026")
st.write("Sistem Pengurusan Aktiviti Digital SK Telok Berembang")
st.divider()

if 'df' in locals():
    if pilihan == "-- SENARAI PENUH --":
        st.subheader("📅 Jadual Keseluruhan Aktiviti")
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        data = df[df['Peristiwa / Program'] == pilihan].iloc[0]
        
        st.info(f"## 📌 {pilihan}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("TARIKH", str(data['Tarikh']))
        with col2:
            st.metric("HARI", str(data['Hari']))
            
        st.divider()
        st.write("### 📂 Dokumen & Lampiran")
        
        # Susunan Butang Empat Segi Tepat (Tidak Memanjang)
        col_btn = st.columns([1, 1, 4]) # Pecah kolum supaya butang duduk rapat ke kiri
        
        with col_btn[0]:
            url_opr = str(data['Link_Gambar_OPR']).strip()
            if url_opr.startswith('http'):
                st.link_button("🖼️ Gambar / OPR", url_opr, use_container_width=False)
            else:
                st.button("🖼️ Tiada OPR", disabled=True, use_container_width=False)
            
        with col_btn[1]:
            url_buku = str(data['Buku Program']).strip()
            if url_buku.startswith('http'):
                st.link_button("📖 Buku Program", url_buku, use_container_width=False)
            else:
                st.button("📖 Tiada Buku", disabled=True, use_container_width=False)
