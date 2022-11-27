import streamlit as st

#Contexto
st.title('Whisper APP')
st.markdown('')

file = st.file_uploader("Suba el archivo mp3 a transcribit")

transcripcion = 'Esta es la transcripción de ejemplo v2'
output_text = st.text_area('Transcripción', transcripcion, height=150)