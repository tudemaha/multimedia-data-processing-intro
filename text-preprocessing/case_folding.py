# import the regex library
import re

# function to lowercase the sentence from dataset
def lowercase(df):
    # for every dataset in dataframe
    for i in df.index:
        # convert them into lowercase
        df['Reviews'][i] = df['Reviews'][i].lower()

# function to remove number from the dataset
def remove_number(df):
    # prepare regex to remove numbers
    number_regex = re.compile('[\d+]|¾')
    # remove the number from every document in dataframe
    for i in df.index:
        df['Reviews'][i] = number_regex.sub('', df['Reviews'][i])

# function to remove symbols and emoticons
def remove_symbol(df):
    # prepare the regex to remove symbols and emoticons
    symbol_regex = re.compile('[^\w\s]')
    # remove the symbols and emoticons from every document in dataframe
    for i in df.index:
        df['Reviews'][i] = symbol_regex.sub('', df['Reviews'][i])

# remove alay word using alay words dictionary
def remove_alay_word(df, dictionary):
    # split every document in dataframe into list words
    for i in df.index:
        current_split = df['Reviews'][i].split()
        
        # enumerate the words that have been splitted
        for j, word in enumerate(current_split):
            # enumerate the key of the alay words
            for key in dictionary:
                # if the current word from document equal with the key
                if word == key:
                    # replace the alay word with the right word from own alay words dictionary
                    current_split[j] = dictionary[key]
        
        # join back the list of words into sentence (document)
        df['Reviews'][i] = " ".join(current_split)