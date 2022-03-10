#!/bin/bash

mkdir -p ~/.streamlit/

echo "\
[server]
headless = true
maxUploadSize = 20
[theme]
base=\"dark\"
" > ~/.streamlit/config.toml

streamlit run main.py
