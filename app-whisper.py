import streamlit as st
import numpy as np
import time
import whisper
import os

# Contexto
st.title('Whisper APP')
st.markdown('')

model_size = st.selectbox(
    'Selecciona el tamaño del modelo',
    ('tiny', 'base', 'small', 'medium', 'large'))

# Model size
if model_size:
    st.write(f'Has elegido el modelo: **whisper-{model_size}**')
    if model_size == 'medium':
        st.warning('Debes tener tener al menos 5GB VRAM', icon="⚠️")
    elif model_size == 'large':
        st.warning('Debes tener tener al menos 10GB VRAM', icon="⚠️")

    with st.spinner('Cargando modelo'):
        try:
            # Si hay problemas de recursos
            # @st.cache
            # def load_model():
            #     model = whisper.load_model(model_size)
            # model = load_model()
            model = whisper.load_model(model_size)
        except:
            st.error(
                'No tienes suficiente VRAM, prueba con un modelo más pequeño', icon="🚨")

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
            # Transcribir
            with st.spinner('Transcribiendo audio'):
                output = model.transcribe("./"+audio_name)
                transcripcion = output['text']
                lang = output['language']
            st.success('Audio transcrito correctamente', icon="✅")
            st.write(f'Lenguaje detectado: {lang}')
            output_text = st.text_area(
                'Transcripción', transcripcion, height=150, label_visibility='hidden')
        os.remove(audio_name)
