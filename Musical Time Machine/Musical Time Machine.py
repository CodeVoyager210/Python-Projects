from math import expm1

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
APP_CLIENT_ID = 'dba14b5ffe464cdc9d47c0aa74cd4104'
APP_CLIENT_SECRET = '00733791696a4b8da97d8baadc434917'
APP_REDIRECT_URI = 'https://hellospotnotblock.com'
USER_ID = '9c31fudodpk8n1ebiv7ip4qft'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=APP_CLIENT_ID,client_secret=APP_CLIENT_SECRET,redirect_uri=APP_REDIRECT_URI,scope='playlist-modify-public'))
year_music = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
url = f'https://billboard.com/charts/hot-100/{year_music}/'
response = requests.get(url=url).text
soup = BeautifulSoup(response,'html.parser')
song_names = [x.getText().strip() for x in soup.select('li ul li h3')]
song_spotify = []
for songs in song_names:
    result = sp.search(q=f"track:{songs} year:{year_music[:4]}", type="track")
    try:
        uri = result['tracks']['items'][0]['uri']
        song_spotify.append(uri)
    except IndexError:
        print(f'{songs} not found in spotify')
create_playlist = sp.user_playlist_create(user=USER_ID,name=f'Top 100 Songs Of {year_music[:4]}')
add_tracks = sp.playlist_add_items(playlist_id=create_playlist['id'],items=song_spotify,position=None)




