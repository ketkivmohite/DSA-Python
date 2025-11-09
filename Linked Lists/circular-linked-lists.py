class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#creating nodes 
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

#connecting nodes to form a circular linked list 
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1  # this makes it circular!

#printing the circular linked list(stops after one full cycle)
current = node1
while True:
    print(current.data, end= " ->")
    current = current.next
    if current == node1:
        break
print("(back to head)") 