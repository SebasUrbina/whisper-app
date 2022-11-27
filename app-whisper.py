import streamlit as st
import numpy as np
# import whisper

# Contexto
st.title('Whisper APP')
st.markdown('')

audio_file = st.file_uploader("Suba el archivo mp3 a transcribir")

# Cargar audio

if audio_file is not None:
    st.audio(audio_file, format='audio/wav')


# Cargar modelo
# model = whisper.load_model("base")
# transcripcion = model.transcribe('despacito.mp3')

if st.button('Transcribir audio'):
    st.write('Transcribiendo audio...')
    transcripcion = 'Esta es la transcripción de ejemplo v2'
    output_text = st.text_area('Transcripción', transcripcion, height=150)

else:
    st.write('Prueba')
