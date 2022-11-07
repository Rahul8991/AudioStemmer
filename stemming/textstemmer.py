from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import LancasterStemmer
from nltk.stem import PorterStemmer
import nltk
import os
import json
# nltk.download()


class word_stemmer:
    # def __init__(self,sentence):
    #     self.sentence=sentence
    def stemSentence(self, sentence="Pythoners are very intelligent and work very pythonly and now they are pythoning their way to success."):
        porter = PorterStemmer()
        token_words = word_tokenize(sentence)
        stem_sentence = []
        for word in token_words:
            stem_sentence.append(porter.stem(word))
            stem_sentence.append(" ")
        return ''.join(stem_sentence)


# save_path = r'C:/Users/{userName}/Desktop/NLP/audiototext/output'
# name = 'unstemmedtextoutput'
# unstemmedtextoutput = os.path.join(save_path, name)

# DIR = r'C:/Users/{userName}/Desktop/NLP/stemming/output'
# filname = 'stemmedtextoutput'
# stemmedtextoutput = os.path.join(DIR, filname)
def stemIt(unstemmedtextoutput, stemmedtextoutput):
    print("Stemming Process Started...")
    line_list = []
    ws1 = word_stemmer()

    print("Reading from Unstemmed text file...")
    with open(unstemmedtextoutput, 'r') as file:
        for lines in enumerate(file):
            line_list.append(lines[1].strip('\n'))

    answer = input("Do you want to retain old data? (Yes/No) ")
    if answer.lower() == 'yes':
        print("Writing To Stemmed File...")
        for sentence in line_list:
            x = ws1.stemSentence(sentence)
            with open(stemmedtextoutput, 'a') as f:
                f.write(f"{x}\n")
            return x
    else:
        print("Erasing and Writing To Stemmed File...")
        for sentence in line_list:
            x = ws1.stemSentence(sentence)
            with open(stemmedtextoutput, 'a') as f:
                f.truncate(0)
                f.write(f"{x}\n")
            return x

    file.close()
    print("Closing File(Unstemmed)")
    f.close()
    print("Closing File(Stemmed)")
