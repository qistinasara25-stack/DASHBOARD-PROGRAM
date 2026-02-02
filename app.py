import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Dashboard SKTB 2026", page_icon="🏫", layout="wide")

# 2. Sambungan Google Sheets (Link CSV anda)
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1DOwnN0agNQnV5tMDqdsUgTk_lBu7h-dkLwsdHt_8MYW_r_2XF1cpvWKQuk9N_W4hGP2NTiZ8ADvC/pub?output=csv"

# 3. Paparan Header (Tanpa CSS tambahan untuk elak ralat)
st.title("📊 Dashboard Program / Aktiviti SKTB 2026")
st.write("Sistem Pengurusan Aktiviti Digital SKTB")
st.divider()

try:
    # Tarik data terkini
    df = pd.read_csv(sheet_url)
    
    # Sidebar untuk carian
    with st.sidebar:
        st.header("🔍 MENU CARIAN")
        # Pastikan nama lajur tepat seperti dalam Sheets anda
        program_list = df['Peristiwa / Program'].dropna().unique().tolist()
        pilihan = st.selectbox("PILIH PROGRAM:", ["SENARAI PENUH"] + program_list)

    if pilihan == "SENARAI PENUH":
        st.markdown("## 📅 Jadual Keseluruhan Aktiviti")
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        # Tunjukkan detail program yang dipilih
        data = df[df['Peristiwa / Program'] == pilihan].iloc[0]
        
        # Gunakan kotak berwarna bawaan Streamlit (lebih selamat daripada CSS)
        st.info(f"## 📌 {pilihan}")
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric("📅 TARIKH", str(data['Tarikh']))
        with c2:
            st.metric("🗓️ HARI", str(data['Hari']))
        
        st.divider()
        st.markdown("### 📂 DOKUMEN & LAMPIRAN")
        
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
    st.error(f"Gagal menarik data. Sila pastikan tajuk lajur di Google Sheets ditaip dengan betul.")

# Footer
st.divider()
st.caption("© 2026 Dashboard SKTB - Versi Stabil v3.0")
