
import speech_recognition as sr
import os

class audio_to_text:

    r = sr.Recognizer()
    
    save_path = 'C:/Users/Rahul/Desktop/NLP/audiototext/output'
    name = 'unstemmedtextoutput'
    completeName = os.path.join(save_path, name)

    def text_creator(self, audio):
        with sr.AudioFile(audio) as source:
            audio_text = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio_data=audio_text)
                print('Converting...')
            except:
                print('Sorry.. try again...')

        with open(self.completeName, 'a') as file1:
            file1.write(f"{text}\n")
            file1.close()
        