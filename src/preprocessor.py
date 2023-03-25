import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_new_lines(text):
    return text.replace("\n", " ")

def remove_extra_spaces(text):
    return " ".join(text.split())

def remove_words_where(text, length):
    words_to_remove = ['ref', 'sam', 'koj'] # TODO: define a proper stopwords list 
    return " ".join([word for word in text.split() if len(word) >= length and word not in words_to_remove])

def to_lower(text):
    return text.lower()

def preprocess_text(text):
    
    text = remove_new_lines(text)
    text = remove_punctuation(text)
    text = remove_extra_spaces(text)
    text = to_lower(text)
    text = remove_words_where(text, 3)
    return text