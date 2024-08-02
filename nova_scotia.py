import os
import streamlit as st
import pandas as pd
from df_global_search import DataFrameSearch


def nbj():
    
    # Directory containing the markdown files
    directory = 'nova_scotia'
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
        search_bar_columns = st.columns((2, 1, 0.5, 0.75, 1))
        with search_bar_columns[1]:
            search_text = st.text_input(
                "Search", label_visibility="collapsed", placeholder="Search Text"
            )
        with search_bar_columns[2]:
            is_regex = st.toggle("Regex", value=False)
        with search_bar_columns[3]:
            case_sensitive = st.toggle("Case Sensitive", value=False)
        with search_bar_columns[4]:
            highlight_match = st.toggle("Highlight Matching Cells", value=True)
        
        df = pd.read_csv(file_path)
        with DataFrameSearch(
            dataframe=df,
            text_search=search_text,
            case_sensitive=case_sensitive,
            regex_search=is_regex,
            highlight_matches=highlight_match,
        ) as df:
            st.dataframe(data=df, use_container_width=True, hide_index=True)