from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
website = response.text

# scrape the website for the top 100 songs and make a list of them
soup = BeautifulSoup(website, "html.parser")
songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
top_100_songs = [song.getText() for song in songs]

# set up the API for Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="****36778ad64719bc1ac8f83d6f****",
        client_secret="****2aa7290144ae83fb55975284****",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
song_uris = []
# find the top 100 songs on Spotify
for song in top_100_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# create the playlist on Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
