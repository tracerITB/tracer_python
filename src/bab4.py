import streamlit as st
import plotly.express as px
from src.bab import Bab


class BabEmpat(Bab):
    def __init__(self, *args):
        super().__init__(*args)
        self.kategori_perusahaan = ["multinasional", "nasional", "lokal"]
        self.bentuk_perusahaan = [
            "instansi pemerintah (termasuk BUMN)",
            "organisasi non-profit / lembaga swadaya masyarakat",
            "perusahaan swasta",
            "wiraswasta / perusahaan sendiri",
        ]

    def show(self):
        self.show_kategori_perusahaan_per_prodi()
        self.show_bentuk_perusahaan_tempat_bekerja()
        self.show_waktu_memulai_usaha()
        self.show_waktu_memulai_usaha_persebaran()

    def show_kategori_perusahaan_per_prodi(self):
        # All
        if self.input_fakultas == "All" and self.input_prodi == "All":
            df = self.dataframe[
                self.dataframe["Apa kategori perusahaan tempat Anda bekerja?"].isin(
                    self.kategori_perusahaan
                )
            ]
            df = df.pivot_table(
                index="Program Studi",
                columns="Apa kategori perusahaan tempat Anda bekerja?",
                aggfunc="size",
                fill_value=0,
            )
            df = df.div(df.sum(axis=1), axis=0) * 100
            fig = px.bar(
                df,
                x=self.kategori_perusahaan,
                labels={"value": "Persentase"},
                title="Kategori Perusahaan per Prodi"
            )

            # Adding labels
            annotations = []
            for i, bar_data in enumerate(fig.data):
                x_values = bar_data.x
                y_values = bar_data.y

                for j, (x, y) in enumerate(zip(x_values, y_values)):
                    x_center = x / 2
                    if i != 0:
                        _i = i
                        while _i > 0:
                            _i -= 1
                            x_center += fig.data[_i].x[j]
                    annotations.append(
                        {
                            "x": x_center,
                            "y": y,
                            "text": f"{x:.2f}%",
                            "font": {"color": "white"},
                            "showarrow": False,
                        }
                    )
            fig.update_layout(annotations=annotations)

            st.plotly_chart(fig, use_container_width=True)

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            df = self.dataframe[
                self.dataframe["Fakultas/Sekolah"] == self.input_fakultas
            ]
            df = df[
                df["Apa kategori perusahaan tempat Anda bekerja?"].isin(
                    self.kategori_perusahaan
                )
            ]
            df = df.pivot_table(
                index="Program Studi",
                columns="Apa kategori perusahaan tempat Anda bekerja?",
                aggfunc="size",
                fill_value=0,
            )
            df = df.div(df.sum(axis=1), axis=0) * 100
            fig = px.bar(
                df,
                x=self.kategori_perusahaan,
                labels={"value": "Persentase"},
                title="Kategori Perusahaan per Prodi"
            )

            # Adding labels
            annotations = []
            for i, bar_data in enumerate(fig.data):
                x_values = bar_data.x
                y_values = bar_data.y

                for j, (x, y) in enumerate(zip(x_values, y_values)):
                    x_center = x / 2
                    if i != 0:
                        _i = i
                        while _i > 0:
                            _i -= 1
                            x_center += fig.data[_i].x[j]
                    annotations.append(
                        {
                            "x": x_center,
                            "y": y,
                            "text": f"{x:.2f}%",
                            "font": {"color": "white"},
                            "showarrow": False,
                        }
                    )
            fig.update_layout(annotations=annotations)

            st.plotly_chart(fig, use_container_width=True)

        # Program studi
        else:
            df = self.dataframe[self.dataframe["Program Studi"] == self.input_prodi]
            df = df["Apa kategori perusahaan tempat Anda bekerja?"].isin(
                self.kategori_perusahaan
            )
            fig = px.bar(
                df,
                x=df.value_counts().tolist(),
                y=df.value_counts().index.tolist(),
                orientation="h",
                labels={"x": "Jumlah", "y": "Kategori Perusahaan"},
                title="Kategori Perusahaan per Prodi"
            )

            # Adding labels
            annotations = []
            max_x = max(fig.data[0]["x"])
            for fig_data in zip(fig.data[0]["y"], fig.data[0]["x"]):
                annotations.append(
                    {
                        "xref": "x1",
                        "yref": "y1",
                        "y": fig_data[0],
                        "x": fig_data[1] + 0.01 * max_x,
                        "text": str(fig_data[1]),
                        "font": {"size": 12},
                        "showarrow": False,
                    }
                )
            fig.update_layout(annotations=annotations)

            st.plotly_chart(fig, use_container_width=True)

    def show_bentuk_perusahaan_tempat_bekerja(self):
        # All
        if self.input_fakultas == "All" and self.input_prodi == "All":
            df = self.dataframe[
                self.dataframe[
                    "Apa jenis perusahaan / instansi / institusi tempat Anda bekerja sekarang?"
                ].isin(self.bentuk_perusahaan)
            ]
            df = df[
                "Apa jenis perusahaan / instansi / institusi tempat Anda bekerja sekarang?"
            ].value_counts()
            fig = px.pie(df, values=df.tolist(), names=df.index.tolist(), title="Bentuk Perusahaan Tempat Bekerja")
            st.plotly_chart(fig, use_container_width=True)

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            df = self.dataframe[
                self.dataframe["Fakultas/Sekolah"] == self.input_fakultas
            ]
            df = df[
                df[
                    "Apa jenis perusahaan / instansi / institusi tempat Anda bekerja sekarang?"
                ].isin(self.bentuk_perusahaan)
            ]
            df = df[
                "Apa jenis perusahaan / instansi / institusi tempat Anda bekerja sekarang?"
            ].value_counts()
            fig = px.pie(df, values=df.tolist(), names=df.index.tolist(), title="Bentuk Perusahaan Tempat Bekerja")
            st.plotly_chart(fig, use_container_width=True)

        # Program studi
        else:
            df = self.dataframe[self.dataframe["Program Studi"] == self.input_prodi]
            df = df[
                df[
                    "Apa jenis perusahaan / instansi / institusi tempat Anda bekerja sekarang?"
                ].isin(self.bentuk_perusahaan)
            ]
            df = df[
                "Apa jenis perusahaan / instansi / institusi tempat Anda bekerja sekarang?"
            ].value_counts()
            fig = px.pie(df, values=df.tolist(), names=df.index.tolist(), title="Bentuk Perusahaan Tempat Bekerja")
            st.plotly_chart(fig, use_container_width=True)

    def show_waktu_memulai_usaha(self):
        # All
        if self.input_fakultas == "All" and self.input_prodi == "All":
            df = self.dataframe["Kapankah Anda memulai usaha?"].value_counts()
            fig = px.pie(df, values=df.tolist(), names=df.index.tolist(), title="Waktu Memulai Usaha")
            st.plotly_chart(fig, use_container_width=True)

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            df = self.dataframe[
                self.dataframe["Fakultas/Sekolah"] == self.input_fakultas
            ]
            df = df["Kapankah Anda memulai usaha?"].value_counts()
            fig = px.pie(df, values=df.tolist(), names=df.index.tolist(), title="Waktu Memulai Usaha")
            st.plotly_chart(fig, use_container_width=True)

        # Program studi
        else:
            df = self.dataframe[self.dataframe["Program Studi"] == self.input_prodi]
            df = df["Kapankah Anda memulai usaha?"].value_counts()
            fig = px.pie(df, values=df.tolist(), names=df.index.tolist(), title="Waktu Memulai Usaha")
            st.plotly_chart(fig, use_container_width=True)

    def show_waktu_memulai_usaha_persebaran(self):
        # All
        if self.input_fakultas == "All" and self.input_prodi == "All":
            df = self.dataframe[
                [
                    "Berapa bulan waktu yang digunakan (sebelum kelulusan) untuk memulai usaha?",
                    "Berapa bulan waktu yang digunakan (sesudah kelulusan) untuk memulai usaha?",
                ]
            ]
            df = df.rename(
                columns={
                    "Berapa bulan waktu yang digunakan (sebelum kelulusan) untuk memulai usaha?": "sebelum lulus",
                    "Berapa bulan waktu yang digunakan (sesudah kelulusan) untuk memulai usaha?": "setelah lulus",
                }
            )
            fig = px.box(df, title="Waktu Memulai Usaha (Persebaran)")
            st.plotly_chart(fig, use_container_width=True)

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            df = self.dataframe[
                self.dataframe["Fakultas/Sekolah"] == self.input_fakultas
            ]
            df = df[
                [
                    "Berapa bulan waktu yang digunakan (sebelum kelulusan) untuk memulai usaha?",
                    "Berapa bulan waktu yang digunakan (sesudah kelulusan) untuk memulai usaha?",
                ]
            ]
            df = df.rename(
                columns={
                    "Berapa bulan waktu yang digunakan (sebelum kelulusan) untuk memulai usaha?": "sebelum lulus",
                    "Berapa bulan waktu yang digunakan (sesudah kelulusan) untuk memulai usaha?": "setelah lulus",
                }
            )
            fig = px.box(df, title="Waktu Memulai Usaha (Persebaran)")
            st.plotly_chart(fig, use_container_width=True)

        # Program studi
        else:
            df = self.dataframe[self.dataframe["Program Studi"] == self.input_prodi]
            df = df[
                [
                    "Berapa bulan waktu yang digunakan (sebelum kelulusan) untuk memulai usaha?",
                    "Berapa bulan waktu yang digunakan (sesudah kelulusan) untuk memulai usaha?",
                ]
            ]
            df = df.rename(
                columns={
                    "Berapa bulan waktu yang digunakan (sebelum kelulusan) untuk memulai usaha?": "sebelum lulus",
                    "Berapa bulan waktu yang digunakan (sesudah kelulusan) untuk memulai usaha?": "setelah lulus",
                }
            )
            fig = px.box(df, title="Waktu Memulai Usaha (Persebaran)")
            st.plotly_chart(fig, use_container_width=True)
