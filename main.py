from unittest import result
import spotipy
import spotipy.oauth2
# import os

# print(os.getenv('SPOTIPY_CLIENT_ID'))
# print(os.getenv('SPOTIPY_CLIENT_SECRET'))
# print(os.getenv('SPOTIPY_REDIRECT_URI'))

spotify = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())
scope = 'playlist-read-private'
sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(scope=scope))
user = sp.user('connor.tynan')
results = sp.current_user_playlists(limit=50)
for i, item in enumerate(results['items']):
    print("%d %s" % (i, item['name']))
#     print(i, j)


# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

