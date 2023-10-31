"""Module providing a function for image file manipulation."""
import base64
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


def replace_image(file_path, file_type):
    """Read and convert image files to base64-encoded strings."""
    if file_type == "svg":
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    else:
        with open(file_path, "rb") as file:
            return f"data:image/jpeg;base64,{base64.b64encode(file.read()).decode('utf-8')}"


@st.cache_data
def load_excel(file_name, sheet_name):
    return pd.read_excel("data/" + file_name, sheet_name=sheet_name)


def load_data():
    file_name = "Standarisasi_Kuesioner_2018-2022.xlsx"
    df2018 = load_excel(file_name, "2018")
    df2019 = load_excel(file_name, "2019")
    df2020 = load_excel(file_name, "2020")
    df2021 = load_excel(file_name, "2021")
    df2022 = load_excel(file_name, "2022")
    return df2018, df2019, df2020, df2021, df2022

def clustering(data, num_categories):
    num_categories = num_categories
    all_reasons = np.array(data)
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(all_reasons)
    kmeans = KMeans(n_clusters=num_categories, random_state=0)
    kmeans.fit(tfidf_matrix)
    reasons_categories = kmeans.labels_

    # Create a dictionary to group reasons by category
    category_reasons = {i: [] for i in range(num_categories)}

    # Generate titles for each category using batch processing
    category_titles = []

    for i, reason in enumerate(all_reasons):
        category = reasons_categories[i]
        category_reasons[category].append(reason)
    for category, reasons in category_reasons.items():
    # Calculate the centroid of the cluster (representative point)
        centroid = np.mean(tfidf_matrix.toarray()[np.array(reasons_categories) == category], axis=0)
        
        # Find the reason closest to the centroid
        representative_reason_index = np.argmax(np.dot(tfidf_matrix.toarray(), centroid))
        
        # Use the most representative reason as the category title
        category_titles.append(all_reasons[representative_reason_index])
    return category_titles,category_reasons

    # Display the 10 categories and their reasons
    # for i, (title, reasons) in enumerate(zip(category_titles, category_reasons.values())):
        # st.write(f"{title}")
        # for reason in reasons:
            # st.write(f"- {reason}")

def clustering_robust_v2(data):
    sil = []
    kmax = 20
    highest_score = float('-inf')
    real_num_categories = 0
    real_reason_categories = []
    all_reasons = np.array(data)

    # dissimilarity would not be defined for a single cluster, thus, minimum number of clusters should be 2
    for k in range(2, kmax+1):
      num_categories = k
      tfidf_vectorizer = TfidfVectorizer()
      tfidf_matrix = tfidf_vectorizer.fit_transform(all_reasons)
      kmeans = KMeans(n_clusters=num_categories, random_state=0)
      kmeans.fit(tfidf_matrix)
      reasons_categories = kmeans.labels_
      sil_score = silhouette_score(tfidf_matrix, reasons_categories, metric = 'euclidean')
      sil.append(sil_score)
      st.write("Iteration sil score value",k,sil_score)
      if sil_score > highest_score:
        st.write("Temporary best number of cluster we get",k)
        highest_score = sil_score
        real_num_categories = k
        real_reason_categories = reasons_categories
      else:
        break
    category_reasons = {i: [] for i in range(real_num_categories)}

    # Generate titles for each category using batch processing
    category_titles = []
    
    for i, reason in enumerate(all_reasons):
        category = real_reason_categories[i]
        category_reasons[category].append(reason)
    for category, reasons in category_reasons.items():
    # Calculate the centroid of the cluster (representative point)
        centroid = np.mean(tfidf_matrix.toarray()[np.array(reasons_categories) == category], axis=0)
        
        # Find the reason closest to the centroid
        representative_reason_index = np.argmax(np.dot(tfidf_matrix.toarray(), centroid))
        
        # Use the most representative reason as the category title
        category_titles.append(all_reasons[representative_reason_index])
    return category_reasons,category_titles