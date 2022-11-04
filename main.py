# from audiototext import audio_to_text
import streamlit as st
import os
from audiototext.audiototext import audio_to_text
from stemming.textstemmer import stemIt
import json


def main():
    os.getcwd()
    os.chdir(".")
    BASE_DIR = os.getcwd()

    # BASE_DIR = f"C:/Users/{userName}/Desktop/NLP/"

    json_file_path = f"{BASE_DIR}DIR_LIST/dir_list.json"
    f = open(json_file_path)
    json_dict = json.load(f)

    audioinput = f"{BASE_DIR}/{json_dict['0']['AUDIO_INPUT']}"
    unstemmedtextoutput = f"{BASE_DIR}/{json_dict['0']['UNSTEMMED_TEXT_OUTPUT']}/unstemmedtextoutput"
    stemmedtextoutput = f"{BASE_DIR}/{json_dict['0']['STEMMED_TEXT_OUTPUT']}/stemmedtextoutput"
    audiooutput = f"{BASE_DIR}/{json_dict['0']['AUDIO_OUTPUT']}"

    audio_file = open(audio_file, 'rb')
    audio_bytes = audio_file.read()
    st.header("Hii")
    with st.container():
        st.text("Welcome to Audio Stemmer")
        st.text("This is the sample unstemmed audio")
        st.audio(audio_bytes, format='audio/wav')
    # car.wav is the audio file present in this project
    file_name = input("Please enter your Audio file name:")
    audio_file = os.path.join(audioinput, file_name)

    # def audio_text():
    #     at1=audio_to_text()
    #     at1.text_creator(audioinput)

    # audio_file = "audio/car.wav"
    # complete_audio_path = os.path.join(BASE_DIR, car_file)
    # def audio_stemmer():
    at1 = audio_to_text()
    at1.text_creator(audioinput)
    stemIt()


if __name__ == "__main__":

    main()
