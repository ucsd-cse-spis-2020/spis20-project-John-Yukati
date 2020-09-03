#authorization code flow
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

dictofavgfeatures = dict()
for genre in genresForSearching:
    #opens the .txt file and reads it's contents
    data = open("txtids/"+genre+".txt", "r")
    if data.mode == 'r':
        contents = data.read()
    good_ids = contents.split()


    dictFeatures = dict()
    #def audio_features(idlist):
    #Add new key-values to store audio features
    dictFeatures['acousticness'] = []
    dictFeatures['danceability'] = []
    dictFeatures['energy'] = []
    dictFeatures['instrumentalness'] = []
    dictFeatures['speechiness'] = []
    dictFeatures['valence'] = []
    #create a track counter


    for ids in good_ids:
        #pull audio features per track
        features = spotify.audio_features(ids)
        
        #Append to relevant key-value
        dictFeatures['acousticness'].append(features[0]['acousticness'])
        dictFeatures['danceability'].append(features[0]['danceability'])
        dictFeatures['energy'].append(features[0]['energy'])
        dictFeatures['instrumentalness'].append(features[0]['instrumentalness'])
        dictFeatures['speechiness'].append(features[0]['speechiness'])
        dictFeatures['valence'].append(features[0]['valence'])

    avgFeatures = dict()
    for key in dictFeatures:
        average = sum(dictFeatures[key]) / len(dictFeatures[key])
        avgFeatures[key] = average

    dictofavgfeatures[genre] = avgFeatures

#i made a dataframe with all the average data, ask ethan to help with the distance formula part of it 
df = pd.DataFrame(dictofavgfeatures)
df.to_csv("txtids/features.csv")

# Commented out code below saves attrdf to a csv file, this way we can use 
# data gathered from this notebook in other notebooks

# attrdf.to_csv('songfeaturedata.csv', encoding='utf-8', index=False)

#so i was thinking you know how for each movie, we made that list of 
# all the music genres, maybe j like take this long ass playlist and 
# sort through it to find like 10 random songs that fit the genres in all 
# the music genres

# playlist link: https://open.spotify.com/playlist/54nv8jbrm4JoHEZ49Qvjgl?si=OcdLjHt6TeWCnxFBo7rcDQ
# playlist uri: spotify:playlist:54nv8jbrm4JoHEZ49Qvjgl
# id: OcdLjHt6TeWCnxFBo7rcDQ