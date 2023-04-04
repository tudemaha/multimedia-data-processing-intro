import pandas as pd
import numpy as np
from math import log10

def create_word_list(dataset_dict):
    words = []

    for key in dataset_dict:
        for word in dataset_dict[key]:
            if word not in words:
                words.append(word)

    words.sort()
    return words

def one_hot_encoding(dataset_dict):
    words = create_word_list(dataset_dict)

    ohe_matrix = np.zeros((len(dataset_dict), len(words)), dtype=int)
    
    for i, key in enumerate(dataset_dict):
        for word in dataset_dict[key]:
            ohe_matrix[i][words.index(word)] = 1

    ohe_df = pd.DataFrame(ohe_matrix, index=[key for key in dataset_dict], columns=words)
    return ohe_df


def bag_of_words(dataset_dict):
    words = create_word_list(dataset_dict)

    bow_matrix = np.zeros((len(dataset_dict), len(words)), dtype=int)

    for i, key in enumerate(dataset_dict):
        for word in dataset_dict[key]:
            bow_matrix[i][words.index(word)] = dataset_dict[key].count(word)
    
    bow_df = pd.DataFrame(bow_matrix, index=[key for key in dataset_dict], columns=words)
    return bow_df

def tfidf(dataset_dict):
    words = create_word_list(dataset_dict)

    tfidf_matrix = np.zeros((len(dataset_dict), len(words)), dtype=float)
    ohe_df = one_hot_encoding(dataset_dict)
    bow_df = bag_of_words(dataset_dict)

    dft = dict()
    for word in words:
        for idx in dataset_dict:
            if word not in dft:
                dft[word] = ohe_df[word][idx]
            else:
                dft[word] = dft[word] + ohe_df[word][idx]

    tfidf_df = pd.DataFrame(tfidf_matrix, index=[key for key in dataset_dict], columns=words)
    for column in tfidf_df:
        for idx in dataset_dict:
            if bow_df[column][idx] != 0:
                tfidf_df[column][idx] = (1 + log10(bow_df[column][idx])) * log10(len(dataset_dict) / dft[column])
    
    return tfidf_df