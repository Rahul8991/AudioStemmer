from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import LancasterStemmer
from nltk.stem import PorterStemmer
import nltk
import os
# nltk.download()


class word_stemmer:

    def stemSentence(self, sentence="Pythoners are very intelligent and work very pythonly and now they are pythoning their way to success."):
        porter = PorterStemmer()
        token_words = word_tokenize(sentence)
        stem_sentence = []
        for word in token_words:
            stem_sentence.append(porter.stem(word))
            stem_sentence.append(" ")
        return ''.join(stem_sentence)


save_path = r'C:/Users/Rahul/Desktop/NLP/audiototext/output'
name = 'unstemmedtextoutput'
unstemmedtextoutput = os.path.join(save_path, name)

DIR = r'C:/Users/Rahul/Desktop/NLP/stemming/output'
filname = 'stemmedtextoutput'
stemmedtextoutput = os.path.join(DIR, filname)

line_list = []

with open(unstemmedtextoutput, 'r') as file:
    for lines in enumerate(file):
        line_list.append(lines[1].strip('\n'))
print(line_list)
for sentence in line_list:
    ws1 = word_stemmer()
    x = ws1.stemSentence(sentence)
    with open(stemmedtextoutput, 'a') as f:
        f.write(f"{x}\n")
        f.close()
