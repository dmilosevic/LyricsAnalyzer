from collections import Counter

def analyze(tokens):
    return { 
        "word_count": len(tokens),
        "unique_word_count": len(set(tokens)), 
        "word_frequency": Counter(tokens)
    }