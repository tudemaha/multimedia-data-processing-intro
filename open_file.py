# import pandas
import pandas as pd

# read excel dataset function
def read_excel(filename, start, end):
    # open the specific excel file and use No and Reviews columns
    data = pd.read_excel(filename, usecols=['No', 'Reviews'])
    # use the No column as index for dataframe
    data = data.set_index('No')
    
    # return the selected range of dataset dataframe
    return data.iloc[start-1:end]

# function to read own dictionary to remove alay words
def read_dictionary(filename):
    # prepare an empty dictionary
    alay_dictionary = {}

    # open the txt alay dictionary file, read, and close
    alay = open(filename, 'r')
    alay_list = alay.readlines()
    alay.close()
    
    # for every line of dictionary
    for data in alay_list:
        # split by ': ' character
        after_split = data.split(': ')
        # strip the whitespace in value
        after_split[1] = after_split[1].strip()
        # add the key-value pair to dictionary
        alay_dictionary[after_split[0]] = after_split[1]

    # return the dictionary of alay words
    return alay_dictionary

# function to read own stopwords
def read_stopwords(filename):
    # prepare empty list
    stopwords = []

    # open, read, and close the own stopword file
    stopword = open(filename, 'r')
    stopword_list = stopword.readlines()
    stopword.close()

    # for every stopwords
    for data in stopword_list:
        # strip the whitespace
        data = data.strip()
        # append it to stopwords list
        stopwords.append(data)
    
    # return the stopwords
    return stopwords