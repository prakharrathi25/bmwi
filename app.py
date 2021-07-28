import os
from typing import final
import streamlit as st
import numpy as np

# Custom imports 
from multipage import MultiPage
# import your pages here
from pages import model_page, data_prep, home_page, error_analysis

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("BMWi Tool")
st.markdown('[Documentation](https://bmwi.readthedocs.io/)')

# The main app
app.add_page("Home Page", home_page.app)
app.add_page("Data Prep", data_prep.app)
app.add_page("Model Page", model_page.app)
app.add_page("Error Analysis", error_analysis.app)

# --- other pages ---
# app.add_page("Upload Data", data_upload.app)
# app.add_page("Data Analysis", data_analysis.app)
# app.add_page("Data Visualization", data_visualize.app)
# app.add_page("Merge Data", merge_data.app)
# app.add_page("Cluster Analysis", cluster_analysis.app)
# app.add_page("KModes Clustering", cluster_kmodes.app)
# app.add_page("Cluster Customization", cluster_customization.app)
# app.add_page("Network: Time-Series", network_numerical.app)
# app.add_page("Network: Categorical", network_categorical.app)
# app.add_page("Testing Page", cinny_page.app)
app.run()