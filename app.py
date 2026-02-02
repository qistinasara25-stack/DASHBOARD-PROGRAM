import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman (Macam rupa portal)
st.set_page_config(page_title="Dashboard SKTB 2026", page_icon="📊", layout="centered")

# 2. Sambungan Data
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1DOwnN0agNQnV5tMDqdsUgTk_lBu7h-dkLwsdHt_8MYW_r_2XF1cpvWKQuk9N_W4hGP2NTiZ8ADvC/pub?output=csv"

# 3. Header Dashboard (Minimalis & Cantik)
st.image("https://cdn-icons-png.flaticon.com/512/3048/3048122.png", width=80)
st.title("Dashboard Program / Aktiviti SKTB 2026")
st.caption("Sistem Pengurusan Aktiviti Digital SKTB")
st.divider()

try:
    df = pd.read_csv(sheet_url)
    
    # 4. Kotak Pilihan (Dropdown macam dalam portal)
    program_list = df['Peristiwa / Program'].dropna().unique().tolist()
    pilihan = st.selectbox("📌 Pilih Nama Program / Aktiviti:", ["-- Sila Pilih Program --"] + program_list)

    if pilihan == "-- Sila Pilih Program --":
        st.info("Sila pilih program daripada senarai di atas untuk melihat maklumat terperinci.")
        # Tunjuk jadual penuh di bawah sebagai rujukan
        with st.expander("Lihat Jadual Keseluruhan"):
            st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        # Data untuk program yang dipilih
        data = df[df['Peristiwa / Program'] == pilihan].iloc[0]
        
        # Paparan Maklumat (Gaya Card yang kemas)
        st.subheader(f"📍 {pilihan}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Tarikh", str(data['Tarikh']))
        with col2:
            st.metric("Hari", str(data['Hari']))
            
        st.write("---")
        st.write("### 📂 Dokumen & Lampiran")
        
        # Butang Link (Gaya Wide & Clean)
        # Link Gambar/OPR
        url_opr = str(data['Link_Gambar_OPR']).strip()
        if url_opr.startswith('http'):
            st.link_button("📂 Buka Gambar / OPR", url_opr, use_container_width=True)
        else:
            st.button("📂 Gambar / OPR Tiada", disabled=True, use_container_width=True)
            
        # Link Buku Program
        url_buku = str(data['Buku Program']).strip()
        if url_buku.startswith('http'):
            st.link_button("📖 Buka Buku Program", url_buku, use_container_width=True)
        else:
            st.button("📖 Buku Program Tiada", disabled=True, use_container_width=True)

except Exception as e:
    st.error("Gagal menarik data. Pastikan lajur Google Sheets tepat (Tarikh, Hari, Peristiwa / Program, Link_Gambar_OPR, Buku Program).")

st.divider()
st.caption("© 2026 Unit Digital SK Telok Berembang")
