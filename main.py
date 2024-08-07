import pandas as pd
import streamlit as st
from pathlib import Path
from streamlit_option_menu import option_menu
from Canadajobs import canada
from GovtJobs import govt
from nova_scotia import nova
from nbjobs import nbj
from jobspei import peijobs
from IndeedJobs import indeed

st.set_page_config(page_title="Job Listings!!", layout="wide")

pages = {
    "Canada Jobs": canada,
    "Nova Sotia": nova,
    "NbJobs": nbj,
    "Govt Jobs": govt,
    "Jobs Pei": peijobs,
    "Indeed Jobs": indeed,
}

with st.sidebar:
    selected = option_menu(
        menu_title = "Job Portal",
        options = list(pages.keys()),
        icons = ["house", "person-arms-up", "book"],
        menu_icon = "robot",
        default_index = 0
    )

pages[selected]()


