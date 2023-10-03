from config import Config
import streamlit as st
from streamlit_option_menu import option_menu
import utils

# Import config from json
cfg = Config('config.json').get_config()
kategori = cfg['kategori']
fakultas = ['All'] + sorted(list(cfg['fakultas'].keys()))
prodi = sorted(list(set([j for i in cfg["fakultas"].values() for j in i])))

# Set wide layout
st.set_page_config(layout="wide")

# Import css
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Sidebar
st.sidebar.markdown(f"<img src=\"{utils.replace_image('assets/logo.png', 'img')}\" alt=\"Logo\" width=\"100\">", unsafe_allow_html=True)
with st.sidebar.expander("About"):
    st.markdown("""
    This app is created to help students of Institut Teknologi Bandung to find their courses easily.
    """)

# Header
with st.container():
    c1, c2, c3 = st.columns(3)    
    c1.markdown(f"<img src=\"{utils.replace_image('assets/logo.png', 'img')}\" alt=\"Logo\" width=\"150\">", unsafe_allow_html=True)
    select_bar = c2.selectbox("Pilih Fakultas : ", fakultas)

# Daftar tahun
tahun_range = list(range(2018, 2023))

# Daftar label untuk tiap tahun
tahun_labels = {2018: 'Tahun 2018', 2019: 'Tahun 2019', 2020: 'Tahun 2020', 2021: 'Tahun 2021', 2022: 'Tahun 2022'}

# Membuat slider tahun
tahun_terpilih = st.slider('', min_value=min(tahun_range), max_value=max(tahun_range))


# Main
with st.container():
        if select_bar == fakultas[0]:
            inputProdi = c3.selectbox('Program Studi', prodi) #Ini harusnya multipage
        elif select_bar == fakultas[1]:
            inputProdi = c3.selectbox('Program Studi', sorted(list(cfg['fakultas'][fakultas[1]])))
        elif select_bar == fakultas[2]:
            inputProdi = c3.selectbox('Program Studi', sorted(list(cfg['fakultas']['Fakultas Matematika dan Ilmu Pengetahuan Alam'])))
        elif select_bar == fakultas[3]:
            inputProdi = c3.selectbox('Program Studi', sorted(list(cfg['fakultas']['Fakultas Seni Rupa dan Desain'])))
        elif select_bar == fakultas[4]:
            inputProdi = c3.selectbox('Program Studi', sorted(list(cfg['fakultas']['Fakultas Teknologi Industri'])))
        elif select_bar == fakultas[5]:
            inputProdi = c3.selectbox('Program Studi', sorted(list(cfg['fakultas']['Fakultas Teknik Sipil dan Lingkungan'])))
        elif select_bar == fakultas[6]:
            inputProdi = c3.selectbox('Program Studi', sorted(list(cfg['fakultas']['Fakultas Teknik Mesin dan Dirgantara'])))
        elif select_bar == fakultas[7]:
            inputProdi = c3.selectbox('Program Studi', sorted(list(cfg['fakultas']['Fakultas Teknik Pertambangan dan Perminyakan'])))
        elif select_bar == fakultas[8]:
            inputProdi = c3.selectbox('Program Studi', sorted(list(cfg['fakultas']['Sekolah Arsitektur, Perencanaan dan Pengembangan Kebijakan'])))
        elif select_bar == fakultas[9]:
            inputProdi = c3.selectbox('Program Studi', sorted(list(cfg['fakultas']['Sekolah Bisnis dan Manajemen'])))
        elif select_bar == fakultas[10]:
            inputProdi = c3.selectbox('Program Studi', sorted(list(cfg['fakultas']['Sekolah Farmasi'])))
        elif select_bar == fakultas[11]:
            inputProdi = c3.selectbox('Program Studi', sorted(list(cfg['fakultas']['Sekolah Ilmu dan Teknologi Hayati'])))
        elif select_bar == fakultas[12]:
            inputProdi = c3.selectbox('Program Studi', sorted(list(cfg['fakultas']['Sekolah Teknik Elektro dan Informatika'])))

selected = option_menu(
        menu_title=None,
        options=kategori,
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important"},
            "nav-link": {
                "font-size": "14px",
                "font-weight": "regular",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#BF9849",
            },  
            "nav-link-selected": {
                "background-color": "#BF9849",
            }
        },
)

st.write(selected,select_bar, inputProdi, tahun_terpilih)
