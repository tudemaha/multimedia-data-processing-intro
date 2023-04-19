# import stemmer libraries from nltk and Sastrawi
from nltk.stem import PorterStemmer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create PorterStemmer object
ps = PorterStemmer()

# create StemmerFatory object
factory = StemmerFactory()
# create stemmer from sastrawi library
stemmer = factory.create_stemmer()

# function to stem english words
def nltk_stemming(dataset_dict):
    # iterate every element in dictionary
    for key in dataset_dict:
        # replace the current document with stemmed words
        # by stemming every word using nltk stemmer
        dataset_dict[key] = [ps.stem(word) for word in dataset_dict[key]]

# function to stem Indonesian words using Sastrawi
def sastrawi_stemming(dataset_dict):
    # iterate every element in dictionary
    for key in dataset_dict:
        # replace the current document with stemmed words
        # by stemming every word using Sastrawi stemmer
        dataset_dict[key] = [stemmer.stem(word) for word in dataset_dict[key]]