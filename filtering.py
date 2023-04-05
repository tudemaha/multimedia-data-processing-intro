# import stopwords library from nltk and Sastrawi
from nltk.corpus import stopwords
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# generate Indonesian stopwords set from nltk
nltk_stopwords = set(stopwords.words('indonesian'))

# create StopWordRemoverFactory object from Sastrawi
factory = StopWordRemoverFactory()
# generate Indonesian stopwords from Sastrawi
sastrawi_stopwords = factory.get_stop_words()

# function to remove stopwords using nltk, Sastrawi, and own stopword list
def remove_stopwords(dataset_dict, stopwords = []):
    # for every document in dataset
    for key in dataset_dict:
        # prepare new list to store the non stopwords
        new_token = []
        # for every word in document
        for word in dataset_dict[key]:
            # if the current word not in nltk_stopwords and not in sastrawi_stopwords and not in own stopwords
            if (word not in nltk_stopwords) and (word not in sastrawi_stopwords) and (word not in stopwords):
                # append the word into new_token list
                new_token.append(word)
        # replace the words of document with non stopwords
        dataset_dict[key] = new_token