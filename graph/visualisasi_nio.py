import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from cek_similarity import sentence_similarity

def display_asal_modal_usaha(df_selection):
    df_sumber_modal_usaha = pd.DataFrame({'Prodi':df_selection["Program Studi"],'Sumber Modal':df_selection["Berasal dari mana modal yang Anda gunakan untuk membangun usaha pertama kali?"]})
    df_sumber_modal_usaha = df_sumber_modal_usaha.dropna()
    sumber_modal_value = df_sumber_modal_usaha.groupby(['Sumber Modal'],as_index=False).Prodi.count()
    df_sumber_modal_usaha_new = pd.DataFrame({'Sumber Modal':sumber_modal_value["Sumber Modal"],'Total':sumber_modal_value["Prodi"]})
    #st.dataframe(df_sumber_modal_usaha)

    fig_sumber_modal_usaha = px.bar(
        df_sumber_modal_usaha_new,
        x="Total",
        y="Sumber Modal",
        orientation = "h",
        template = "plotly_white",
    )
    st.header("Grafik sumber modal usaha")
    st.plotly_chart(fig_sumber_modal_usaha)

def display_asal_modal_lanjut_studi(df_selection):
    df_sumber_modal_kuliah = pd.DataFrame({'Prodi':df_selection["Program Studi"],'Sumber Modal':df_selection["Darimanakah sumber biaya studi Anda?"]})
    df_sumber_modal_kuliah = df_sumber_modal_kuliah.dropna()
    sumber_modal = df_sumber_modal_kuliah.groupby(['Sumber Modal'],as_index=False).Prodi.count()
    st.dataframe(df_sumber_modal_kuliah)

    df_sumber_modal_kuliah_new = pd.DataFrame({'Sumber Modal':sumber_modal["Sumber Modal"],'Total':sumber_modal["Prodi"]})
    st.dataframe(df_sumber_modal_kuliah_new)

    fig_sumber_modal_kuliah, ax_sumber_modal_kuliah = plt.subplots()
    ax_sumber_modal_kuliah.pie(df_sumber_modal_kuliah_new['Total'],labels=df_sumber_modal_kuliah_new['Sumber Modal'],autopct='%1.1f%%',startangle=90)
    ax_sumber_modal_kuliah.axis('equal')
    st.header("Grafik sumber modal melanjutkan studi")
    st.pyplot(fig_sumber_modal_kuliah)

def display_penghasilan_(df_selection):
    df_penghasilan = pd.DataFrame({'Prodi':df_selection['Program Studi'],'Penghasilan':df_selection['Berapa gaji per bulan saat ini di luar bonus? (dalam Rupiah)']})
    df_penghasilan = df_penghasilan.dropna()
    penghasilan_per_prodi_mean = df_penghasilan.groupby(['Prodi'],as_index=False).Penghasilan.mean().round()
    penghasilan_per_prodi_median = df_penghasilan.groupby(['Prodi'],as_index=False).Penghasilan.median()
    # penghasilan_per_prodi_coba = df_penghasilan['Prodi'].iloc[0:10]
    #st.write(prodis,penghasilans)
    df_penghasilan_prodi_mean = pd.DataFrame({'Prodi':penghasilan_per_prodi_mean['Prodi'],'Penghasilan':penghasilan_per_prodi_mean['Penghasilan']})

    #st.dataframe(df_penghasilan)
    #st.dataframe(df_penghasilan_prodi_mean)
    st.write(penghasilan_per_prodi_mean)
    st.write(penghasilan_per_prodi_median)

    fig_penghasilan = px.bar(
        penghasilan_per_prodi_median,
        x="Penghasilan",
        y="Prodi",
        orientation = "h",
        template = "plotly_white",
    )
    st.header("Grafik Penghasilan")
    st.plotly_chart(fig_penghasilan)

