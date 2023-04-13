import string
import json

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_new_lines(text):
    return text.replace("\n", " ")

def remove_extra_spaces(text):
    return " ".join(text.split())

def remove_short_words(text, min_length):     
    return " ".join([word for word in text.split() if len(word) >= min_length])

def remove_stopwords(tokens):
    stopwords = None
    with open("../assets/stopwords.json", "r") as file:
        stopwords = json.load(file)

    return [token for token in tokens if token not in stopwords]

def preprocess(text): 
    text = remove_new_lines(text)
    text = remove_punctuation(text)
    text = remove_extra_spaces(text)
    text = text.lower()
    text = remove_short_words(text, 3)
    return text