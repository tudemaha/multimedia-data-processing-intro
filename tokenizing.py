# import word_tokenize from nltk library
from nltk.tokenize import word_tokenize

# function to tokenizing the document in dataset
def tokenizing(df):
    # prepare empty dictionary
    dataset_dict = {}

    # iterate the dataset dataframe
    for i in df.index:
        # add the current index as key to the dictionary
        # and the tokenized words as value to the dictionary
        dataset_dict[i] = word_tokenize(df['Reviews'][i])
    
    # return the tokenized words from the documents
    return dataset_dict