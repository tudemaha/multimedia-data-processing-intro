import re

def lowercase(df):
    for i in df.index:
        df['Reviews'][i] = df['Reviews'][i].lower()

def remove_number(df):
    number_regex = re.compile('[\d+]|¾')
    for i in df.index:
        df['Reviews'][i] = number_regex.sub('', df['Reviews'][i])

def remove_symbol(df):
    symbol_regex = re.compile('[^\w\s]')
    for i in df.index:
        df['Reviews'][i] = symbol_regex.sub('', df['Reviews'][i])

def remove_alay_word(df, dictionary):
    for i in df.index:
        current_split = df['Reviews'][i].split()
        
        for j, word in enumerate(current_split):
            for key in dictionary:
                if word == key:
                    current_split[j] = dictionary[key]
        
        df['Reviews'][i] = " ".join(current_split)
