# Binary search tree is a data structure faster on search vs linked list as 
# a search will tha OLog(n)

# A tree is compose o one parent node a child nodes. 

# Parent node should be grater than left child and less than right child

class Node(object):

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
    
    def insert(self, data):

        if not self.root:
            self.root = Node(data)       
        else:
            self.insertNode(data, self.root)
    
    #Olog(N)
    def insertNode(self, data, node):
        """
        To insert the node first we check the left wing, if data is less than node
        then check if there is a leftchild and if true we go recursively until we leftchild is node
        to instantiate a new node.

        The same thing we right wing of the tree
        """
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    #Return the minimum value on the tree 
    def getMinValue(self):
        
        if self.root:
            return self.getMin(self.root)
    
    def getMin(self, node):

        if node.leftChild:
            return self.getMin(node.leftChild)
        
        return node.data
   
    #Return the max value on the tree
    def getMaxValue(self):

        if self.root:
            return self.getMax(self.root)
    
    def getMax(self, node):

        if node.rightChild:
            return self.getMax(node.rightChild)
        
        return node.data
    
    def traverse(self):

        if self.root:
            self.traverseInOrder(self.root)
    
    def traverseInOrder(self, node):

        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        
        print("%s" % node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

    def remove(self, data):
        
        if self.root:
            self.root = self.removeNode(data, self.root)
    
    def removeNode(self, data, node):

        if not node:
            return node
        
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node")
                del node
                return None
            
            if not node.leftChild:
                print("Removing node with single righ child...")
                tempNode = node.rightChild
                del node
                return tempNode
            
            elif not node.rightChild:
                print("Removing node with single left child...")
                tempNode = node.leftChild
                del node
                return tempNode
        
        print("Removing node with two children")
        tempNode = self.getPredecessor(node.leftChild)
        node.data = tempNode.data
        node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        
    def getPredecessor(self, node):

        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node

        


bst = BinarySearchTree()
bst.insert(5)
bst.insert(10)
bst.insert(3)
bst.insert(100)
bst.insert(65)

print(bst.getMinValue())
print(bst.getMaxValue())

bst.traverse()