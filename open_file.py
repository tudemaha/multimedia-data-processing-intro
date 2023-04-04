import pandas as pd

def read_excel(filename, start, end):
    data = pd.read_excel(filename, usecols=['No', 'Reviews'])
    data = data.set_index('No')
    
    return data.iloc[[i for i in range(start - 1, end)]]

def read_dictionary(filename):
    alay_dictionary = {}

    alay = open(filename, 'r')
    alay_list = alay.readlines()
    alay.close()
    
    for data in alay_list:
        after_split = data.split(': ')
        after_split[1] = after_split[1].strip()
        alay_dictionary[after_split[0]] = after_split[1]

    return alay_dictionary

def read_stopwords(filename):
    stopwords = []

    stopword = open(filename, 'r')
    stopword_list = stopword.readlines()
    stopword.close()

    for data in stopword_list:
        data = data.strip()
        stopwords.append(data)
    
    return stopwords