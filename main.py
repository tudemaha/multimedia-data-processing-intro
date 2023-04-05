# import modules
import open_file
import case_folding
import tokenizing
import filtering
import stemming
import representations
import printing

# read the dataset, alay dictionary, and own stopword files
df = open_file.read_excel('dataset A.xlsx', 101, 110)
alay_dict = open_file.read_dictionary('alay_dictionary.txt')
stopwords = open_file.read_stopwords('own_stopword.txt')

# original dataset
print('Original dataset:\n', df)

# case folding -> lowercase
case_folding.lowercase(df)
print('\nLowercase:\n', df)

# case folding -> remove numbers
case_folding.remove_number(df)
print('\nNumber removal:\n', df)

#case folding -> remove symbols and emoticons
case_folding.remove_symbol(df)
print('\nRemove symbols and emoticons:\n', df)

# case folding -> remove alay words
case_folding.remove_alay_word(df, alay_dict)
print('\nAlay words removal:\n', df)

# tokenizing dataset
dataset_tokenize = tokenizing.tokenizing(df)
print('\nTokenizing:')
printing.print_dictionary(dataset_tokenize)

# filter stopwords using nltk, sastrawi, and own stopwords
filtering.remove_stopwords(dataset_tokenize, stopwords)
print('\nStopwords removal:')
printing.print_dictionary(dataset_tokenize)

# nltk stemming
# stemming.nltk_stemming(dataset_tokenize)
stemming.sastrawi_stemming(dataset_tokenize)
print('\nSastrawi stemming:')
printing.print_dictionary(dataset_tokenize)

# representation -> one hot encoding (transposed dataframe)
ohe_df = representations.one_hot_encoding(dataset_tokenize)
print('\n\nOne Hot Encoding:\n', ohe_df.T)
# representation -> bag of words (transposed dataframe)
bow_df = representations.bag_of_words(dataset_tokenize)
print('\nBag of Words:\n', bow_df.T)
# representation -> TDIDF (transposed dataframe)
tfidf_df = representations.tfidf(dataset_tokenize)
print('\nTF-IDF:\n', tfidf_df.T)