import streamlit as st
import pandas as pd
import io

# Konfigurasi ringkas tanpa CSS berat
st.set_page_config(page_title="Dashboard RBT 2026", page_icon="🌸")

st.title("🌸 Dashboard Aktiviti RBT 2026")
st.write("SK Telok Berembang")

# Data CSV yang sudah disiap isi
csv_data = """Tarikh,Hari,Program
08/01,Khamis,Taklimat Ibu Bapa Tahun 1 & Prasekolah 2026
12/01,Isnin,Pelancaran Amalan Sek. Penyayang 2026
12/01 - 06/02,Isnin-Jumaat,Program Transisi 2026
14/01,Rabu,Penyerahan Wang BAP 2026
15/01,Khamis,RBT / Hari Persekolahan
16/01,Jumaat,Program Isra' Mikraj
19/01,Isnin,Perjumpaan Permainan / Persatuan
20/01,Selasa,Perjumpaan UBB dan Rumah Sukan
23/01,Jumaat,Taklimat Guru Besar
30/01,Jumaat,Merentas Desa 2026"""

df = pd.read_csv(io.StringIO(csv_data))

# Paparan jadual kemas
st.dataframe(df, use_container_width=True)

if st.button("🐱 Panggil Ciko"):
    st.balloons()
