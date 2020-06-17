"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
        # self.header = None
        # self.tail = None
    
    def __len__(self):
        return self.size

    def enqueue(self, value):  
        #self.storage.insert(0,value)
        self.storage.append(value)
        self.size += 1
        # if self.header is None and self.tail is None:    
            
        #     self.size += 1
        #     self.header = 0
        #     self.tail = 0    
        # else:
        #     self.storage.append(value)
        #     self.size += 1            
        #     self.tail += 1    

    

    def dequeue(self):
        if self.size != 0:
            self.size -= 1
            #return self.storage.pop()
            return self.storage.pop(0)
        else:
            return None
        # if self.size != 0:
        #     self.storage.remove(self.storage[self.header])
        #     self.size -= 1
        #     self.tail -= 1
        
        
#qu = Queue()
#https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaQueueinPython.html
# qu = Queue()
# print(qu.__len__())
# qu.enqueue(2)
# print(qu.__len__())
# qu.enqueue(3)
# print(qu.__len__())

# qu.dequeue()
# print(qu.__len__())