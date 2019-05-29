# Stack is an abstrack data type.
# Main operations includes:
#  - pus()
#  - pop()
#  - peek()
# It has LIFO structure meaning Last in, First Out

# Push - Adding a new element into the Stack is done in O(1)
# Pop -  Removes the last element inserted as LIFO, is done in O(1)
# Peek - Returns the las item in the stack without remove it O(1)

# Stack aplications:

# - In stack oriented programming
# - Graph algorithm depth-first search
# - Finding Euler-cycles ina Graph
# -  Finding strongly connected components in a graph
class Stack:

    def __init__(self):
        self.stack = []

    def isEmpy(self):
        return self.stack == []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        return self.stack[-1]
    
    def sizeStack(self):
        return len(self.stack)
        