def display_omset(df_selection):
    df_omset = pd.DataFrame({'Prodi':df_selection['Program Studi'],'Omset':df_selection['Berapa omset rata-rata perbulan? (dalam Rupiah)']})
    df_omset = df_omset.dropna()
    df_omset_anomali = df_omset[df_omset.Prodi == 'Teknik Geologi']
    omset_per_prodi_mean = df_omset.groupby(['Prodi'],as_index=False).Omset.mean().round()
    omset_per_prodi_median = df_omset.groupby(['Prodi'],as_index=False).Omset.median()
    # penghasilan_per_prodi_coba = df_penghasilan['Prodi'].iloc[0:10]
    #st.write(prodis,penghasilans)
    df_omset_prodi_mean = pd.DataFrame({'Prodi':omset_per_prodi_mean['Prodi'],'Omset':omset_per_prodi_mean['Omset']})

    #st.dataframe(df_penghasilan)
    #st.write(df_omset_anomali)
    #st.dataframe(df_omset_prodi_mean)
    st.dataframe(omset_per_prodi_mean)
    st.dataframe(omset_per_prodi_median)
    # st.write(penghasilan_per_prodi_mean)
    # st.write(penghasilan_per_prodi_median)

    fig_omset = px.bar(
        omset_per_prodi_median,
        x="Omset",
        y="Prodi",
        orientation = "h",
        template = "plotly_white",
    )
    st.header("Grafik omset")
    st.plotly_chart(fig_omset)

def display_kategori_bidang_usaha_fakultas(df_selection):
    df_bidang_usaha = pd.DataFrame({'Prodi':df_selection['Program Studi'],'Bidang Usaha':df_selection['Bidang usaha wirausaha/wiraswasta']})
    df_bidang_usaha = df_bidang_usaha.dropna()
    bidang_usaha = df_bidang_usaha.groupby(['Bidang Usaha'],as_index=False).Prodi.count()

    df_bidang_usaha_new = pd.DataFrame({'Bidang Usaha':bidang_usaha["Bidang Usaha"],'Total':bidang_usaha["Prodi"]})
    st.dataframe(df_bidang_usaha)
    st.dataframe(df_bidang_usaha_new)
    #df_bidang_usaha_new = df_bidang_usaha_new.dropna()

    # st.dataframe(df_bidang_usaha)
    # st.write(bidang_usaha)
    # st.dataframe(df_bidang_usaha_new)


    fig_bidang_usaha, ax_bidang_usaha = plt.subplots()
    ax_bidang_usaha.pie(df_bidang_usaha_new['Total'],labels=df_bidang_usaha_new['Bidang Usaha'],autopct='%1.1f%%',startangle=90)
    ax_bidang_usaha.axis('equal')
    st.header("Grafik Kategori Bidang Usaha")
    st.pyplot(fig_bidang_usaha)

def display_status_bekerja_sebelumnya(df_selection):
    df_pernah_bekerja_sebelumnya = pd.DataFrame({'Prodi':df_selection["Program Studi"],'Status sebelumnya':df_selection["Apakah Anda pernah bekerja sebelumnya?"]})
    df_pernah_bekerja_sebelumnya = df_pernah_bekerja_sebelumnya.dropna()
    pernah_bekerja_sebelumnya_value = df_pernah_bekerja_sebelumnya.groupby(['Status sebelumnya'],as_index=False).Prodi.count()
    df_pernah_bekerja_sebelumnya_new = pd.DataFrame({'Status sebelumnya':pernah_bekerja_sebelumnya_value["Status sebelumnya"],'Total':pernah_bekerja_sebelumnya_value["Prodi"]})
    #st.dataframe(df_sumber_modal_usaha)

    fig_pernah_bekerja_sebelumnya = px.bar(
        df_pernah_bekerja_sebelumnya_new,
        x="Status sebelumnya",
        y="Total",
        orientation = "v",
        template = "plotly_white",
    )
    st.header("Grafik Pernah Bekerja Sebelumnya")
    st.plotly_chart(fig_pernah_bekerja_sebelumnya)