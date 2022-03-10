import json
from typing import Dict, Union

import requests
import streamlit as st
from config.settings import get_settings

settings = get_settings()
headers = {"X-Api-Key": settings.API_KEY}


def upload_file(files: Dict) -> None:
    data = {"source": "streamlit"}
    try:
        r = requests.post(
            settings.API_URL + settings.API_UPLOAD_PATH,
            files=files,
            data=data,
            headers=headers,
        )
        if r.status_code == 201:
            st.info("File sucessfully uploaded.")
        else:
            st.error("There was an error uploaded your file. Please try again.")
    except Exception:
        st.error("There was an issue uploaded your file.")


def predict(image: str) -> Union[Dict, None]:
    data = {"image_id": image}
    try:
        r = requests.post(
            settings.API_URL + settings.API_PREDICT_PATH,
            data=json.dumps(data),
            headers=headers,
        )
        if r.status_code == 200:
            return json.loads(r.text)
        else:
            st.error("There was an error predicting your image.")
    except Exception:
        st.error("There was an exception predicting your image.")
