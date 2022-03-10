import streamlit as st


def app():
    st.title("MAIRROR")
    st.caption("Welcome to the Mairror Image Predictor")

    col1, col2, col3 = st.columns([4, 6, 4])

    col2.image(
        "https://avatars.githubusercontent.com/u/99807917?s=400&u=5f9547743b7c79cca27c8a7197c96ab3856df21d&v=4",
        use_column_width="never",
    )
