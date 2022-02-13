import spotipy
from spotipy.oauth2 import SpotifyOAuth


def show_tracks(results):
    for item in results['items']:
        track = item['track']
        print("%32.32s %s" % (track['artists'][0]['name'], track['name']))


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='0aa505304fb3415a9b52df7ab67db1c7',
    client_secret='afe4be1035bc4248a39c43bd9e4079f7',
    scope='user-library-read',
    redirect_uri='http://0.0.0.0:7555/'
))

results = sp.current_user_saved_tracks(limit=50)
show_tracks(results)

while results['next']:
    results = sp.next(results)
    show_tracks(results)
