class Node:
    def __init__(self, data):
        self.data = data   #store data 
        self.next = None   # pointer to next node 
        self.prev = None   # poniter to previous node

#creating nodes 
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

#linking nodes forward and backward
node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

#traversing forward from head 
print("Forward traversal:")
current = node1
while current is not None:
    print(current.data, end=" <-> ")
    current = current.next
print("None")

#Traversing backward from tail
print("Backward traversal:")
current = node4
while current is not None:
    print(current.data, end=" <-> ")
    current = current.prev
print("None")


