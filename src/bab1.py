import streamlit as st
import plotly.express as px
import pandas as pd

class BabSatu:
    def __init__(self, input_tahun, input_fakultas, input_prodi, dataframe):
        self.input_tahun = input_tahun
        self.input_fakultas = input_fakultas
        self.input_prodi = input_prodi
        self.dataframe = dataframe

    def showIPAlumniITB(self):
        # All
        if self.input_fakultas == "All":
            # IP Histogram
            st.write("")
            st.write("Distribusi Indeks Prestasi")
            df = self.dataframe["IP"]
            fig = px.histogram(df, x="IP")
            st.plotly_chart(fig, use_container_width=True)
            #IP Per Prodi
            st.write("")
            st.write("Indeks Prestasi per Program Studi")
            df2 = self.dataframe.groupby('Program Studi')['IP'].mean().reset_index().sort_values(by='IP',ascending=True)
            fig2 = px.bar(df2,  x='IP', y='Program Studi')
            st.plotly_chart(fig2, use_container_width=True)
        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.write("")
            st.write("Distribusi Indeks Prestasi")
            df = self.dataframe[
                self.dataframe["Fakultas/Sekolah"] == self.input_fakultas
            ]
            df = df["IP"]
            fig = px.histogram(df, x="IP")
            st.plotly_chart(fig, use_container_width=True)
            #IP Per Prodi
            st.write("")
            st.write("Indeks Prestasi per Program Studi")
            df2 = self.dataframe[self.dataframe['Fakultas/Sekolah'] == self.input_fakultas ].groupby('Program Studi')['IP'].mean().reset_index().sort_values(by='IP',ascending=True)
            fig2 = px.bar(df2,  x='IP', y='Program Studi')
            st.plotly_chart(fig2, use_container_width=True)
        # Program studi
        else:
            st.write("")
            st.write("Distribusi Indeks Prestasi")
            df = self.dataframe[self.dataframe["Program Studi"] == self.input_prodi]
            df = df["IP"]
            fig = px.histogram(df, x="IP")
            st.plotly_chart(fig, use_container_width=True)

    # def showTes():
    # 2. IPPerProdi
    #
    # ip = df2018['IP']
    # pilih if All
    # if input_fakultas == fakultas[0]:
    #     ip = df2018[df2018['Fakultas/Sekolah'] == input_fakultas].groupby('Program Studi')['IP'].mean().reset_index().sort_values(by='IP',ascending=True)
    # ifFakultas
    # elif input_fakultas != fakultas[0] and  input_prodi == 'All'
    # ifProdi
    # else
    #    ip = df2018[df2018[''] == input_prodi].groupby('Program Studi')['IP'].mean().reset_index().sort_values(by='IP',ascending=True)
    # figIP = px.histogram(ip, x="IP")
    # st.plotly_chart(figIP, use_container_width=True)
