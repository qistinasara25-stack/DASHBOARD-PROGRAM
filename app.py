import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Dashboard SKTB 2026", page_icon="🏫", layout="wide")

# 2. Sambungan Google Sheets
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1DOwnN0agNQnV5tMDqdsUgTk_lBu7h-dkLwsdHt_8MYW_r_2XF1cpvWKQuk9N_W4hGP2NTiZ8ADvC/pub?output=csv"

# 3. Paparan Header (Guna saiz besar & emoji)
st.title("📊 Dashboard Program / Aktiviti SKTB 2026")
st.write("### SK Telok Berembang | Digital Management")
st.divider()

try:
    # Tarik data terkini
    df = pd.read_csv(sheet_url)
    
    # Sidebar untuk carian
    with st.sidebar:
        st.header("🔍 MENU CARIAN")
        program_list = df['Peristiwa / Program'].dropna().unique().tolist()
        pilihan = st.selectbox("PILIH PROGRAM:", ["SENARAI PENUH"] + program_list)
        st.divider()
        st.info("💡 Tip: Kemaskini link di Google Sheets, dashboard akan berubah automatik!")

    if pilihan == "SENARAI PENUH":
        st.subheader("📅 Jadual Keseluruhan Aktiviti")
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        # Tunjukkan maklumat program dengan gaya 'Metric' (Tulisan Besar)
        data = df[df['Peristiwa / Program'] == pilihan].iloc[0]
        
        st.info(f"## 📌 {pilihan}")
        
        # Guna Metric supaya tulisan nampak besar dan profesional
        m1, m2 = st.columns(2)
        m1.metric("📅 TARIKH", str(data['Tarikh']))
        m2.metric("🗓️ HARI", str(data['Hari']))
        
        st.divider()
        st.markdown("### 📂 DOKUMEN & LAMPIRAN")
        
        col_btn1, col_btn2 = st.columns(2)
        
        # Butang 1: Link Gambar / OPR
        with col_btn1:
            url_opr = str(data['Link_Gambar_OPR']).strip()
            if url_opr.startswith('http'):
                st.link_button("🖼️ BUKA GAMBAR / OPR", url_opr, use_container_width=True, type="primary")
            else:
                st.button("🖼️ GAMBAR/OPR TIADA", disabled=True, use_container_width=True)
        
        # Butang 2: Link Buku Program
        with col_btn2:
            url_buku = str(data['Buku Program']).strip()
            if url_buku.startswith('http'):
                st.link_button("📖 BUKA BUKU PROGRAM", url_buku, use_container_width=True, type="secondary")
            else:
                st.button("📖 BUKU PROGRAM TIADA", disabled=True, use_container_width=True)

except Exception as e:
    st.error("Gagal menarik data. Pastikan nama lajur di Google Sheets tepat.")

st.divider()
st.caption("© 2026 Dashboard SKTB - Digital Management Unit")
