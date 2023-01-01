import requests
import time

current_track_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
best_tracks_URL = 'https://api.spotify.com/v1/me/top/tracks'
best_artists_URL = 'https://api.spotify.com/v1/me/top/artists'

current_track_token = 'BQCr4f3aiowYHcNZna1YWwIFX9H9MT0OtP-LyTIhDL26zZW7IeqqlGAuAyDF2jJcPL4X-dhV8PX7awJz_3rkLslAkihFpPq5rWHeLNFLvKtAk1vgVSbCmIg4toiLA4oEa9PUjK2MLLtaB1ALHTYTsqcWGcXsHdvpprhPCk5fsdHzorxSzNmqkNtEg6Fl9MxQn8de'
best_tracks_token = 'BQAEHcCebTnxQYnGiP_OaQ1dAdFJM5qLrPTQsEoIUhk5G3Z2sdA8-UiL3hlhBoWBZVZsuqdKl6MMaShSzee4fjGsI6LZ1QAc7PQtB0N4jFyTJEKSycao5JIROpnoNeChZog0QYfk263IIKYC7GLn06YIXbYimaVh3QKejc0X416I_OD-FpDnwz8MIWBjlbeFpqq_JS0'
best_artists_token = 'BQAa5ZicFb8HcpniQ7zn07ev5gHO3P-PClIVR57fiCebg9m5dXaqXtFVB1PcuauXuVpWow6_zzOzaPYLCngqeFfvgRR4Ls67JwA_32asJ-UkmxA6W_SDhbuoCttaYx8ZPQGmM_122JpnJKwFXrEqBYeOUGisLMU5q8u3OJ7LnDUrVQyoSXbwacJovHJpqY2t_ncZoWM'

def get_best_tracks():
    response = requests.get(best_tracks_URL, headers={
        "Authorization" : f"Bearer {best_tracks_token}"
    })
    json_resp = response.json()
    
    for i in range(len(json_resp)):
        #Getting artists
        artists = [artist for artist in json_resp['items'][i]['artists']]
        artist_names = ', '.join([artist['name'] for artist in artists])

        best_tracks = {
            "name" : json_resp['items'][i]['name'],
            "artists" : artist_names,
        }

    return best_tracks

def get_best_artists():
    response = requests.get(best_artists_URL, headers={
        "Authorization" : f"Bearer {best_artists_token}"
    })
    json_resp = response.json()

    for i in range(len(json_resp)):
        #Getting artists
        artists = [artist for artist in json_resp['item'][i]['artists']]
        artist_names = ', '.join([artist['name'] for artist in artists])
        #Getting genres
        genres = [genre for genre in json_resp['item'][i]['genres']]
        genre_names = ', '.join([genre['name'] for genre in genres])

        best_artists = {
            "name" : json_resp['items'][i]['name'],
            "artists" : artist_names,
            "genres" : genre_names
        }

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
    	"track_name": json_resp['item']['name'],
    	"artists": artist_names
    }

    return current_track_info


def main():
    current_track_id = None

    best_tracks = get_best_tracks() #SHORT_TERM (4 weeks)
    print(best_tracks)

    best_artists = get_best_artists() 
    print(best_artists)

    while True:
        current_track_info = get_current_track()
        if current_track_info['id'] != current_track_id:
            print(current_track_info)
            current_track_id = current_track_info['id']
        time.sleep(1)

main()