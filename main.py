from unittest import result
import spotipy
import spotipy.oauth2
# import os

# print(os.getenv('SPOTIPY_CLIENT_ID'))
# print(os.getenv('SPOTIPY_CLIENT_SECRET'))
# print(os.getenv('SPOTIPY_REDIRECT_URI'))

spotify = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())
scope = 'user-top-read'
sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(scope=scope))

ranges = ['short_term', 'medium_term', 'long_term']

for sp_range in ranges:
    print("range: ", range)
    results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
    for i, item in enumerate(results['items']):
        # print(i, item)
        print(i, item['name'], '//', item['artists'][0]['name'], '//', item['artists'][0]['type'], '//', item['type'])
    print()
