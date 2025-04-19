import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Data Analysis Dashboard")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.dataframe(data.head())

    st.subheader("Summary Statistics")
    st.write(data.describe())

    st.subheader("Correlation Matrix")
    corr = data.corr()
    st.write(corr)

    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    st.subheader("Select columns for scatter plot")
    numeric_columns = data.select_dtypes(include=np.number).columns.tolist()
    x_axis = st.selectbox("X axis", numeric_columns)
    y_axis = st.selectbox("Y axis", numeric_columns)

    if x_axis and y_axis:
        st.subheader(f"Scatter Plot: {x_axis} vs {y_axis}")
        fig2, ax2 = plt.subplots()
        ax2.scatter(data[x_axis], data[y_axis])
        ax2.set_xlabel(x_axis)
        ax2.set_ylabel(y_axis)
        st.pyplot(fig2)
