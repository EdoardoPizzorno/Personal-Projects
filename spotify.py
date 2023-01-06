import requests

current_track_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
best_tracks_URL = 'https://api.spotify.com/v1/me/top/tracks'
best_artists_URL = 'https://api.spotify.com/v1/me/top/artists'

current_track_token = 'BQA4N3Kh-3bvuRyXsGhAYfZxcWN46pUvSK0pROvjZ6C5KBc8GGcyZGWW-n90A_2A5Bj4RgA52lK3YfkOzcsdkmNFY9Q7W5LTtmlzWb4GSmF7V7Diwkxr5AmRsu9op97BRRZGticAFbSBFKOHNQAEpNCCZNpJjqsRozgt07XX4BXelU6T8H9FDX8oNlLZb6OHfKYY'
best_tracks_token = 'BQBVS2gsJheo5Kg97qe5xrF8-lf823XzzC8_aGc9ZFXP_tE97JX8m62dhV2Q8On8Q8xzM4epg8YfK6AGQhVcRIxtGNlj6Jy2H5sGZ-Z_7xS8xkuWiqeo3VsmEUu8Lxt1JGBDGscjvLgG64bVcnTvEDenlrpsNCT73rB5fAa9YvcQ8DWMRsTM5lxOVmYbRyWOHydRVXw'
best_artists_token = 'BQA8Z039782xMQihrhcVdgtbR3cETHK5npbBx2aouzQbGUSGOcglai6DJL_tX-D-agRZbDsHtJAEw8umc_Kkz9QHxGrUgT-49GKdqDMawkG8jyCdLkwAyjPHBce1iReisHsGxIyAJoov7KjsJOnRTaIngBKB6iMRYGFNzPmQbC-MiY2yp06Tg6yXesNl0Zji8oHW4ZI'

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