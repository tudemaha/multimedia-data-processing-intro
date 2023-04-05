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
        # prepare empty list to store the stemmed words
        after_stemming = []
        # iterate words of current document
        for word in dataset_dict[key]:
            # stem the current word
            stemming = ps.stem(word)
            # if the stemmed word not in after_stemming list
            if stemming not in after_stemming:
                # append it into after_stemming list
                after_stemming.append(stemming)
        
        # replace the current document with stemmed words
        dataset_dict[key] = after_stemming

# function to stem Indonesian words using Sastrawi
def sastrawi_stemming(dataset_dict):
    # iterate every element in dictionary
    for key in dataset_dict:
        # replace the current document with stemmed words
        # by stemming every word using Sastrawi stemmer
        dataset_dict[key] = [stemmer.stem(word) for word in dataset_dict[key]]