#Imagine you have a simple photo gallery where each image can be viewed one at a time. 
# You want to be able to go to the next photo or back to the previous photo easily—just like in an image viewer 
# app on your phone. 
# Each photo becomes a node in your doubly linked list.
#The next lets you go forward, and prev lets you go backwards.

class Node:
    def __init__(self, photo_name):
        self.data = photo_name   #Photo file name or name 
        self.next = None   # pointer to next node 
        self.prev = None   # pointer to previous node

#creating photo nodes (photos in album)
pic1 = Node("family.jpg")
pic2 = Node("vacation.png")
pic3 = Node("birthday.bmp")
pic4 = Node("graduation.tiff")

#link photos in both directions 
pic1.next = pic2
pic2.prev = pic1
pic2.next = pic3
pic3.prev = pic2
pic3.next = pic4
pic4.prev = pic3

#start viewing from the first photo 
current = pic1 

#view forward through the album 
print("Viewing forward: ")
while current:
    print("Viewing photo:", current.data)
    current = current.next

#now view backward from the last photo 
current = pic4 
print("\nViewing backward: ")
while current:
    print("Viewing photo:", current.data)
    current = current.prev
    