import time
import uuid

import streamlit as st
from api.requests import predict, upload_file


def app():
    st.title("Mairror: Image Predictor")
    st.caption("Image Uploader")

    image = st.file_uploader(
        "Please upload a image file: ", type=["png", "jpg"], accept_multiple_files=False
    )
    if image:
        bytes_image = image.read()
        image_name_real = image.name

        if len(image_name_real) > 15:
            image_name_real = image.name[10:]

        image_name = str(uuid.uuid1()) + "_" + image.name

        files = {"file": (image_name, bytes_image)}
        upload_file(files)

    if st.button("Predict") and image:
        spinner()
        prediction = predict("raw/" + image_name)
        if prediction:
            st.text("The prediction was....")
            st.json(prediction)


def spinner():
    my_bar = st.progress(0)
    for percent_complete in range(0, 100, 20):
        time.sleep(0.5)
        my_bar.progress(percent_complete + 20)
    my_bar.empty()
