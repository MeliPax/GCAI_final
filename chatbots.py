import streamlit as st
import numpy as np
import pandas as pd
import Overview, Introduction, Results,  Recommendations, Conclusion, Methodology

PAGES = {
    "Overview": Overview,
    "Introduction": Introduction,
    "Methodology": Methodology,
    "Results": Results,
    "Recommendations": Recommendations,
    "Conclusions": Conclusion,
}


selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.chatbots()