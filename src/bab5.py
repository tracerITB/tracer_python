import streamlit as st
import plotly.express as px
from src.bab import Bab


class BabLima(Bab):
    def __init__(self, input_tahun, input_fakultas, input_prodi, dataframe):
        super().__init__(input_tahun, input_fakultas, input_prodi, dataframe)

    def showKesesuaianKuliahDenganPekerjaan(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")

    def showKesesuaianKuliahDenganPekerjaanPerProdi(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")

    def showKategoriBidangUsaha(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")

    def showKategoriBidangUsahaPerProdi(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")

    def showKategoriJenisPekerjaan(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")

    def showJabatan(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")

    def showJabatanPerProdi(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")

    def showPenghasilanDanBonus(self, type):
        if type == "bar":
            # All
            if self.input_fakultas == "All":
                st.warning("Not yet implemented.")

            # Fakultas
            elif self.input_fakultas != "All" and self.input_prodi == "All":
                st.warning("Not yet implemented.")

            # Program studi
            else:
                st.warning("Not yet implemented.")
        elif type == "table":
            # All
            if self.input_fakultas == "All":
                st.warning("Not yet implemented.")

            # Fakultas
            elif self.input_fakultas != "All" and self.input_prodi == "All":
                st.warning("Not yet implemented.")

            # Program studi
            else:
                st.warning("Not yet implemented.")

    def showPenghasilanPerProdi(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")

    def showBonusPerProdi(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")
