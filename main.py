import open_file
import case_folding
import tokenizing
import filtering
import stemming
import representations

# import the dataset and alay dictionary
df = open_file.read_excel('dataset A.xlsx', 101, 110)
alay_dict = open_file.read_dictionary('alay_dictionary.txt')
stopwords = open_file.read_stopwords('own_stopword.txt')

# case folding -> lowercase
case_folding.lowercase(df)
# case folding -> remove numbers
case_folding.remove_number(df)
#case folding -> remove symbols and emoticons
case_folding.remove_symbol(df)
# case folding -> remove alay word
case_folding.remove_alay_word(df, alay_dict)

# tokenizing dataset
dataset_tokenize = tokenizing.tokenizing(df)

# filter stopwords using nltk, sastrawi, and own stopwords
filtering.remove_stopwords(dataset_tokenize, stopwords)

# nltk stemming
# stemming.nltk_stemming(dataset_tokenize)
stemming.sastrawi_stemming(dataset_tokenize)

# print the dictionary
for key in dataset_tokenize:
    print(key, dataset_tokenize[key])

# representation -> one hot encoding
ohe_df = representations.one_hot_encoding(dataset_tokenize)
print('\nOne Hot Encoding:\n', ohe_df.T)
# representation -> bag of words
bow_df = representations.bag_of_words(dataset_tokenize)
print('\nBag of Words:\n', bow_df.T)
# representation -> TDIDF
tfidf_df = representations.tfidf(dataset_tokenize)
print('\nTF-IDF:\n', tfidf_df.T)