import streamlit as st
import plotly.express as px
import pandas as pd


class BabEmpat:
    def __init__(self, input_tahun, input_fakultas, input_prodi, dataframe):
        self.input_tahun = input_tahun
        self.input_fakultas = input_fakultas
        self.input_prodi = input_prodi
        self.dataframe = dataframe
        self.valid_categories = ["multinasional", "nasional", "lokal"]

    def showKategoriPerusahaanPerProdi(self):
        # All
        if self.input_fakultas == "All":
            st.write("")
            st.write("Kategori Perusahaan per Prodi")
            df = self.dataframe[
                self.dataframe["Apa kategori perusahaan tempat Anda bekerja?"].isin(
                    self.valid_categories
                )
            ]
            pivot_df = df.pivot_table(
                index="Program Studi",
                columns="Apa kategori perusahaan tempat Anda bekerja?",
                aggfunc="size",
                fill_value=0,
            )
            pivot_df_percentage = pivot_df.div(pivot_df.sum(axis=1), axis=0) * 100
            fig = px.bar(
                pivot_df_percentage,
                x=self.valid_categories,
                labels={"value": "Persentase"},
            )

            # Adding labels
            annotations = []
            for i in range(len(fig.data)):
                bar_data = fig.data[i]
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
                        dict(
                            x=x_center,
                            y=y,
                            text=f"{x:.2f}%",
                            font=dict(color="white"),
                            showarrow=False,
                        )
                    )
            fig.update_layout(annotations=annotations)

            st.plotly_chart(fig, use_container_width=True)

        # Fakultas
        elif self.input_fakultas != "All" and self.input_prodi == "All":
            st.write("")
            st.write("Kategori Perusahaan per Prodi")
            df = self.dataframe[
                self.dataframe["Fakultas/Sekolah"] == self.input_fakultas
            ]
            df = df[
                df["Apa kategori perusahaan tempat Anda bekerja?"].isin(
                    self.valid_categories
                )
            ]
            pivot_df = df.pivot_table(
                index="Program Studi",
                columns="Apa kategori perusahaan tempat Anda bekerja?",
                aggfunc="size",
                fill_value=0,
            )
            pivot_df_percentage = pivot_df.div(pivot_df.sum(axis=1), axis=0) * 100
            fig = px.bar(
                pivot_df_percentage,
                x=self.valid_categories,
                labels={"value": "Persentase"},
            )

            # Adding labels
            annotations = []
            for i in range(len(fig.data)):
                bar_data = fig.data[i]
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
                        dict(
                            x=x_center,
                            y=y,
                            text=f"{x:.2f}%",
                            font=dict(color="white"),
                            showarrow=False,
                        )
                    )
            fig.update_layout(annotations=annotations)

            st.plotly_chart(fig, use_container_width=True)

        # Program studi
        else:
            st.write("")
            st.write("Kategori Perusahaan per Prodi")
            df = self.dataframe[self.dataframe["Program Studi"] == self.input_prodi]
            df = df["Apa kategori perusahaan tempat Anda bekerja?"]
            x = ["multinasional", "nasional", "lokal"]
            df = df[df.isin(x)]
            fig = px.bar(
                df,
                x=df.value_counts().tolist(),
                y=df.value_counts().index.tolist(),
                orientation="h",
                labels={"x": "Jumlah", "y": "Kategori Perusahaan"},
            )

            # Adding labels
            annotations = []
            max_x = max(fig.data[0]["x"])
            for fig_data in zip(fig.data[0]["y"], fig.data[0]["x"]):
                annotations.append(
                    dict(
                        xref="x1",
                        yref="y1",
                        y=fig_data[0],
                        x=fig_data[1] + 0.01 * max_x,
                        text=str(fig_data[1]),
                        font=dict(size=12),
                        showarrow=False,
                    )
                )
            fig.update_layout(annotations=annotations)

            st.plotly_chart(fig, use_container_width=True)
