def sentiment_calculator(positivewordsfile, negativewordsfile, stemmedtextoutputfile):
    print("Process Started...")
    positive_words = []
    with open(positivewordsfile, 'r') as f:
        for lines in enumerate(f):
            positive_words.append(lines[1].strip('\n'))
    # print(positive_words)

    negative_words = []
    with open(negativewordsfile, 'r') as f:
        for lines in enumerate(f):
            negative_words.append(lines[1].strip('\n'))
    # print(negative_words)

    line_list = []
    with open(stemmedtextoutputfile, 'r') as f:
        for lines in enumerate(f):
            line_list.append(lines[1].strip('\n'))
    # print(line_list)

    word_list = []
    for sentence in line_list:
        # print(sentence)
        # print(type(sentence))
        # print(len(sentence))
        # print(sentence.split(' '))
        word_list = [i for i in sentence.split(' ') if i]
        # print(word_list)

    pscore = 0
    for word in word_list:
        for pword in positive_words:
            if(word == pword):
                pscore += 1
    # print(pscore)
    ppercent = int(pscore/len(word_list)*100)
    print(f"{ppercent} %")

    nscore = 0
    for word in word_list:
        for nword in negative_words:
            if(word == nword):
                nscore += 1
    # print(nscore)
    npercent = int(nscore/len(word_list)*100)
    print(f"{npercent} %")

    if(ppercent > npercent):
        print("Positive Audio File")
    else:
        print("Negative Audio File")
