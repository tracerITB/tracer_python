"""This script defines a Streamlit web application for analyzing and visualizing course statistics
for students at Institut Teknologi Bandung."""
import streamlit as st
import pandas as pd
import plotly.express as px
from config import Config
import utils

# Import config from json
cfg = Config("config.json").get_config()
kategori = cfg["kategori"]
fakultas = ["All"] + sorted(list(cfg["fakultas"].keys()))
prodi = sorted(list({[j for i in cfg["fakultas"].values() for j in i]}))

# Set wide layout
st.set_page_config(layout="wide")


# Import css
with open("style.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with st.container():
    st.sidebar.markdown(
        "<div style='padding-top: 0px; margin-top: -60px; margin-left: 40px;'><img"
        f" src=\"{utils.replace_image('assets/logo.png', 'logo')}\" alt=\"Logo\""
        ' width="200">',
        unsafe_allow_html=True,
    )
    with st.sidebar.expander("About"):
        st.markdown(
            "This app is created to help students of Institut Teknologi Bandung to find"
            " their courses easily."
        )
    with st.sidebar.expander("Help"):
        st.markdown("Silakan pilih Fakultas > Jurusan > Tahun > Bab yang diinginkan")

# Header
with st.container():
    c1, c2, c3 = st.columns(3)
    c1.markdown(
        "<div style='padding-left : 20px; padding-right: 20px; padding-bottom: 0px;"
        " padding-top: 5px; margin-left: 70px;'><img"
        f" src=\"{utils.replace_image('assets/logo.png', 'img')}\" alt=\"Logo\""
        ' width="100">',
        unsafe_allow_html=True,
    )
    # pilih fakultas
    select_bar = c2.selectbox(
        "Pilih Fakultas : ",
        (fakultas),
    )

# Main
with st.container():
    # pilih prodi
    if select_bar == fakultas[0]:
        inputProdi = c3.selectbox("Program Studi :", prodi)  # Ini harusnya multipage
    else:
        inputProdi = c3.selectbox(
            "Program Studi :", sorted(list(cfg["fakultas"][select_bar]))
        )

st.header(select_bar)

# Daftar tahun
tahun_range = list(range(2018, 2023))

# Daftar label untuk tiap tahun
tahun_labels = {
    2018: "Tahun 2018",
    2019: "Tahun 2019",
    2020: "Tahun 2020",
    2021: "Tahun 2021",
    2022: "Tahun 2022",
}

# Membuat slider tahun
tahun_terpilih = st.slider("", min_value=min(tahun_range), max_value=max(tahun_range))

if tahun_terpilih == 2018:
    with st.expander("Bab 1"):
        # Input
        df2018 = pd.read_excel(
            "Standarisasi_Kuesioner_2018-2022.xlsx", sheet_name="2018"
        )
        if select_bar == fakultas[0]:
            # IP Histogram
            st.write("Distribusi Indeks Prestasi")
            ip1 = df2018["IP"]
            fig1 = px.histogram(ip1, x="IP")
            st.plotly_chart(fig1, use_container_width=True)
        elif select_bar != fakultas[0] and inputProdi == "All":
            st.write("Distribusi Indeks Prestasi")
            df = df2018[df2018["Fakultas/Sekolah"] == select_bar]
            ip1 = df["IP"]
            fig1 = px.histogram(ip1, x="IP")
            st.plotly_chart(fig1, use_container_width=True)
        else:
            st.write("Distribusi Indeks Prestasi")
            df = df2018[df2018["Program Studi"] == inputProdi]
            ip1 = df["IP"]
            fig1 = px.histogram(ip1, x="IP")
            st.plotly_chart(fig1, use_container_width=True)

        # 2. IPPerProdi
        #
        # ip = df2018['IP']
        # pilih if All
        # if select_bar == fakultas[0]:
        #     ip = df2018[df2018['Fakultas/Sekolah'] == select_bar].groupby('Program Studi')['IP'].mean().reset_index().sort_values(by='IP',ascending=True)
        # ifFakultas
        # elif select_bar != fakultas[0] and  inputProdi == 'All'
        # ifProdi
        # else
        #    ip = df2018[df2018[''] == inputProdi].groupby('Program Studi')['IP'].mean().reset_index().sort_values(by='IP',ascending=True)
        # figIP = px.histogram(ip, x="IP")
        # st.plotly_chart(figIP, use_container_width=True)

    with st.expander("Bab 2"):
        st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

    with st.expander("Bab 3"):
        st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

    with st.expander("Bab 4"):
        st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

    with st.expander("Bab 5"):
        st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

else:
    with st.expander("Bab 1"):
        st.write("EMPTY")

    with st.expander("Bab 2"):
        st.write("EMPTY")

    with st.expander("Bab 3"):
        st.write("EMPTY")

    with st.expander("Bab 4"):
        st.write("EMPTY")

    with st.expander("Bab 5"):
        st.write("EMPTY")
