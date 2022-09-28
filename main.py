
# Packages

import spotipy
import spotipy.oauth2

# Short-handing command

spotify = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())

# Setting scope and retrieving auth

scope = 'playlist-read-private'
sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(scope=scope))

user_id = sp.current_user()["id"]
print(user_id)

results = sp.current_user_playlists(limit=50)

print("User playlists: ")
for i, item in enumerate(results['items']):
    print("%d %s" % (i, item['name']))

ind_inp = input("Please input playlist index to copy")

print("Playlist name: ", results['items'][int(ind_inp)]['name'], "Playlist ID: ", results['items'][int(ind_inp)]['id'])

playlist_id = results['items'][int(ind_inp)]['id']

playlist_results = sp.user_playlist_tracks(user_id,playlist_id)
for i in range(len(playlist_results['items'])):
    print("Name: ", playlist_results['items'][i]['track']['name'],"Artist: ", playlist_results['items'][i]['track']['artists'][0]['name'])



