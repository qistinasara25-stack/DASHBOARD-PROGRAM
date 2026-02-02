import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Dashboard SKTB 2026", page_icon="🏫", layout="wide")

# 2. Kesan Interaktif & Zoom (CSS)
st.markdown("""
    <style>
    /* Kesan Zoom pada Butang Streamlit */
    div.stButton > button {
        transition: all 0.3s ease-in-out;
        border-radius: 10px;
    }
    
    div.stButton > button:hover {
        transform: scale(1.1); /* Zoom in 10% */
        background-color: #007bff; /* Tukar warna bila kursor hala */
        color: white;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
    }
    
    /* Kesan Zoom pada Pautan (Link Button) */
    div.stLinkButton > a {
        transition: all 0.3s ease-in-out;
        border-radius: 10px;
        text-decoration: none;
    }
    
    div.stLinkButton > a:hover {
        transform: scale(1.05); /* Zoom in 5% */
        box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_index=True)

# 3. Sambungan Google Sheets (Link CSV anda)
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1DOwnN0agNQnV5tMDqdsUgTk_lBu7h-dkLwsdHt_8MYW_r_2XF1cpvWKQuk9N_W4hGP2NTiZ8ADvC/pub?output=csv"

# 4. Paparan Tajuk
st.title("📊 Dashboard Program / Aktiviti SKTB 2026")
st.write("Sistem Pengurusan Aktiviti Digital SKTB")
st.divider()

try:
    # Tarik data terkini dari Google Sheets
    df = pd.read_csv(sheet_url)
    
    # Sidebar untuk carian
    with st.sidebar:
        st.header("🔍 Menu Carian")
        program_list = df['Peristiwa / Program'].tolist()
        pilihan = st.selectbox("Pilih Program:", ["Semua Program"] + program_list)
        st.divider()
        st.info("Setiap perubahan di Google Sheets akan dikemaskini di sini secara automatik.")

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
        
        st.write("#### 📂 Dokumen & Lampiran (Hala kursor untuk zoom)")
        btn_col1, btn_col2 = st.columns(2)
        
        # Butang 1: Link Gambar / OPR
        with btn_col1:
            if 'Link_Gambar_OPR' in data and pd.notna(data['Link_Gambar_OPR']) and str(data['Link_Gambar_OPR']).startswith('http'):
                st.link_button("🖼️ Buka Gambar / OPR", str(data['Link_Gambar_OPR']), use_container_width=True)
            else:
                st.button("🖼️ Gambar/OPR Tiada", disabled=True, use_container_width=True)
        
        # Butang 2: Link Buku Program
        with btn_col2:
            if 'Buku_Program' in data and pd.notna(data['Buku_Program']) and str(data['Buku_Program']).startswith('http'):
                st.link_button("📖 Buka Buku Program", str(data['Buku_Program']), use_container_width=True)
            else:
                st.button("📖 Buku Program Tiada", disabled=True, use_container_width=True)

except Exception as e:
    st.error("Gagal menarik data. Sila pastikan lajur di Google Sheets anda (Tarikh, Hari, Peristiwa / Program, Link_Gambar_OPR, Buku_Program) adalah tepat.")
