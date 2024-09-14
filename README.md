# Installation and Run Steps

## Create Virual Environment with following command and Active in CLI
    - python -m venv .venv
    - .venv\Scripts\activate.bat   

## For cuda enabled Torch use this command:
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

## Install all dependencies by from requirments.txt
    - pip install -r requirements.txt

## Run streamlit application 
    - streamlit run 1_🏚_Home.py