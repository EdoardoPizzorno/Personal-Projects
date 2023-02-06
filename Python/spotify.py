import requests

current_track_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
best_tracks_URL = 'https://api.spotify.com/v1/me/top/tracks'
best_artists_URL = 'https://api.spotify.com/v1/me/top/artists'

current_track_token = 'BQADX99mb45VqayXy0erWpd1U_BU4S0fe_gli4oZcAQBouG2jWaYAUPKmUt3KikToXOJFQjLWbZw-Y7NYP0UgE0xYW9NR5TaiKTZ0zy7NGErbWRO4bmot48Z1McaUvEIPnNWkdzqEa2LOS96B63UWD16x3vWheNOTnFD4NjuudokqQXkCMHEWh4EHBdSUgTU6tmV'
best_tracks_token = 'BQBIUMfiUeDXwssZbUrbJQ56z0UZ-dqmSq1DrnaNusL7qIgA_-yu8SWfXz0EYcLjx0K3Jdldq9rk847zM87wKcegYgklzAinNcfDafyY2pP58-VhhDpUBFygvY34nFjMcCb7Z703zBSm28GdciKY1wmrG7t7ImfYx07hg_N4sxLn5C2o5SaXK4UPGj3pbkLYxeb0KyU'
best_artists_token = 'BQD8elHR1flZ5fKPiQKVIwyeEQJ9ZEcpmN5M-gozLGhTrFWY5XzfyREZwk6tZ4VqQ7Lo8iHLRULA2FSIzI9qJhvhM9J9DDqtxt8P94kxzDswvY4iGyyZaBo4sJfsIsjaZqXTigjkQ2z38j1fxxnm8Vh_8PLilxywuMZDfFUSOTlHISRj4DM0WPvrsRsR3fZfpJ_RCbw'

def get_best_tracks():
    best_tracks = []

    response = requests.get(best_tracks_URL, headers={
        "Authorization" : f"Bearer {best_tracks_token}"
    })
    json_resp = response.json()

    for i in range(len(json_resp)):
        #Getting artists
        artists = [artist for artist in json_resp['items'][i]['artists']]
        artist_names = ', '.join([artist['name'] for artist in artists])

        best_tracks.append({
            "name" : json_resp['items'][i]['name'],
            "artists" : artist_names,
        })

    return best_tracks

def get_best_artists():
    best_artists = []

    response = requests.get(best_artists_URL, headers={
        "Authorization" : f"Bearer {best_artists_token}"
    })
    json_resp = response.json()

    for i in range(len(json_resp)):
        genre_names = ""
        #Getting genres
        for j in range(len(json_resp['items'][i]['genres'])):
            genre_names += json_resp['items'][i]['genres'][j]

        best_artists.append({
            "name" : json_resp['items'][i]['name'],
            "genres" : genre_names
        })

    return best_artists

def get_current_track():
    response = requests.get(current_track_URL,headers={
            "Authorization": f"Bearer {current_track_token}"
        }
    )
    json_resp = response.json()

    #Getting artists
    artists = [artist for artist in json_resp['item']['artists']]
    artist_names = ', '.join([artist['name'] for artist in artists])

    current_track_info = {
        "id" : json_resp['item']['id'],
    	"name": json_resp['item']['name'],
    	"artists": artist_names
    }

    return current_track_info

def printLists(list, field):
    i = 0
    str = "ARTISTS"
    if field == 'genres':
        str = "GENRES"

    for i in range(len(list)):
        print(f"{(i + 1)}) NAME: {list[i]['name']}\n{str}: {list[i][field]}\n")

def main():
    current_track_id = None
    best_tracks = []
    best_artists = []
    current_track_id = {}

    i = -1 #initially best_tracks' length is 0
    while i != len(best_tracks):
        best_tracks = get_best_tracks() #SHORT_TERM (4 weeks)
        i += 1
    print("\n\n\nBEST TRACKS: ")
    printLists(best_tracks, 'artists')

    i = -1 #initially best_artists' length is 0
    while i != len(best_tracks):
        best_artists = get_best_artists() #SHORT_TERM (4 weeks)
        i += 1
    print("\n\nBEST ARTISTS: ")
    printLists(best_artists, 'genres')

    current_track_info = get_current_track()
    if current_track_info['id'] != current_track_id:
        print(f"\n\nCURRENT TRACK: \nNAME: {current_track_info['name']}\nARTISTS: {current_track_info['artists']}\n")

        current_track_id = current_track_info['id']

main()