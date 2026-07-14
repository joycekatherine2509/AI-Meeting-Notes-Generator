import streamlit as st
from faster_whisper import WhisperModel

@st.cache_resource
def load_model():
    return WhisperModel(
        "base",
        device="cpu",
        compute_type="int8"
    )

def transcribe_audio(file):
    model = load_model()

    segments, info = model.transcribe(file)

    transcript = ""

    for segment in segments:
        transcript += segment.text + " "

    return transcript