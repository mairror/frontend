import streamlit as st


def app():
    st.title("MAIRROR")
    st.caption("About this APP")
    st.markdown(
        """
    This APP provides a predictor using a model trained with Tensorflow an Keras
    to generate a prediction of the age and gender of the faces that appears
    in the image upload in the "Image prediction" page.
    """
    )
