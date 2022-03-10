# Mairror Frontend

The Mairror Frontend

## Converting Anaconda environment to pip requirements

1. Use [conda-minify](https://github.com/jamespreed/conda-minify) to export only the top level requirements without the build string. It **must** be installed and executed within the conda `base` environment.

conda run --name base conda-minify -n mairror-frontend > environment.yml

2. Use the conversion tool `utils/conversor.py` to convert the requirements to a pip requirements file. It reads the previously generated YAML file and outputs a requirements.txt file in the same folder.

python utils/conversor.py

## Resources

- https://docs.streamlit.io/library/api-reference/media/st.image
- https://discuss.streamlit.io/t/streamlit-data-limit/8843
