import os
import streamlit as st
st.set_page_config(page_title="Job Listings!!", layout="wide")

def canada():
    # Directory containing the markdown files
    directory = 'Jobs'
    # List all markdown files in the directory
    markdown_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    # Streamlit application
    st.title('Job Listings!!')
    # Display the list of markdown files in a sidebar
    st.header("Select a Tag")
    selected_file = st.selectbox('', markdown_files)
    # Display the content of the selected markdown file
    if selected_file:
        st.subheader(selected_file)
        file_path = os.path.join(directory, selected_file)
        df = pd.read_csv(file_path)
        st.dataframe(df, height=1500)




