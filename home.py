from config import Config
import streamlit as st
import streamlit.components.v1 as components
import utils

# Import config from json
cfg = Config('config.json').get_config()

st.set_page_config(
    layout="wide",
)

kategori = cfg['kategori']
utils.replace_image()

with st.container():
    with open('cache/navbar.html') as f:
        st.markdown(f.read(), unsafe_allow_html=True)

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# # Side bar
# st.sidebar.image("image/logo.jpeg", caption="ITB Tracer Study")