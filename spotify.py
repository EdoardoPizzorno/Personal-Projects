import requests

current_track_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
best_tracks_URL = 'https://api.spotify.com/v1/me/top/tracks'
best_artists_URL = 'https://api.spotify.com/v1/me/top/artists'

current_track_token = 'BQB3brvdsuKosMQN0JoihQuX_NUlLdWYdgv2rmaRr4N0QZbt8VmzqmZ84whS9_YZ1D3qZlhgiA0M15Lsee9rnTX58zQzmXweZqLm89M9ADOaQUW9cWPMtc4PNpLzMAbpZzMgLFjtut5u50I-kUdbCN7p3JnsjrnysZPd1OuZCDZSPVsMXoz6RGnUEg771tmFxlc5'
best_tracks_token = 'BQBpPg8xx-NJXL2bHmx56bkwGO9ewhxT9abvwx2NXTdti7Op72467HFPdUoAQOvR1E7XtR02d0YkiPnI6s8zzJU-_fi1QtO_momfk2e8Iki_Q-6V9l7r8zdAi9ai8WTtPkxes-z1alDZ6VUjxnqOEbON4jYQvvkkXzEMHmDszt0jKpXH7-CS-GZZ2tT6PJuMEUZ5jO0'
best_artists_token = 'BQCmM29H86mlFEqfOnziDa32ujF69LXNlyYDtUWiDx0ilPyhRfBA6SuTL17MxN8dMMJjTC-auU0U03c0kyXwdWDEgbjnC7DMrEtzYfjgm8zlaLeA3tbFyt2ICYdMPUskmXt-mGJCnbBYRgbfIXHnxrQ2a2KdfjqlUmaz8zf1NDQUjUNMoxt1KA-NZxmT7GbWFwiwxa8'

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
        i += 1
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
        i += 1

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
    	"track_name": json_resp['item']['name'],
    	"artists": artist_names
    }

    return current_track_info


def main():
    current_track_id = None
    best_tracks = []
    best_artists = []
    current_track_id = {}

    i = -1 #initially best_tracks' length is 0
    while i != len(best_tracks):
        best_tracks = get_best_tracks() #SHORT_TERM (4 weeks)
        i += 1
    print(best_tracks)

    i = -1 #initially best_artists' length is 0
    while i != len(best_tracks):
        best_artists = get_best_artists() #SHORT_TERM (4 weeks)
        i += 1
    print(best_artists)

    current_track_info = get_current_track()
    if current_track_info['id'] != current_track_id:
        print(current_track_info)
        current_track_id = current_track_info['id']

main()