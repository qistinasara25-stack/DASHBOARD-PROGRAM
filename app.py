import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman Ringkas
st.set_page_config(page_title="Dashboard SKTB 2026", page_icon="🏫", layout="wide")

# 2. Sambungan Google Sheets (Link CSV awak)
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1DOwnN0agNQnV5tMDqdsUgTk_lBu7h-dkLwsdHt_8MYW_r_2XF1cpvWKQuk9N_W4hGP2NTiZ8ADvC/pub?output=csv"

# 3. Header Dashboard (Tanpa CSS pelik untuk elak ralat)
st.title("📊 Dashboard Program / Aktiviti SKTB 2026")
st.write("Sistem Pengurusan Aktiviti Digital SKTB")
st.divider()

try:
    # Tarik data terkini
    df = pd.read_csv(sheet_url)
    
    # Sidebar untuk carian
    with st.sidebar:
        st.header("🔍 Menu Carian")
        program_list = df['Peristiwa / Program'].dropna().unique().tolist()
        pilihan = st.selectbox("Pilih Program:", ["Semua Program"] + program_list)

    if pilihan == "Semua Program":
        st.subheader("📅 Jadual Keseluruhan Aktiviti")
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        # Tunjukkan detail program yang dipilih
        data = df[df['Peristiwa / Program'] == pilihan].iloc[0]
        
        st.info(f"### 📌 {pilihan}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**📅 Tarikh:** {data['Tarikh']}")
        with col2:
            st.write(f"**🗓️ Hari:** {data['Hari']}")
        
        st.divider()
        st.write("#### 📂 Dokumen & Lampiran")
        
        btn1, btn2 = st.columns(2)
        
        # Lajur Link_Gambar_OPR
        with btn1:
            link_opr = str(data['Link_Gambar_OPR']).strip()
            if link_opr.startswith('http'):
                st.link_button("🖼️ Buka Gambar / OPR", link_opr, use_container_width=True)
            else:
                st.button("🖼️ Gambar/OPR Tiada", disabled=True, use_container_width=True)
        
        # Lajur Buku Program
        with btn2:
            link_buku = str(data['Buku Program']).strip()
            if link_buku.startswith('http'):
                st.link_button("📖 Buka Buku Program", link_buku, use_container_width=True)
            else:
                st.button("📖 Buku Program Tiada", disabled=True, use_container_width=True)

except Exception as e:
    st.error("Alamak! Ada masalah tarik data. Pastikan tajuk lajur kat Google Sheets awak betul.")
