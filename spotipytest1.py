#authorization code flow
import sys
import spotipy
import spotipy.oauth2 as oauth2
import csv 

client_id = "3628a923d3b94e21aa42b2f305e03b8c"
client_secret = "2d7c5941ea754a23ae050fed2b663189"

credentials = oauth2.SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret)

token = credentials.get_access_token(as_dict=False)
spotify = spotipy.Spotify(auth=token)

print ("Good Morning")


#list of all the music genres we have 
genresForSearching = ['Metal', 'Electronic', 
'Rock', 'Pop', 'Dance', 'Feel Good', 'Jazz', 'Suspense',
'Hip-Hop', 'Romance', 'Indie', 'Dramatic', 'Acoustic', 'Chill', 'Patriotic', 'Country']



#take one genre for each loop iteration

genreTotal = dict()
for specificgenre in genresForSearching:

        # specificgenre = genresForSearching[0]
        # finds playlists for a genre query
        results = spotify.search(q='playlist:'+specificgenre, type='playlist', limit=4)
        # narrows down dictionary scope
        items = results['playlists']['items']
        # creates a list of playlist uris
        listofplaylisturis =[]
        for i in range(len(items)):
                playlist = items[i]
                listofplaylisturis.append(playlist['id'])

        # gives ID of all songs in all playlist
        genre_ids = [] 
        for uri in listofplaylisturis:
                #search for the playslist
                genre_playlist = spotify.playlist(uri)
                #lines below enumerate each song
                genre_tracks = genre_playlist["tracks"]
                genre_songs = genre_tracks["items"] 
                #adds each track to a list
                while genre_tracks['next']:
                        genre_tracks = spotify.next(genre_tracks)
                        for item in genre_tracks["items"]:
                                genre_songs.append(item)
                # a list of all the ids for the songs
                for i in range(len(genre_songs)):
                        try:
                                if genre_songs[i]['track']['id'] != None:
                                        genre_ids.append(genre_songs[i]['track']['id'])
                        except TypeError:
                                i = i + 1

        # saves the list of songs for each genre
        genreTotal[specificgenre] = genre_ids

        w = open("txtids/"+specificgenre+".txt","w") 
  
# \n is placed to indicate EOL (End of Line) 
        for id in genre_ids:
                w.write(id+" ") 
       # w = csv.writer(open(specificgenre+".csv", "w"))
       # w.writerow(genre_ids)

#print(genreTotal)
#print(items['display_name'])

#print(results['playlists'])
#print(items)

#if len(items) > 0:
        #artist = items[0]
        #print(artist['name'], artist['images'][0]['url'])

