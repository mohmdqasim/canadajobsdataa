import pandas as pd
import streamlit as st
from pathlib import Path


st.set_page_config(page_title="Job Listings!!", layout="wide")
st.title("Job Portal!!")
file = Path(__file__).parent / "JobTitles.csv"
df = pd.read_csv(file)

st.dataframe(df, height=1500)
