# resume_script

Parse:
    name (x)
    email (x)
    phone (x)
    location (x)
    language (x)
    skills (x)
    experience (x)

## Install

    ### install dependencies
    sudo apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 virtualenv libsox-fmt-mp3 sox libjpeg-dev swig libpulse-dev

    ### install packages
    pip install -r requirements.txt
    python -m spacy download en_core_web_lg
   
    ### Versions
    . main.py --> Script whitout nltk
    . main_2.py --> Script with nltk