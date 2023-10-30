import streamlit as st
from src.bab import Bab


class BabLima(Bab):
    def show_kesesuaian_kuliah_dengan_pekerjaan(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")

    def show_kesesuaian_kuliah_dengan_pekerjaan_per_prodi(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")

    def show_kategori_bidang_usaha(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")

    def show_kategori_bidang_usaha_per_prodi(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")

    def show_kategori_jenis_pekerjaan(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")

    def show_jabatan(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")

    def show_jabatan_per_prodi(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")

    def show_penghasilan_dan_bonus(self, graph_type):
        if graph_type == "bar":
            # All
            if self.input_fakultas == "All":
                st.warning("Not yet implemented.")

            # Fakultas
            elif self.input_fakultas != "All" and self.input_prodi == "All":
                st.warning("Not yet implemented.")

            # Program studi
            else:
                st.warning("Not yet implemented.")
        elif graph_type == "table":
            # All
            if self.input_fakultas == "All":
                st.warning("Not yet implemented.")

            # Fakultas
            elif self.input_fakultas != "All" and self.input_prodi == "All":
                st.warning("Not yet implemented.")

            # Program studi
            else:
                st.warning("Not yet implemented.")

    def show_penghasilan_per_prodi(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")

    def show_bonus_per_prodi(self):
        # All
        if self.input_fakultas == "All":
            st.warning("Not yet implemented.")

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.warning("Not yet implemented.")

        # Program studi
        else:
            st.warning("Not yet implemented.")
