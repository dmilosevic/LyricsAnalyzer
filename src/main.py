import os
import glob
import preprocessor as pp
from tokenizer import tokenize
from analyzer import analyze

def load_text_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def pretty_print(result):
    print(f"Word count: {result['word_count']}")
    print(f"Unique word count: {result['unique_word_count']}")
    print("Word frequency:")
    #sort by frequency
    for word in sorted(result['word_frequency'], key=result['word_frequency'].get, reverse=True):
        print(f"\t{word}: {result['word_frequency'][word]}")

def concat_all_lyrics():
    directory = "../assets/lyrics/bajaga"
    files = glob.glob(os.path.join(directory, "*.txt"))

    #print(len(files))
    result = ""
    for file in files:
        with open(file, "r") as f:
            result += f.read() + " "
    return result

def main(): 
    input_text = concat_all_lyrics()
    result = pp.preprocess_text(input_text)
    print(result)

    tokenized_result = tokenize(result)
    result = analyze(tokenized_result)
    pretty_print(result)
    with open("../assets/results/bajaga.txt", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
    