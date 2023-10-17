"""This script defines a Streamlit web application for analyzing and visualizing course statistics
for students at Institut Teknologi Bandung."""
import streamlit as st
from config import Config
from src.bab1 import BabSatu
from src.bab4 import BabEmpat
import utils

# Import config from json
cfg = Config("config.json").get_config()
kategori = cfg["kategori"]
fakultas = ["All"] + sorted(list(cfg["fakultas"].keys()))
prodi = sorted(list({j for i in cfg["fakultas"].values() for j in i}))

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
    input_fakultas = c2.selectbox(
        "Pilih Fakultas : ",
        (fakultas),
    )
    # pilih prodi
    if input_fakultas == fakultas[0]:
        input_prodi = c3.selectbox("Program Studi :", prodi)  # Ini harusnya multipage
    else:
        input_prodi = c3.selectbox(
            "Program Studi :", sorted(list(cfg["fakultas"][input_fakultas]))
        )

# Main
# Daftar tahun
tahun_range = list(range(2018, 2023))
with st.container():
    st.header(input_fakultas)

    # Membuat slider tahun
    input_tahun = st.slider(" ", min_value=min(tahun_range), max_value=max(tahun_range))

    with st.spinner("Loading data..."):
        dataframes = utils.load_data()
        dataframes = {
            2018: dataframes[0],
            2019: dataframes[1],
            2020: dataframes[2],
            2021: dataframes[3],
            2022: dataframes[4],
        }

    with st.expander("Bab 1"):
        bab1 = BabSatu(
            input_tahun, input_fakultas, input_prodi, dataframes.get(input_tahun)
        )
        bab1.showIPAlumniITB()

    with st.expander("Bab 2"):
        st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
        st.warning("Not yet implemented.")

    with st.expander("Bab 3"):
        st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
        st.warning("Not yet implemented.")

    with st.expander("Bab 4"):
        bab4 = BabEmpat(
            input_tahun, input_fakultas, input_prodi, dataframes.get(input_tahun)
        )
        bab4.showKategoriPerusahaanPerProdi()

    with st.expander("Bab 5"):
        st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
        st.warning("Not yet implemented.")
