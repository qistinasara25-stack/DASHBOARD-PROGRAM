import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Dashboard SKTB 2026", page_icon="🏫", layout="wide")

# 2. Sambungan Google Sheets (Link CSV anda)
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1DOwnN0agNQnV5tMDqdsUgTk_lBu7h-dkLwsdHt_8MYW_r_2XF1cpvWKQuk9N_W4hGP2NTiZ8ADvC/pub?output=csv"

# 3. Paparan Header (Saiz Besar)
st.markdown("# 📊 Dashboard Program / Aktiviti SKTB 2026")
st.markdown("### *Sistem Pengurusan Aktiviti Digital SKTB*")
st.divider()

try:
    # Tarik data terkini
    df = pd.read_csv(sheet_url)
    
    # Sidebar untuk carian dengan saiz lebih besar
    with st.sidebar:
        st.header("🔍 MENU CARIAN")
        program_list = df['Peristiwa / Program'].dropna().unique().tolist()
        pilihan = st.selectbox("PILIH PROGRAM UNTUK DETAIL:", ["SENARAI PENUH"] + program_list)
        st.divider()
        st.write("Dikuasakan oleh Unit Digital SKTB")

    if pilihan == "SENARAI PENUH":
        st.markdown("## 📅 Jadual Keseluruhan Aktiviti")
        # Paparan jadual yang lebih besar
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        # Tunjukkan detail program yang dipilih (Layout Card)
        data = df[df['Peristiwa / Program'] == pilihan].iloc[0]
        
        # Nama Program (Header Paling Besar)
        st.markdown(f"## 📌 {pilihan}")
        
        # Maklumat Tarikh & Hari dalam Kotak Besar
        c1, c2 = st.columns(2)
        with c1:
            st.error(f"### 📅 TARIKH: {data['Tarikh']}")
        with c2:
            st.success(f"### 🗓️ HARI: {data['Hari']}")
        
        st.divider()
        
        # Bahagian Dokumen dengan Butang Besar
        st.markdown("## 📂 DOKUMEN & LAMPIRAN")
        st.write("Klik butang di bawah untuk membuka fail berkaitan:")
        
        btn_col1, btn_col2 = st.columns(2)
        
        # Butang Link Gambar / OPR
        with btn_col1:
            url_opr = str(data['Link_Gambar_OPR']).strip()
            if url_opr.startswith('http'):
                st.link_button("🖼️ BUKA GAMBAR / OPR", url_opr, use_container_width=True)
            else:
                st.button("🖼️ GAMBAR/OPR TIADA", disabled=True, use_container_width=True)
        
        # Butang Buku Program
        with btn_col2:
            url_buku = str(data['Buku Program']).strip()
            if url_buku.startswith('http'):
                st.link_button("📖 BUKA BUKU PROGRAM", url_buku, use_container_width=True)
            else:
                st.button("📖 BUKU PROGRAM TIADA", disabled=True, use_container_width=True)

except Exception as e:
    st.error("Gagal menarik data. Sila pastikan tajuk lajur di Google Sheets ditaip dengan betul.")

# Footer
st.divider()
st.caption("© 2026 Dashboard SKTB - Versi Interaktif v2.0")
