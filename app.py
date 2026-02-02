import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Dashboard SKTB 2026", page_icon="🏫", layout="wide")

# 2. Sambungan Google Sheets (Link CSV anda)
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1DOwnN0agNQnV5tMDqdsUgTk_lBu7h-dkLwsdHt_8MYW_r_2XF1cpvWKQuk9N_W4hGP2NTiZ8ADvC/pub?output=csv"

# 3. Paparan Tajuk
st.title("📊 Dashboard Program / Aktiviti SKTB 2026")
st.write("Sistem Pengurusan Aktiviti Digital SKTB")
st.divider()

try:
    # Tarik data terkini dari Google Sheets
    df = pd.read_csv(sheet_url)
    
    # Sidebar untuk carian
    with st.sidebar:
        st.header("🔍 Menu Carian")
        # Menggunakan nama lajur 'Peristiwa / Program' seperti dalam Sheets anda
        program_list = df['Peristiwa / Program'].tolist()
        pilihan = st.selectbox("Pilih Program:", ["Semua Program"] + program_list)
        st.divider()
        st.info("Kemaskini data di Google Sheets untuk perubahan automatik.")

    if pilihan == "Semua Program":
        st.subheader("📅 Jadual Keseluruhan")
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        # Tunjukkan detail program yang dipilih
        data = df[df['Peristiwa / Program'] == pilihan].iloc[0]
        
        st.markdown(f"### 📌 {pilihan}")
        c1, c2 = st.columns(2)
        with c1:
            st.info(f"**📅 Tarikh:** {data['Tarikh']}")
        with c2:
            st.info(f"**🗓️ Hari:** {data['Hari']}")
        
        # Check jika ada link gambar/OPR
        link_col = 'Link_Gambar_OPR'
        if link_col in data and pd.notna(data[link_col]) and str(data[link_col]).startswith('http'):
            st.link_button(f"📂 Buka Gambar / OPR", str(data[link_col]), use_container_width=True)
        else:
            st.warning("⚠️ Pautan dokumen belum dimasukkan dalam Google Sheets.")

except Exception as e:
    st.error("Gagal menarik data. Pastikan Google Sheets anda masih dalam status 'Publish to web'.")
