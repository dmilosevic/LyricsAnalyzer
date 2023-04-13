from snowballstemmer import stemmer
import json
from collections import Counter
import subprocess
import os

serbian_stemmer = stemmer('serbian')

def tokenize(text):
    tokens = text.split()
    return tokens

def lookup(tokens):
    data = None
    matches = []
    no_matches = []

    with open('../assets/sr_lemma_lookup.json', 'r') as f:
        data = json.load(f)

    for token in tokens:
        if token in data.keys():
            matches.append(data[token])
        else:
            no_matches.append(token)

    return matches, no_matches

def lemmatize(tokens): 
    token_lemma_dict, not_found = get_token_lemma_dict(tokens)

    #print(f"stems not found: {Counter(not_found)}")

    matches = [token_lemma_dict[token] for token in tokens if token in token_lemma_dict.keys()]
    
    return matches

def get_token_lemma_dict(tokens): 
    data = None
    token_lemma_dict = {}
    processsed = set()
    not_found = []

    with open('../assets/uniques.json', 'r') as f:
        data = json.load(f)

    for token in tokens:
        stem = serbian_stemmer.stemWord(token)

        if stem in processsed:
            continue
        found = False
        
        for key in data.keys():
            if key.startswith(stem):
                token_lemma_dict[token] = data[key]
                found = True
                processsed.add(stem)
                break
  
        if not found:
            not_found.append(token)

    return token_lemma_dict, not_found

            

# bash alternative (get_token_lemma_dict)
# file_path = "../assets/sr_lemma_lookup.json"
#         bash_cmd = f"grep -i '\"{stem}' {file_path} | head -n 1 | cut -d':' -f2 | sed 's/[^a-zA-Z]//g'"
        
#         result = subprocess.run([bash_cmd], shell=True, stdout=subprocess.PIPE)
#         #print(result.stdout.decode('utf-8').strip())
#         output = result.stdout.decode('utf-8').strip()

#         if output != "":
#             token_lemma_dict[token] = output
#             #found = True
#             processsed.add(stem)
#         else:
#             not_found.append(token)