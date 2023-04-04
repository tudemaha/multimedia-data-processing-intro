from nltk.stem import PorterStemmer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

ps = PorterStemmer()

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def nltk_stemming(dataset_dict):
    for key in dataset_dict:
        after_stemming = []
        for word in dataset_dict[key]:
            stemming = ps.stem(word)
            if stemming not in after_stemming:
                after_stemming.append(stemming)
        
        dataset_dict[key] = after_stemming

def sastrawi_stemming(dataset_dict):
    for key in dataset_dict:
        dataset_dict[key] = [stemmer.stem(word) for word in dataset_dict[key]]