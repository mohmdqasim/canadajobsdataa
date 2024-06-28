import os
import streamlit as st
import pandas as pd


def govt():
    
    # Directory containing the markdown files
    directory = 'Jobs'
    # List all markdown files in the directory
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    # Streamlit application
    st.title('Canada Job Listings!!')
    # Display the list of markdown files in a sidebar
    st.write("Select a Tag")
    titles = []
    for elem in csv_files:
        titles.append(elem[:-4])
    selected_file = st.selectbox('', titles)
    # Display the content of the selected markdown file
    if selected_file:
        file_path = os.path.join(directory, selected_file+".csv")
        df = pd.read_csv(file_path)
        st.dataframe(df, height=700)