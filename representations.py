# import necessary libraries
import pandas as pd
import numpy as np
from math import log10

# function to create list of all words of all documents
def create_word_list(dataset_dict):
    # prepare empty list to store the words
    words = []

    # iterate every document in dataset
    for key in dataset_dict:
        # iterate every word in current document
        for word in dataset_dict[key]:
            # if the word not in words list append it to list
            if word not in words:
                words.append(word)

    # sort the words ascending
    words.sort()
    # return the words list
    return words

# create one-hot encoding representation
def one_hot_encoding(dataset_dict):
    # create the words list from dataset
    words = create_word_list(dataset_dict)

    # prepare zero matrix for ohe representation
    ohe_matrix = np.zeros((len(dataset_dict), len(words)), dtype=int)
    
    # iterate and enumerate dictionary of dataset
    for i, key in enumerate(dataset_dict):
        # iterate every word in current document
        for word in dataset_dict[key]:
            # set ohe_matrix in current document's index row and current word's index to 1
            ohe_matrix[i][words.index(word)] = 1

    # create dataframe from ohe_matrix
    ohe_df = pd.DataFrame(ohe_matrix, index=[key for key in dataset_dict], columns=words)
    # return the ohe dataframe
    return ohe_df


# create bag-of-words representation
def bag_of_words(dataset_dict):
    # create the words list from dataset
    words = create_word_list(dataset_dict)

    # prepare zero matrix for bow representation
    bow_matrix = np.zeros((len(dataset_dict), len(words)), dtype=int)

    # iterate and enumerate dictionary of dataset
    for i, key in enumerate(dataset_dict):
        for word in dataset_dict[key]:
            # set ohe_matrix in current document's index row and current word's index
            # with the number of current word appears in the current document
            bow_matrix[i][words.index(word)] = dataset_dict[key].count(word)
    
    # create dataframe from bow_matrix
    bow_df = pd.DataFrame(bow_matrix, index=[key for key in dataset_dict], columns=words)
    # return the bow dataframe
    return bow_df

# create TF-IDF representation
def tfidf(dataset_dict):
    # create the words list from dataset
    words = create_word_list(dataset_dict)

    # prepare zero matrix for TF-IDF representation
    tfidf_matrix = np.zeros((len(dataset_dict), len(words)), dtype=float)
    # make ohe representation from current dataset
    ohe_df = one_hot_encoding(dataset_dict)
    # make bow representatino from current dataset
    bow_df = bag_of_words(dataset_dict)

    # create empty dictionary to store words list (key) and the number of document they appear (key)
    dft = dict()

    # iterate words list
    for word in words:
        # iterate the dataset dictionary
        for idx in dataset_dict:
            # if the word not in dft, add it into dft as key
            # and the value of ohe_df[word][idx] as value
            if word not in dft:
                dft[word] = ohe_df[word][idx]
            # else, do addition with the value before
            else:
                dft[word] = dft[word] + ohe_df[word][idx]

    # create dataframe from zero TF-IDF matrix
    tfidf_df = pd.DataFrame(tfidf_matrix, index=[key for key in dataset_dict], columns=words)
    # iterate every column (words) in tfidf_df
    for column in tfidf_df:
        # iterate the key from dataset dictionary
        for idx in dataset_dict:
            # if the value in bow_df[column][idx] not 0
            if bow_df[column][idx] != 0:
                # update the tfidf_df in current cell with TF-IDF value 
                tfidf_df[column][idx] = (1 + log10(bow_df[column][idx])) * log10(len(dataset_dict) / dft[column])

    # return the TF-IDF dataframe
    return tfidf_df