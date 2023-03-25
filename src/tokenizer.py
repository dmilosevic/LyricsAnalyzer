from snowballstemmer import stemmer 
serbian_stemmer = stemmer('serbian')

#nltk.download('punkt') #comtrans?

def tokenize(text):
    tokens = split_into_tokens(text)
    return [serbian_stemmer.stemWord(token) for token in tokens]

# def remove_stopwords(tokens):
#     return [token for token in tokens if token not in stopwords.words('serbian')]

def split_into_tokens(text):
    return text.split()