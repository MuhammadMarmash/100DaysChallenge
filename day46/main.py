import requests
from bs4 import BeautifulSoup
import spotipy

sp = spotipy.Spotify(
    auth_manager=spotipy.oauth2.SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="cc945339b3124b0491c9678d8329c49f",
        client_secret="ad79e194adc64abf83215322a74a5d37",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-00: ")
website = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
website.raise_for_status()
soup = BeautifulSoup(website.text, "html.parser")
titles = soup.select("ul li #title-of-a-story")
titles = [title.string.strip() for title in titles]
song_uris = []
year = date.split("-")[0]
for title in titles:
    result = sp.search(q=f"track:{title} year:{year}", type="track")
    try:

        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
