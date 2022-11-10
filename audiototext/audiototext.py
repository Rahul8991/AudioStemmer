
import speech_recognition as sr
import os
import sys
import json


class audio_to_text:

    r = sr.Recognizer()

    # save_path = 'C:/Users/{userName}/Desktop/NLP/audiototext/output'
    # name = 'unstemmedtextoutput'
    # completeName = os.path.join(save_path, name)

    def text_creator(self, audio, unstemmedtextoutput):
        print("Audio to Text Conversion Started...")
        with sr.AudioFile(audio) as source:
            audio_text = self.r.record(source)
            try:
                print('Converting...')
                text = self.r.recognize_google(audio_data=audio_text)
                print(text)
                print("returning text to main...")
            except:
                print('Sorry.. something happened...')

        print("Opening File...")
        with open(unstemmedtextoutput, 'a') as file1:
            answer = input("Do you want to retain old data? (Yes/No) ")
            if answer.lower() == 'yes':
                print("Writing to File Started...")
                file1.write(f"{text}\n")
                print("Closing File(Unstemmed)...")
                file1.close()
            else:
                print("Erasing...")
                file1.truncate(0)
                print("Writing to File Started...")
                file1.write(f"{text}\n")
                print("Closing File(Unstemmed)...")
                file1.close()
        return text
