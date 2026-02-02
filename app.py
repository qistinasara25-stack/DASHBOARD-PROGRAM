import streamlit as st
import pandas as pd
import io

# 1. Konfigurasi Halaman (Profesional)
st.set_page_config(page_title="Dashboard SKTB 2026", page_icon="🏫", layout="wide")

# 2. Data Program SKTB
csv_data = """Tarikh,Hari,Program,Link
08/01,Khamis,Taklimat Ibu Bapa Tahun 1 & Prasekolah 2026,#
12/01,Isnin,Pelancaran Amalan Sek. Penyayang 2026,#
12/01 - 06/02,Isnin-Jumaat,Program Transisi 2026,#
14/01,Rabu,Penyerahan Wang BAP 2026,#
15/01,Khamis,RBT / Hari Persekolahan,#
16/01,Jumaat,Program Isra' Mikraj,#
19/01,Isnin,Perjumpaan Permainan / Persatuan,#
20/01,Selasa,Perjumpaan UBB dan Rumah Sukan,#
23/01,Jumaat,Taklimat Guru Besar,#
30/01,Jumaat,Merentas Desa 2026,#"""

df = pd.read_csv(io.StringIO(csv_data))

# 3. Sidebar Interaktif
with st.sidebar:
    st.header("🔍 Menu Carian")
    pilihan_program = st.selectbox("Pilih Program Untuk Detail:", ["Semua Program"] + list(df['Program']))
    st.divider()
    st.info("Pilih program untuk melihat tarikh dan maklumat berkaitan.")

# 4. Paparan Utama
st.title("📊 Dashboard Program / Aktiviti SKTB 2026")
st.write("Sistem Pengurusan Aktiviti Digital Sekolah")
st.divider()

if pilihan_program == "Semua Program":
    # Paparan Senarai Penuh
    st.subheader("📅 Jadual Keseluruhan Aktiviti")
    st.dataframe(df[['Tarikh', 'Hari', 'Program']], use_container_width=True, hide_index=True)
else:
    # Paparan Detail Program yang dipilih
    data_program = df[df['Program'] == pilihan_program].iloc[0]
    
    st.subheader(f"📌 Detail: {data_program['Program']}")
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**📅 Tarikh:** {data_program['Tarikh']}")
    with col2:
        st.info(f"**🗓️ Hari:** {data_program['Hari']}")
    
    if data_program['Link'] != "#":
        st.link_button(f"📂 Buka Dokumen {pilihan_program}", data_program['Link'], use_container_width=True)
    else:
        st.warning("⚠️ Pautan dokumen atau gambar belum dikemaskini.")

st.divider()
st.caption("© 2026 Dashboard SKTB - Diuruskan oleh Unit Digital Sekolah")
