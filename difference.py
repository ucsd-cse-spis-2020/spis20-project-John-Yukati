import sys
import spotipy
import spotipy.oauth2 as oauth2
import csv 
import pandas as pd

client_id = "3628a923d3b94e21aa42b2f305e03b8c"
client_secret = "2d7c5941ea754a23ae050fed2b663189"

credentials = oauth2.SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret)

token = credentials.get_access_token(as_dict=False)
spotify = spotipy.Spotify(auth=token)

genresForSearching = ['Metal', 'Electronic', 
'Rock', 'Pop', 'Dance', 'Feel Good', 'Jazz', 'Suspense',
'Hip-Hop', 'Romance', 'Indie', 'Dramatic', 'Acoustic', 'Chill', 'Patriotic', 'Country']
tracks = ['10igKaIKsSB6ZnWxPxPvKO']

features = spotify.audio_features(tracks)

prediction = []

prediction.append(features[0]['acousticness'])
prediction.append(features[0]['danceability'])
prediction.append(features[0]['energy'])
prediction.append(features[0]['instrumentalness'])
prediction.append(features[0]['speechiness'])
prediction.append(features[0]['valence']) 

print(prediction)
dif = []
genreList = []

with open("txtids/features.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for i in range(len(genresForSearching)):
        for row in reader:
            genreList.append(row[genresForSearching[i]])
        print(genreList)


"""
zip_object = zip(list1, list2)
for list1_i, list2_i in zip_object:
    difference.append(list1_i-list2_i)
"""