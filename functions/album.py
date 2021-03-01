#Use the function to make three dictionaries representing different albums. 
#print each retune value to show that the dictionaries are sorting the album correctly

def makeAlbum(artistName, albumTitle, songs=0):
  albums = { 
    'artistName' : artistName.title(),
    'albumTitle': albumTitle.title()
  }
  if songs:
    albums['songs'] = songs 
  return(albums)




albumOne = makeAlbum('john lennon', 'imagine')
print(albumOne) 

albumtwo = makeAlbum('alejandro fernandez', 'hecho en mexico')
print(albumtwo) 

albumThree = makeAlbum('anuel aa', 'emmanuel', songs=10)
print(albumThree)  

