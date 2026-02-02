import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Dashboard SKTB 2026", page_icon="🏫", layout="wide")

# 2. Kesan Interaktif & Zoom (CSS)
st.markdown("""
    <style>
    div.stButton > button:hover, div.stLinkButton > a:hover {
        transform: scale(1.05);
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_index=True)

# 3. Sambungan Google Sheets (Link CSV anda)
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1DOwnN0agNQnV5tMDqdsUgTk_lBu7h-dkLwsdHt_8MYW_r_2XF1cpvWKQuk9N_W4hGP2NTiZ8ADvC/pub?output=csv"

# 4. Paparan Tajuk
st.title("Dashboard Program / Aktiviti SKTB 2026")
st.write("Sistem Pengurusan Aktiviti Digital SKTB")
st.divider()

try:
    # Tarik data dari Google Sheets
    df = pd.read_csv(sheet_url)
    
    # Sidebar untuk carian
    with st.sidebar:
        st.header("Carian Program")
        program_list = df['Peristiwa / Program'].dropna().unique().tolist()
        pilihan = st.selectbox("Pilih Program:", ["Semua Program"] + program_list)

    if pilihan == "Semua Program":
        st.subheader("Jadual Keseluruhan")
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        # Detail program yang dipilih
        data = df[df['Peristiwa / Program'] == pilihan].iloc[0]
        
        st.subheader(f"Program: {pilihan}")
        c1, c2 = st.columns(2)
        with c1:
            st.info(f"Tarikh: {data['Tarikh']}")
        with c2:
            st.info(f"Hari: {data['Hari']}")
        
        st.write("Dokumen & Lampiran")
        btn_col1, btn_col2 = st.columns(2)
        
        # Butang Link Gambar / OPR (Lajur D)
        with btn_col1:
            url_opr = str(data['Link_Gambar_OPR']).strip()
            if url_opr.startswith('http'):
                st.link_button("Buka Gambar / OPR", url_opr, use_container_width=True)
            else:
                st.button("Gambar/OPR Tiada", disabled=True, use_container_width=True)
        
        # Butang Buku Program (Lajur E)
        with btn_col2:
            url_buku = str(data['Buku Program']).strip()
            if url_buku.startswith('http'):
                st.link_button("Buka Buku Program", url_buku, use_container_width=True)
            else:
                st.button("Buku Program Tiada", disabled=True, use_container_width=True)

except Exception as e:
    st.error("Gagal menarik data. Pastikan nama lajur di Google Sheets adalah tepat.")
