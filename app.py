import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Dashboard SKTB 2026", page_icon="🏫", layout="wide")

# 2. Kesan Hover Zoom (Kod CSS Paling Stabil)
st.markdown("""
    <style>
    /* Kesan pada butang link */
    .stLinkButton a {
        transition: all 0.3s ease-in-out !important;
    }
    .stLinkButton a:hover {
        transform: scale(1.1) !important;
        background-color: #FFB6C1 !important; /* Warna pink pastel bila hala kursor */
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2) !important;
    }
    /* Kesan pada butang biasa */
    .stButton button {
        transition: all 0.3s ease-in-out !important;
    }
    .stButton button:hover {
        transform: scale(1.1) !important;
    }
    </style>
    """, unsafe_allow_index=True)

# 3. Sambungan Google Sheets
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1DOwnN0agNQnV5tMDqdsUgTk_lBu7h-dkLwsdHt_8MYW_r_2XF1cpvWKQuk9N_W4hGP2NTiZ8ADvC/pub?output=csv"

# 4. Header Dashboard
st.markdown("# 📊 Dashboard Program / Aktiviti SKTB 2026")
st.markdown("### *Sistem Pengurusan Aktiviti Digital SKTB*")
st.divider()

try:
    df = pd.read_csv(sheet_url)
    
    with st.sidebar:
        st.header("🔍 MENU CARIAN")
        program_list = df['Peristiwa / Program'].dropna().unique().tolist()
        pilihan = st.selectbox("PILIH PROGRAM:", ["SENARAI PENUH"] + program_list)

    if pilihan == "SENARAI PENUH":
        st.markdown("## 📅 Jadual Keseluruhan Aktiviti")
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        data = df[df['Peristiwa / Program'] == pilihan].iloc[0]
        st.markdown(f"## 📌 {pilihan}")
        
        c1, c2 = st.columns(2)
        with c1:
            st.error(f"### 📅 TARIKH: {data['Tarikh']}")
        with c2:
            st.success(f"### 🗓️ HARI: {data['Hari']}")
        
        st.divider()
        st.markdown("## 📂 DOKUMEN & LAMPIRAN")
        st.write("Hala kursor (hover) pada butang untuk kesan zoom:")
        
        btn_col1, btn_col2 = st.columns(2)
        
        with btn_col1:
            url_opr = str(data['Link_Gambar_OPR']).strip()
            if url_opr.startswith('http'):
                st.link_button("🖼️ BUKA GAMBAR / OPR", url_opr, use_container_width=True)
            else:
                st.button("🖼️ GAMBAR/OPR TIADA", disabled=True, use_container_width=True)
        
        with btn_col2:
            url_buku = str(data['Buku Program']).strip()
            if url_buku.startswith('http'):
                st.link_button("📖 BUKA BUKU PROGRAM", url_buku, use_container_width=True)
            else:
                st.button("📖 BUKU PROGRAM TIADA", disabled=True, use_container_width=True)

except Exception as e:
    st.error("Gagal menarik data. Sila pastikan lajur di Google Sheets ditaip dengan betul.")
