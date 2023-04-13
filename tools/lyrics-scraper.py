from bs4 import BeautifulSoup
import requests
import string
import os

artist_name = "sinan"
artist_page = "https://tekstovi.net/2,1,0.html"

def save_artist_songs(artist_page):
    print("Downloading songs...")
    resp = requests.get(artist_page)
    soup = BeautifulSoup(resp.text, "html.parser")
    all_songs_p = soup.find_all("p", class_="artLyrList")

    for song in all_songs_p:
        a_tag = song.find("a")
        href = a_tag["href"]
        song_name = a_tag.text

        save_individual_song(href, song_name)

    print("Done!")

def save_individual_song(href, song_name):
    url = "https://tekstovi.net/" + href
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    lyrics_p = soup.find_all("p", class_="lyric")
    
    lyrics_text = " ".join([lyrics.text.strip() for lyrics in lyrics_p])

    file_name = get_file_name(song_name)
    #beware of ../ path, it appears to be relative to the file where the script is RUN FROM
    file_path = f"../assets/lyrics/{artist_name}/{file_name}"  
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(lyrics_text)

def get_file_name(song_name):
    file_name = song_name.translate(str.maketrans('', '', string.punctuation))
    file_name = " ".join(file_name.split())
    file_name = file_name.replace(" ", "-") + ".txt"
    return file_name

save_artist_songs(artist_page)