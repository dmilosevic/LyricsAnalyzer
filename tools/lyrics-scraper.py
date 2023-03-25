from bs4 import BeautifulSoup
import requests
import string

artist_name = "bajaga"
artist_page = "https://tekstovi.net/2,150,0.html" # Bajaga

def save_artist_songs(artist_page):
    resp = requests.get(artist_page)
    soup = BeautifulSoup(resp.text, "html.parser")
    all_songs_p = soup.find_all("p", class_="artLyrList")

    for song in all_songs_p:
        a_tag = song.find("a")
        href = a_tag["href"]
        song_name = a_tag.text

        save_individual_song(href, song_name)
        #print(song_name)

def save_individual_song(href, song_name):
    url = "https://tekstovi.net/" + href
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    lyrics_p = soup.find_all("p", class_="lyric")
    
    lyrics_text = " ".join([lyrics.text.strip() for lyrics in lyrics_p])

    file_name = get_file_name(song_name)
    
    with open(f"../assets/lyrics/{artist_name}/{file_name}", "w") as f:
        f.write(lyrics_text)

def get_file_name(song_name):
    file_name = song_name.translate(str.maketrans('', '', string.punctuation))
    file_name = " ".join(file_name.split())
    file_name = file_name.replace(" ", "-") + ".txt"
    return file_name

save_artist_songs(artist_page)
