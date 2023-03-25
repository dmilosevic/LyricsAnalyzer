from collections import Counter

def analyze(tokens):
    """Analyze text for word count, unique word count and word frequency.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary with the results of the analysis.
    """
    return { 
        "word_count": len(tokens),
        "unique_word_count": len(set(tokens)), 
        "word_frequency": Counter(tokens)
    }