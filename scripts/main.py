# from audiototext import audio_to_text
# import streamlit as st
import os
from audiototext.audiototext import audio_to_text
from stemming.textstemmer import stemIt
from sentimentanalysis.sentiment import sentiment_calculator
import json

BASE_DIR = os.getcwd()

# BASE_DIR = f"C:/Users/{userName}/Desktop/NLP/"

json_file_path = f"{BASE_DIR}/DIR_LIST/dir_list.json"
f = open(json_file_path)
json_dict = json.load(f)
print("Gathering Paths from json file...")
audioinput = f"{BASE_DIR}/{json_dict['0']['AUDIO_INPUT']}"
unstemmedtextoutput = f"{BASE_DIR}/{json_dict['0']['UNSTEMMED_TEXT_OUTPUT']}/unstemmedtextoutput"
stemmedtextoutput = f"{BASE_DIR}/{json_dict['0']['STEMMED_TEXT_OUTPUT']}/stemmedtextoutput"
audiooutput = f"{BASE_DIR}/{json_dict['0']['AUDIO_OUTPUT']}"
positivewords = f"{BASE_DIR}/{json_dict['0']['WORDS_LIST']}/positive_words"
negativewords = f"{BASE_DIR}/{json_dict['0']['WORDS_LIST']}/negative_words"

print("Path generated...")

# def main(audio_file_name, audio_file_type):


#     try:
# -----------------------------------------------------------------------------
# audio_file = open(audio_file, 'rb')
# audio_bytes = audio_file.read()
# st.header("Hii")
# with st.container():
#     st.text("Welcome to Audio Stemmer")
#     st.text("This is the sample unstemmed audio")
#     st.audio(audio_bytes, format='audio/wav')
# ---------------------------------------------------------------------------------
# car.wav is the audio file present in this project
# file_name = input("Please enter your Audio file name:")
# file_type = input("Choose your file type: (wav,mp3,mp4) ")

# -----------------------------------------------------------------
# def audio_text():                                                    |
#     at1=audio_to_text()                                              |
#     at1.text_creator(audioinput)                                     |
# audio_file = "audio/car.wav"                                         |
# complete_audio_path = os.path.join(BASE_DIR, car_file)               |
# def audio_stemmer():                                                 |
# --------------------------------------------------------------------
try:
    def audioToText(audio_file_name, audio_file_type):
        audio_file_path = os.path.join(
            audioinput, f"{audio_file_name.strip()}.{audio_file_type.strip()}")
        print(audio_file_path)
        print("---------------Audio To Text------------------")
        at1 = audio_to_text()
        convertedTextOutput = at1.text_creator(
            audio_file_path, unstemmedtextoutput)
        print("Audio to Text Conversion Finished...")
        print("-------------------------------------------------")
        return convertedTextOutput

    def textStemming(audio_file_name, audio_file_type):
        audioToText(audio_file_name, audio_file_type)
        print("-------------------Stemming Process----------------")
        stemmed = stemIt(unstemmedtextoutput, stemmedtextoutput)
        print("Stemming Process Finished...")
        print("---------------------------------------------------")
        return stemmed

    def sentimentAnalysis(audio_file_name, audio_file_type):
        textStemming(audio_file_name, audio_file_type)
        print("-----------------Sentiment Analysis--------------------")
        sentiment = sentiment_calculator(
            positivewords, negativewords, stemmedtextoutput)
        print("Sentiment Analysis Finished...")
        print("-------------------------------------------------")
        return sentiment
except Exception as e:
    print("Audio File Error!")
    print(e)


# if __name__ == "__main__":
#     print("WELCOME TO AUDIO STEMMER")
#     print("<><><><><><>><><><><><><><><>")
#     main()
