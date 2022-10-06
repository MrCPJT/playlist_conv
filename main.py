# Packages

import spotipy
import spotipy.oauth2
from youtube_search import YoutubeSearch

# Short-handing command

spotify = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())

# Setting scope and retrieving auth

scope = 'playlist-read-private'
sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(scope=scope))

# Fetching user ID

user_id = sp.current_user()["id"]

# Fetching current user's playlists

results = sp.current_user_playlists(limit=50)

# Displaying current selectable-playlists

print("User playlists: "); print('-----')
for i, item in enumerate(results['items']):
    print("%d %s" % (i, item['name']))
print('-----')
# User selects playlist-of-interest
# Prints relevant playlist information
# Fetch playlist ID

print(''); ind_inp = input("Please input playlist index to copy: ")
print(''); print("Playlist name: ", results['items'][int(ind_inp)]['name'], "Playlist ID: ", results['items'][int(ind_inp)]['id'])
playlist_id = results['items'][int(ind_inp)]['id']

print("Now fetching playlist contents... Please wait...")
print("User id: ", user_id)

# Fetch playlist-contents
# List song titles for later youtube-searching

to_search =[]
playlist_results = sp.user_playlist_tracks(user_id,playlist_id)
for i in range(len(playlist_results['items'])):
    to_search.append(playlist_results['items'][i]['track']['name'] + ' ' + playlist_results['items'][i]['track']['artists'][0]['name'])

print(''); print("Playlist content fetching complete! Thanks for waiting")

# Collecting most-relevant search result URL for later adding to playlist

search_results = []
for i in to_search:
    videoSearch = YoutubeSearch(i,max_results=1).to_dict()
    search_results.append('https://www.youtube.com' + videoSearch[0]['url_suffix'])

print("URL Fetching Complete! Thanks for waiting")