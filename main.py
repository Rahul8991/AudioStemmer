# from audiototext import audio_to_text
import streamlit as st
import os
from audiototext.audiototext import audio_to_text


BASE_DIR = r"C:/Users/Rahul/Desktop/NLP/audio/"
car_file = "car.wav"
complete_audio_path = os.path.join(BASE_DIR, car_file)

obj = audio_to_text()
obj.text_creator(complete_audio_path)

audio_file = open(complete_audio_path, 'rb')
audio_bytes = audio_file.read()


if __name__ == "__main__":
    st.header("Hii")
    with st.container():
        st.text("Welcome to Audio Stemmer")
        st.text("This is the sample unstemmed audio")
        st.audio(audio_bytes, format='audio/wav')
