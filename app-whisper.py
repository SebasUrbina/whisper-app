import streamlit as st
import numpy as np
import time
import whisper
import os

# Contexto
st.title('Whisper APP')
st.markdown('')

with st.spinner('Cargando modelo'):
    model = whisper.load_model("tiny")

audio_file = st.file_uploader("Suba el archivo mp3 a transcribir")
# Cargar audio
if audio_file is not None:
    st.audio(audio_file, format='audio/wav')
    audio_name = audio_file.name
    with open(audio_name, 'wb') as f:
        f.write(audio_file.read())

    # Cargar modelo
    if st.button('Transcribir audio'):
        # st.warning('Transcribiendo audio...', icon="⚠️")
        with st.spinner('Transcribiendo audio'):
            output = model.transcribe(audio_name)
            transcripcion = output['text']
        st.success('Audio transcrito correctamente', icon="✅")
        output_text = st.text_area(
            'Transcripción', transcripcion, height=150, label_visibility='hidden')
    os.remove(audio_name)
