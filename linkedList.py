

class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self, data):
        #everytime new node is insert it, list size is bigger
        self.size = self.size + 1
        #instantiate new node
        newNode = Node(data)

        #if not head means node is new head
        if not self.head:
            self.head = newNode
        #else newnode will reference to the head
        else:
            newNode.nextNode = self.head
            self.head = newNode
    
    def remove(self, data):

        if self.head is None:
            return
        
        #decrease de size of the linked list
        self.size = self.size - 1 

        #set current node variable to be head
        currentNode = self.head 
        previousNode = None

        #While data is not found keep going
        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode

    def Size(self):
        return self.size
    
    def insertEnd(self, data):

        self.size = self.size + 1
        newNode = Node(data)
        #actual Node will always be the node in the list
        actualNode = self.head

        #while actual node is not null them go to the next to find it
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        
        #finally update the reference of the actual node next node to be the new node
        actualNode.nextNode = newNode
    
    def traverseList(self):

        actualNode = self.head

        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode