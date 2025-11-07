#Let's imagine you are building a very basic music playlist. Each song is a node,
# containing the song's title (like your node's data), and each song points to the next 
# song in the sequence (using the next pointer).
#If you want to play all songs in order, you start from the first song and then 
#follow the chain (next) until you reach the end

class Node:
    def __init__(self, song):
        self.data = song #song title 
        self.next = None #next song in the playlist

#creating the playlist nodes (songs)
song1 = Node("Blankspace")
song2 = Node("Lover")
song3 = Node("Snap")
song4 = Node("Style")

#Link songs in playlist order 
song1.next = song2
song2.next = song3
song3.next = song4

#Play songs in order 
current = song1
while current:
    print("Playing:", current.data)
    current = current.next
print("End of Playlist")