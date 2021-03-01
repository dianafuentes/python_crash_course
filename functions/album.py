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

#write a while loop that allows users to enter an album and artist. 
while True: 
  print("\n Enter an album name")
  print(" & Enter an artist name")
  print("ENTER 'q' AT ANY TIME TO QUIT")
  
  albumTitle = input("Album name:")
  if albumTitle == 'q':
    break 
  
  artistName = input("Artist name:")
  if artistName == 'q':
    break 

  album = makeAlbum(artistName, albumTitle)
  print(album)

  # NOTE: Dicitionaly keys can be printed out by calling
  # the variable and the key in brackets.
  # print(album['albumTitle'])
  # print(album['artistName'])

print("\nThanks for responding!")





#albumOne = makeAlbum('john lennon', 'imagine')
#print(albumOne) 

#albumtwo = makeAlbum('alejandro fernandez', 'hecho en mexico')
#print(albumtwo) 

#albumThree = makeAlbum('anuel aa', 'emmanuel', songs=10)
#print(albumThree)  

