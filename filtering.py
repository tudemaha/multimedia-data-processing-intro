from nltk.corpus import stopwords
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

nltk_stopwords = set(stopwords.words('indonesian'))

factory = StopWordRemoverFactory()
sastrawi_stopwords = factory.get_stop_words()

def remove_stopwords(dataset_dict, stopwords = []):
    for key in dataset_dict:
        new_token = []
        for word in dataset_dict[key]:
            if (word not in nltk_stopwords) and (word not in sastrawi_stopwords) and (word not in stopwords):
                new_token.append(word)
        dataset_dict[key] = new_token