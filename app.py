import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# add tittle
st.title('Data Analysis Applications')
st.subheader('This is a simple data analysis application Created by Umar Mehmood')

# load the data

# Dropdown to select dataset
dataset_options = ['iris', 'titanic', 'diamonds', 'tips']
selected_dataset = st.selectbox('Select a dataset', dataset_options)

# File uploader for user to upload their own dataset
uploaded_file = st.file_uploader("Or upload your own dataset (CSV file)", type="csv")

# Load the selected dataset or the uploaded file
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("User uploaded dataset:")
else:
    if selected_dataset == 'iris':
        data = sns.load_dataset('iris')
    elif selected_dataset == 'titanic':
        data = sns.load_dataset('titanic')
    elif selected_dataset == 'diamonds':
        data = sns.load_dataset('diamonds')
    elif selected_dataset == 'tips':
        data = sns.load_dataset('tips')
    st.write(f"Selected {selected_dataset}:")

st.write(data)

# Display the number of rows and columns from the selected dataset
num_rows = data.shape[0]# number of rows
num_cols = data.shape[1]# number of columns
st.write(f"The dataset has {num_rows} rows and {num_cols} columns.")

# Display the columns name from selected data with their data types 
st.write("Column Names and data types:")
st.write(data.dtypes)

# print the null values if those are > 0
if data.isnull().sum().sum() > 0:
    st.write("Missing values in the dataset:")
    st.write(data.isnull().sum().sort_values(ascending=False))
else:
    st.write("No missing values in the dataset.")   
    
# Display the summary statistics from selected datasets
st.write("Summary Statistics:")
st.write(data.describe(include='all'))

# select the column to be used as hue in pairplot
hue_column = st.selectbox('Select a column to be used as hue in pairplot', data.columns)
st.pyplot(sns.pairplot(data, hue=hue_column))

# Show me app attractive background color for the app
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0;
        }
    </style>
    """,
    unsafe_allow_html=True
    
)


         
