
from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()

#get user input 
inputMovie = input("Enter a movie: ")

#get the most popular search result
movies = ia.search_movie(inputMovie)
movieName = movies[0]
#movie name returns this: <Movie id:0133093[http] title:_The Matrix (1999)_>
# for some reason the key 'genre' exists in movie (below), but not movieName even though they are the same type???

#isolate the movie id and save movie name
movieID = movieName.movieID
movie = ia.get_movie(movieID)

#check to see if variables are working + types
print (movieName, type(movieName))
#print (movieID, type(movieID))
#print (movie, type(movie))

# print the genres of the movie
print('Genres:')
genreList = []
for genre in movie['genres']:
    genreList.append(genre)

print(genreList)

# a dictionary of all music genres corresponding to all movie genres
musicdict = {
    "Action" : ["Electronic", "Rock", "Pop", "Dramatic", "Hip-Hop"],
    "Adventure" : ["Metal", "Rock"],
    "Animation" : ["Pop", "Dance"],
    "Comedy" : ["Feel Good", "Pop"],
    "Crime" : ["Rock", "Jazz", "Electronic", "Suspense"],
    "Drama" : ["Hip-Hop", "Romantic", "Indie", "Dramatic"],
    "Family" : ["Feel Good", "Pop"],
    "Fantasy" : ["Pop", "Electronic"],
    "History" : ["Pop", "Acoustic"],
    "Horror" : ["Jazz", "Suspense"],
    "Musical" : ["Broadway"],
    "Mystery" : ["Jazz", "Suspense"],
    "Reality-TV" : ["Pop", "Dance", "Hip-Hop"],
    "Romance" : ["Indie", "Jazz", "Romantic"],
    "Sci-Fi" : ["Electronic"],
    "Sport" : ["Dance", "Rock", "Dramatic", "Hip-Hop"],
    "Thriller" : ["Dramatic", "Suspense",],
    "War" : ["Patriotic"],
    "Western" : ["Country", "Folk", "Acoustic"]
}

# creates a list of the music genres that correspond to that movie
musicgenreList = []
for genre in genreList:
    miniMusicGenres = musicdict[genre]
    for genr in miniMusicGenres:
        if genr in musicgenreList:
            None
        else:
            musicgenreList.append(genr)

print(musicgenreList)