import time

import streamlit as st
from api.requests import predict, upload_file


def app():

    st.title("Mairror: Image Predictor")
    st.caption("Image Uploader")

    image = st.file_uploader(
        "Please upload a image file: ", type=["png", "jpg"], accept_multiple_files=False
    )

    col1, col2, _ = st.columns([3, 5, 2])
    if image:
        bytes_image = image.read()
        image_name_real = image.name

        if len(image_name_real) > 15:
            image_name_real = image.name[10:]

    with col1:
        if st.button("Upload", help="Upload image") and image:

            files = {"file": (image_name_real, bytes_image)}
            upload_file(files)

    with col2:
        if st.button("Predict", help="Predict Image", key=1) and image:
            spinner()
            prediction = predict("raw/" + image_name_real)
            if prediction:
                st.text("The prediction was....")
                st.json(prediction)


def spinner():
    my_bar = st.progress(0)
    for percent_complete in range(0, 100, 20):
        time.sleep(0.5)
        my_bar.progress(percent_complete + 20)
    my_bar.empty()
