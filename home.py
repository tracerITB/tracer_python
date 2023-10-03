from config import Config
import streamlit as st
import utils

# Import config from json
cfg = Config('config.json').get_config()
kategori = cfg['kategori']
fakultas = sorted(list(cfg['fakultas'].keys()))
prodi = sorted(list(set([j for i in cfg["fakultas"].values() for j in i])))

# Set wide layout
st.set_page_config(layout="wide")

# Import css
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Header
with st.container():
    c1, c2, c3 = st.columns((2, 2, 5))
    
    c1.markdown(f"""
        <button onclick="hi()">
        </button>
    """, unsafe_allow_html=True)
    
    c2.markdown(f"<img src=\"{utils.replace_image('assets/logo.png', 'img')}\" alt=\"Logo\" width=\"200\">", unsafe_allow_html=True)
    
    c3.markdown("")
    c3.markdown("")
    c3.markdown("")
    select_bar = c3.selectbox("Select Faculty", fakultas)
print(utils.replace_image('assets/menu.svg', 'svg'))

# Main
with st.container():
    select_button = st.button("Select")
    homepage_button = st.button("Go to Homepage")

    # if select_button:
    #     if select_bar == fakultas[0]:
    #         inputProdi = st.selectbox('Program Studi', prodiAll) #Ini harusnya multipage
    #     elif select_bar == fakultas[1]:
    #         inputProdi = st.selectbox('Program Studi', prodiFITB)
    #     elif select_bar == fakultas[2]:
    #         inputProdi = st.selectbox('Program Studi', prodiFMIPA)
    #     elif select_bar == fakultas[3]:
    #         inputProdi = st.selectbox('Program Studi', prodiFSRD)
    #     elif select_bar == fakultas[4]:
    #         inputProdi = st.selectbox('Program Studi', prodiFTI)
    #     elif select_bar == fakultas[5]:
    #         inputProdi = st.selectbox('Program Studi', prodiFTSL)
    #     elif select_bar == fakultas[6]:
    #         inputProdi = st.selectbox('Program Studi', prodiFTMD)
    #     elif select_bar == fakultas[7]:
    #         inputProdi = st.selectbox('Program Studi', prodiFTTM)
    #     elif select_bar == fakultas[8]:
    #         inputProdi = st.selectbox('Program Studi', prodiSAPPK)
    #     elif select_bar == fakultas[9]:
    #         inputProdi = st.selectbox('Program Studi', prodiSBM)
    #     elif select_bar == fakultas[10]:
    #         inputProdi = st.selectbox('Program Studi', prodiSF)
    #     elif select_bar == fakultas[11]:
    #         inputProdi = st.selectbox('Program Studi', prodiSITH)
    #     elif select_bar == fakultas[12]:
    #         inputProdi = st.selectbox('Program Studi', prodiSTEI)