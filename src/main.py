import os
import glob
from preprocessor import preprocess, remove_stopwords
from tokenizer import tokenize, lemmatize, lookup
from analyzer import analyze
from wordcloud_generator import generate_wordcloud
import json

def concat_all_lyrics(artist_name):
    directory = f"../assets/lyrics/{artist_name}"
    files = glob.glob(os.path.join(directory, "*.txt"))

    result = ""
    for file in files:
        with open(file, "r", encoding="latin-1") as f:
            result += f.read() + " "
    return result

def save_result(result, artist_name):
    result["word_frequency"] = {k: v for k, v in sorted(result["word_frequency"].items(), key=lambda item: item[1], reverse=True)}
    with open(f"../assets/results/{artist_name}.json", "w") as f:
        json.dump(result, f, indent=4)

def main(): 
    artist_name = "sinan"
    input_text = concat_all_lyrics(artist_name)
    
    input_text = preprocess(input_text)
    tokens = tokenize(input_text)
    tokens = remove_stopwords(tokens)

    matches, no_matches = lookup(tokens)
    matches.extend(lemmatize(no_matches))
    
    result = analyze(matches)
    save_result(result, artist_name)
    generate_wordcloud(artist_name)

if __name__ == "__main__":
    main()
    