# Python script 
# File: useful_functions.py
# Author: Christian Brandstätter 
# Contact: bran.chri@gmail.com
# Date: 22.01.2020
# Copyright (C) 2020
# Description: functions created by Benjamin


# Defining Function that cleans a string
def cleanText(text):
    '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# Defining a funtion that cleans the Text of Stopwords, which are not relevant to us in this context.
def cleanStopWords(text):
    #Defining the english stop words:
    stopWords = set(stopwords.words('english'))
    textSplitted = text.split(' ')
    cleanedText = ''
    for element in textSplitted:
        if element not in stopWords:
            cleanedText = cleanedText + ' ' + element
    return cleanedText

# Defining Function to create a wordcloud
def wordCloudCreation (text, title='', width= 500, height = 400):
    text_string = ''
    for element in text:
        text_string= text_string + ' ' + element
    stop_words = set(stopwords.words('english'))
    wc = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark2",collocations=False,
               max_font_size=150, random_state=42, width=width, height=height, margin = 20)
    
    wc.generate(text_string)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis('off')
    plt.title(title+'\n')
    #plt.show()

#Defining a Function which returns the most common words in a data series.
def wholeReviewTextFromSeries(text):
    wholeReview = ''
    for element in text:
        wholeReview = wholeReview + ' ' + element
    return Counter(wholeReview.split()).most_common()
