import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman (Moden & Bersih)
st.set_page_config(page_title="Dashboard SKTB 2026", page_icon="🏫", layout="wide")

# 2. Pautan CSV Google Sheets Awak
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1DOwnN0agNQnV5tMDqdsUgTk_lBu7h-dkLwsdHt_8MYW_r_2XF1cpvWKQuk9N_W4hGP2NTiZ8ADvC/pub?output=csv"

# 3. Paparan Tajuk
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📊 Dashboard Program / Aktiviti SKTB 2026</h1>", unsafe_allow_index=True)
st.markdown("<p style='text-align: center; color: #666;'>Sistem Pengurusan Aktiviti Digital Sekolah</p>", unsafe_allow_index=True)
st.divider()

try:
    # Tarik data secara automatik dari Google Sheets
    df = pd.read_csv(sheet_url)
    
    # Sidebar untuk carian interaktif
    with st.sidebar:
        st.header("🔍 Menu Carian")
        pilihan = st.selectbox("Pilih Program Untuk Detail:", ["Semua Program"] + list(df['Peristiwa / Program']))
        st.divider()
        st.info("Setiap kali anda kemaskini Google Sheets, maklumat di sini akan berubah secara automatik.")

    if pilihan == "Semua Program":
        st.subheader("📅 Jadual Keseluruhan Aktiviti")
        # Paparkan jadual penuh
        st.dataframe(df[['Tarikh', 'Hari', 'Peristiwa / Program']], use_container_width=True, hide_index=True)
    else:
        # Tunjukkan detail program yang dipilih sahaja
        data = df[df['Peristiwa / Program'] == pilihan].iloc[0]
        st.subheader(f"📌 Maklumat Program: {pilihan}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**📅 Tarikh:** {data['Tarikh']}")
        with col2:
            st.info(f"**🗓️ Hari:** {data['Hari']}")
        
        # Logik untuk butang Link Gambar/OPR
        link_col = 'Link_Gambar_OPR'
        if link_col in data and pd.notna(data[link_col]) and str(data[link_col]).startswith('http'):
            st.link_button(f"📂 Buka Gambar / OPR {pilihan}", str(data[link_col]), use_container_width=True)
        else:
            st.warning("⚠️ Pautan dokumen atau gambar belum dikemaskini dalam Google Sheets untuk program ini.")

except Exception as e:
    st.error("Gagal menarik data. Sila pastikan Google Sheets anda telah di-'Publish to Web' dalam format CSV.")
    st.info("Tips: Klik File > Share > Publish to web > Pilih Comma-separated values (.csv)")

st.divider()
st.caption("© 2026 Dashboard SKTB - Diuruskan oleh Unit Digital Sekolah")
