from config import Config
import streamlit as st
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


# Header
with st.container():
    c1, c2 = st.columns(2)
    
    c1.markdown(f"<img src=\"{utils.replace_image('assets/logo.png', 'img')}\" alt=\"Logo\" width=\"200\">", unsafe_allow_html=True)
    
    c2.markdown("")
    c2.markdown("")
    c2.markdown("")
    select_bar = c2.selectbox("Select Faculty", fakultas)

# Main
with st.container():
    select_button = st.button("Select")
    homepage_button = st.button("Go to Homepage")

    if select_button:
        if select_bar == fakultas[0]:
            inputProdi = st.selectbox('Program Studi', prodi) #Ini harusnya multipage
        elif select_bar == fakultas[1]:
            inputProdi = st.selectbox('Program Studi', sorted(list(cfg['fakultas']['Fakultas Ilmu dan Teknologi Kebumian'])))
        elif select_bar == fakultas[2]:
            inputProdi = st.selectbox('Program Studi', sorted(list(cfg['fakultas']['Fakultas Matematika dan Ilmu Pengetahuan Alam'])))
        elif select_bar == fakultas[3]:
            inputProdi = st.selectbox('Program Studi', sorted(list(cfg['fakultas']['Fakultas Seni Rupa dan Desain'])))
        elif select_bar == fakultas[4]:
            inputProdi = st.selectbox('Program Studi', sorted(list(cfg['fakultas']['Fakultas Teknologi Industri'])))
        elif select_bar == fakultas[5]:
            inputProdi = st.selectbox('Program Studi', sorted(list(cfg['fakultas']['Fakultas Teknik Sipil dan Lingkungan'])))
        elif select_bar == fakultas[6]:
            inputProdi = st.selectbox('Program Studi', sorted(list(cfg['fakultas']['Fakultas Teknik Mesin dan Dirgantara'])))
        elif select_bar == fakultas[7]:
            inputProdi = st.selectbox('Program Studi', sorted(list(cfg['fakultas']['Fakultas Teknik Pertambangan dan Perminyakan'])))
        elif select_bar == fakultas[8]:
            inputProdi = st.selectbox('Program Studi', sorted(list(cfg['fakultas']['Sekolah Arsitektur, Perencanaan dan Pengembangan Kebijakan'])))
        elif select_bar == fakultas[9]:
            inputProdi = st.selectbox('Program Studi', sorted(list(cfg['fakultas']['Sekolah Bisnis dan Manajemen'])))
        elif select_bar == fakultas[10]:
            inputProdi = st.selectbox('Program Studi', sorted(list(cfg['fakultas']['Sekolah Farmasi'])))
        elif select_bar == fakultas[11]:
            inputProdi = st.selectbox('Program Studi', sorted(list(cfg['fakultas']['Sekolah Ilmu dan Teknologi Hayati'])))
        elif select_bar == fakultas[12]:
            inputProdi = st.selectbox('Program Studi', sorted(list(cfg['fakultas']['Sekolah Teknik Elektro dan Informatika'])))