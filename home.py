from config import Config
import streamlit as st
import streamlit.components.v1 as components
import utils

# Import config from json
cfg = Config('config.json').get_config()

# st.set_page_config(
#     layout="wide",
# )


kategori = cfg['kategori']
utils.replace_image()

with st.container():
    with open('cache/navbar.html') as f:
        st.markdown(f.read(), unsafe_allow_html=True)

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# List Fakultas
fakultas = ["All", "Fakultas Ilmu dan Teknologi Kebumian",
            "Fakultas Matematika dan Ilmu Pengetahuan Alam",
            "Fakultas Seni Rupa dan Desain",
            "Fakultas Teknologi Industri",
            "Fakultas Teknik Sipil dan Lingkungan",
            "Fakultas Teknik Mesin dan Dirgantara",
            "Fakultas Teknik Pertambangan dan Perminyakan",
            "Sekolah Arsitektur, Perencanaan dan Pengembangan Kebijakan",
            "Sekolah Bisnis dan Manajemen",
            "Sekolah Farmasi",
            "Sekolah Ilmu dan Teknologi Hayati",
            "Sekolah Teknik Elektro dan Informatika"]

#List Prodi
prodiAll = ["All", "Teknik Geologi", "Teknik Geodesi dan Geomatika",
             "Meteorologi", "Oseanografi","Matematika", "Fisika", "Astronomi", "Kimia","Seni Rupa", "Desain Interior",
             "Desain Komunikasi Visual", "Desain Produk","Teknik Kimia", "Teknik Industri",
            "Teknik Fisika", "Manajemen Rekayasa Industri","Teknik Sipil", "Teknik Lingkungan", "Teknik Kelautan","Teknik Mesin", "Teknik Dirgantara", "Teknik Material","Teknik Pertambangan", "Teknik Perminyakan",
             "Teknik Geofisika", "Teknik Metalurgi","Arsitektur", "Perencanaan Wilayah dan Kota","Manajemen", "Kewirausahaan","Sains dan Teknologi Farmasi, Farmasi Klinik dan Komunitas","Biologi", "Mikrobiologi", "Rekayasa Hayati",
             "Rekayasa Pertanian", "Rekayasa Kehutanan", "Teknologi Pasca Panen","Teknik Elektro", "Teknik Tenaga Listrik", "Teknik Telekomunikasi",
             "Teknik Biomedis", "Teknik Informatika", "Sistem dan Teknologi Informasi"]
prodiFITB = ["All", "Teknik Geologi", "Teknik Geodesi dan Geomatika",
             "Meteorologi", "Oseanografi"]
prodiFMIPA = ["All","Matematika", "Fisika", "Astronomi", "Kimia"]
prodiFSRD = ["All","Seni Rupa", "Desain Interior",
             "Desain Komunikasi Visual", "Desain Produk"]
prodiFTI = ["All","Teknik Kimia", "Teknik Industri",
            "Teknik Fisika", "Manajemen Rekayasa Industri"]
prodiFTSL = ["All","Teknik Sipil", "Teknik Lingkungan", "Teknik Kelautan"]
prodiFTMD = ["All","Teknik Mesin", "Teknik Dirgantara", "Teknik Material"]
prodiFTTM = ["All","Teknik Pertambangan", "Teknik Perminyakan",
             "Teknik Geofisika", "Teknik Metalurgi"]
prodiSAPPK = ["All","Arsitektur", "Perencanaan Wilayah dan Kota"]
prodiSBM = ["All","Manajemen", "Kewirausahaan"]
prodiSF = ["All","Sains dan Teknologi Farmasi, Farmasi Klinik dan Komunitas"]
prodiSITH = ["All","Biologi", "Mikrobiologi", "Rekayasa Hayati",
             "Rekayasa Pertanian", "Rekayasa Kehutanan", "Teknologi Pasca Panen"]
prodiSTEI = ["All","Teknik Elektro", "Teknik Tenaga Listrik", "Teknik Telekomunikasi",
             "Teknik Biomedis", "Teknik Informatika", "Sistem dan Teknologi Informasi"]

# Ini selection box
select_bar = st.selectbox("Select Faculty", fakultas)

select_button = st.button("Select")
homepage_button = st.button("Go to Homepage")

if select_button:
    if select_bar == fakultas[0]:
        inputProdi = st.selectbox('Program Studi', prodiAll) #Ini harusnya multipage
    elif select_bar == fakultas[1]:
        inputProdi = st.selectbox('Program Studi', prodiFITB)
    elif select_bar == fakultas[2]:
        inputProdi = st.selectbox('Program Studi', prodiFMIPA)
    elif select_bar == fakultas[3]:
        inputProdi = st.selectbox('Program Studi', prodiFSRD)
    elif select_bar == fakultas[4]:
        inputProdi = st.selectbox('Program Studi', prodiFTI)
    elif select_bar == fakultas[5]:
        inputProdi = st.selectbox('Program Studi', prodiFTSL)
    elif select_bar == fakultas[6]:
        inputProdi = st.selectbox('Program Studi', prodiFTMD)
    elif select_bar == fakultas[7]:
        inputProdi = st.selectbox('Program Studi', prodiFTTM)
    elif select_bar == fakultas[8]:
        inputProdi = st.selectbox('Program Studi', prodiSAPPK)
    elif select_bar == fakultas[9]:
        inputProdi = st.selectbox('Program Studi', prodiSBM)
    elif select_bar == fakultas[10]:
        inputProdi = st.selectbox('Program Studi', prodiSF)
    elif select_bar == fakultas[11]:
        inputProdi = st.selectbox('Program Studi', prodiSITH)
    elif select_bar == fakultas[12]:
        inputProdi = st.selectbox('Program Studi', prodiSTEI)

if homepage_button:
    st.write("Homepage")