import streamlit as st
from multiapp.page_selection import MultiApp
from pages import about, home, image_prediction

st.set_page_config(
    layout="wide",
    page_title="Mairror",
    menu_items={
        "Get Help": "https://github.com/mairror/mairror/blob/main/README.md",
        "Report a bug": "https://github.com/mairror/frontend/issues",
        "About": "# Welcome to Mairror!",
    },
)

app = MultiApp()

app.add_pages("Home", home.app)
app.add_pages("Image Prediction", image_prediction.app)
app.add_pages("About", about.app)

app.run()
