import streamlit as st
import pandas as pd

st.title("Aplikasi Filter Sentimen Komentar (File PKL)")

# Load dataset dari pickle
@st.cache_data
def load_data():
    df = pd.read_pickle("processed_jumbo.pkl")
    return df

df = load_data()

# Tampilkan informasi dasar
st.subheader("Informasi Dataset")
if 'sentimen' in df.columns and 'komentar' in df.columns:
    st.write(f"Jumlah total komentar: {len(df)}")
    st.write(df['sentimen'].value_counts())
else:
    st.error("Kolom 'sentimen' atau 'komentar' tidak ditemukan!")

# Filter berdasarkan sentimen
st.subheader("Filter Komentar Berdasarkan Sentimen")
sentimen_filter = st.selectbox("Pilih sentimen:", ["positif", "netral", "negatif"])

# Tampilkan hasil filter
if 'sentimen' in df.columns and 'komentar' in df.columns:
    filtered_df = df[df['sentimen'].str.lower() == sentimen_filter.lower()]
    st.write(f"Menampilkan {len(filtered_df)} komentar dengan sentimen: {sentimen_filter}")
    st.dataframe(filtered_df[['komentar', 'sentimen']])
