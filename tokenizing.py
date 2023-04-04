from nltk.tokenize import word_tokenize

def tokenizing(df):
    dataset_dict = {}
    for i in df.index:
        dataset_dict[i] = word_tokenize(df['Reviews'][i])
    
    return dataset_dict