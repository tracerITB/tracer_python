import streamlit as st
import plotly.express as px
from src.bab import Bab


class BabLima(Bab):
    def __init__(self, *args):
        super().__init__(*args)
        self.kesesuaian = ["ya", "tidak"]
        self.bidang_usaha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']

    def show(self):
        self.show_kesesuaian_kuliah_dengan_pekerjaan()
        self.show_kesesuaian_kuliah_dengan_pekerjaan_per_prodi()
        self.show_kategori_bidang_usaha()
        self.show_kategori_bidang_usaha_per_prodi()
        self.show_kategori_jenis_pekerjaan()
        self.show_jabatan()
        self.show_jabatan_per_prodi()
        self.show_penghasilan_dan_bonus(True)
        self.show_penghasilan_dan_bonus(False)
        self.show_penghasilan_per_prodi()
        self.show_bonus_per_prodi()

    def show_kesesuaian_kuliah_dengan_pekerjaan(self):
        # All
        if self.input_fakultas == "All":
            df = self.dataframe[
                self.dataframe["Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"].isin(
                    self.kesesuaian
                )
            ]
            df = df[
                "Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"
            ].value_counts()
            fig = px.pie(df, values=df.tolist(), names=df.index.tolist(), title="Kesesuaian Kuliah dengan Pekerjaan")
            st.plotly_chart(fig, use_container_width=True)

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            df = self.dataframe[
                self.dataframe["Fakultas/Sekolah"] == self.input_fakultas
            ]
            df = df[
                df["Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"].isin(
                    self.kesesuaian
                )
            ]
            df = df[
                "Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"
            ].value_counts()
            fig = px.pie(df, values=df.tolist(), names=df.index.tolist(), title="Kesesuaian Kuliah dengan Pekerjaan")
            st.plotly_chart(fig, use_container_width=True)

        # Program studi
        else:
            df = self.dataframe[self.dataframe["Program Studi"] == self.input_prodi]
            df = df[
                df["Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"].isin(
                    self.kesesuaian
                )
            ]
            df = df[
                "Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"
            ].value_counts()
            fig = px.pie(df, values=df.tolist(), names=df.index.tolist(), title="Kesesuaian Kuliah dengan Pekerjaan")
            st.plotly_chart(fig, use_container_width=True)

    def show_kesesuaian_kuliah_dengan_pekerjaan_per_prodi(self):
        # All
        if self.input_fakultas == "All":
            df = self.dataframe[
                self.dataframe["Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"].isin(
                    self.kesesuaian
                )
            ]
            df = df.pivot_table(
                index="Program Studi",
                columns="Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?",
                aggfunc="size",
                fill_value=0,
            )
            df = df.div(df.sum(axis=1), axis=0) * 100
            fig = px.bar(
                df,
                x=self.kesesuaian,
                labels={"value": "Persentase"},
                title="Kesesuaian Kuliah dengan Pekerjaan per Prodi"
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
                df["Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"].isin(
                    self.kesesuaian
                )
            ]
            df = df.pivot_table(
                index="Program Studi",
                columns="Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?",
                aggfunc="size",
                fill_value=0,
            )
            df = df.div(df.sum(axis=1), axis=0) * 100
            fig = px.bar(
                df,
                x=self.kesesuaian,
                labels={"value": "Persentase"},
                title="Kesesuaian Kuliah dengan Pekerjaan per Prodi"
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
            df = df["Apakah pekerjaan yang Anda lakukan di tempat bekerja sesuai dengan bidang kuliah?"].isin(
                self.kesesuaian
            )
            df = df.replace({True: "ya", False: "tidak"})
            fig = px.bar(
                df,
                x=df.value_counts().tolist(),
                y=df.value_counts().index.tolist(),
                orientation="h",
                labels={"x": "Jumlah", "y": "Kesesuaian Kuliah dengan Pekerjaan"},
                title="Kesesuaian Kuliah dengan Pekerjaan per Prodi"
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

    def show_kategori_bidang_usaha(self):
        # All
        if self.input_fakultas == "All":
            df = self.dataframe[self.dataframe["Bidang usaha bekerja"].isin(
                self.bidang_usaha
            )]
            df = df[
                "Bidang usaha bekerja"
            ].value_counts().sort_index()
            fig = px.pie(df, values=df.tolist(), names=df.index.tolist(), title="Kategori Bidang Usaha")
            fig.update_traces(sort=False)
            st.plotly_chart(fig, use_container_width=True)

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            df = self.dataframe[
                self.dataframe["Fakultas/Sekolah"] == self.input_fakultas
            ]
            df = df[df["Bidang usaha bekerja"].isin(
                self.bidang_usaha
            )]
            df = df[
                "Bidang usaha bekerja"
            ].value_counts().sort_index()
            fig = px.pie(df, values=df.tolist(), names=df.index.tolist(), title="Kategori Bidang Usaha")
            fig.update_traces(sort=False)
            st.plotly_chart(fig, use_container_width=True)

        # Program studi
        else:
            df = self.dataframe[self.dataframe["Program Studi"] == self.input_prodi]
            df = df[df["Bidang usaha bekerja"].isin(
                self.bidang_usaha
            )]
            df = df[
                "Bidang usaha bekerja"
            ].value_counts().sort_index()
            fig = px.pie(df, values=df.tolist(), names=df.index.tolist(), title="Kategori Bidang Usaha")
            fig.update_traces(sort=False)
            st.plotly_chart(fig, use_container_width=True)

    def show_kategori_bidang_usaha_per_prodi(self):
        # All
        if self.input_fakultas == "All":
            df = self.dataframe[
                self.dataframe["Bidang usaha bekerja"].isin(
                    self.kesesuaian
                )
            ]
            df = df.pivot_table(
                index="Program Studi",
                columns="Bidang usaha bekerja",
                aggfunc="size",
                fill_value=0,
            )
            df = df.div(df.sum(axis=1), axis=0) * 100
            fig = px.bar(
                df,
                x=self.kesesuaian,
                labels={"value": "Persentase"},
                title="Kategori Bidang Usaha per Prodi"
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
                df["Bidang usaha bekerja"].isin(
                    self.kesesuaian
                )
            ]
            df = df.pivot_table(
                index="Program Studi",
                columns="Bidang usaha bekerja",
                aggfunc="size",
                fill_value=0,
            )
            df = df.div(df.sum(axis=1), axis=0) * 100
            fig = px.bar(
                df,
                x=self.kesesuaian,
                labels={"value": "Persentase"},
                title="Kategori Bidang Usaha per Prodi"
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
            df = df[df["Bidang usaha bekerja"].isin(
                self.bidang_usaha
            )]
            df = df["Bidang usaha bekerja"].value_counts().sort_index(ascending=False)
            fig = px.bar(
                df,
                x=df.tolist(),
                y=df.index.tolist(),
                orientation="h",
                labels={"x": "Jumlah", "y": "Kategori Bidang Usaha per Prodi"},
                title="Kategori Bidang Usaha per Prodi",
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

    def show_penghasilan_dan_bonus(self, is_vertical_bar):
        if is_vertical_bar:
            # All
            if self.input_fakultas == "All":
                st.warning("Not yet implemented.")

            # Fakultas
            elif self.input_fakultas != "All" and self.input_prodi == "All":
                st.warning("Not yet implemented.")

            # Program studi
            else:
                st.warning("Not yet implemented.")
        else:
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
