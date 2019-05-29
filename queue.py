# Queue is an abstract data type (interface)
# Basic operation are: enqueue(), dequeue(), peek()
# It uses a FIFO structure First-in First-out
# It can be implemented with arrays and linked lists

class Queue:

    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        data = self.queue[0]
        #del self.queue[0]
        self.queue.remove(data)
        return data
    
    def peek(self):
        return self.queue[0]
    
    def sizeQueue(self):
        print(len(self.queue))

if __name__ == "__main__":
    q = Queue()
    print(q.isEmpty())

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    q.sizeQueue()

    q.dequeue()
    
    print(q.queue)
    q.sizeQueue()

    
