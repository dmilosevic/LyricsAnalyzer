from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json

def generate_wordcloud(artist_name):
    with open(f"../assets/results/{artist_name}.json", "r") as f:
        data = json.load(f)
    wordcloud = WordCloud(width=800, height=800, background_color='white').generate_from_frequencies(data["word_frequency"])
    plt.figure(figsize=(8,8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(f"../assets/results/{artist_name}.png")
    plt.show()