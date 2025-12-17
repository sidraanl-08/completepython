#understanding linkedlist
#making a simple linked list 

#STEP1: make structure to make nodes

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


#STEP2: make nodes according to class Node
#we are just making the nodes
#they are not connected yet

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)


#STEP3: connect the nodes to form a linked list

node1.next = node2
node2.next = node3
node3.next = node4


#STEP4: print the linked list

current = node1
while current is not None:
    print(current.data, end="->")
    current = current.next
print("None")