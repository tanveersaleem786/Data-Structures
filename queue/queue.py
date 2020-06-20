import sys
sys.path.append('./singly_linked_list')
sys.path.append('./stack')
from singly_linked_list import LinkedList
from stack import Stack



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
"""
Answer for Q3:-
In this case array and linked list are working the same way but there are different way to implement queue with array
"""

class Queue1:
    def __init__(self):
        self.size = 0
        self.storage = []
       
    
    def __len__(self):
        return self.size


    def enqueue(self, value):  
        #self.storage.insert(0,value)
        self.storage.append(value)
        self.size += 1


    def dequeue(self):
        if self.size != 0:
            self.size -= 1
            #return self.storage.pop()
            return self.storage.pop(0)
        else:
            return None
   

# Queue with LinkedList
class Queue2:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
       
    
    def __len__(self):
        return self.size

    def enqueue(self, value):          
        self.storage.add_to_tail(value)
        self.size += 1    

    def dequeue(self):
        if self.size != 0:
            self.size -= 1           
            return self.storage.remove_head()
        else:
            return None

# Queue with Stack
class Queue:
    def __init__(self):       
        self.stack1 = Stack()
        self.stack2 = Stack()

    
    def __len__(self):
        return self.stack1.size


    def enqueue(self, value):          
        self.stack1.push(value) 


    def dequeue(self):
        
        if self.stack1.size != 0:
            
            while(self.stack1.size > 0):           
                x = self.stack1.pop()                 
                if self.stack1.size > 0:
                    self.stack2.push(x) 
             
            while(self.stack2.size > 0):
                y = self.stack2.pop()                                
                self.stack1.push(y)    

            return x              
            
        else:
            return None
   
        
#qu = Queue()
#https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaQueueinPython.html
# qu = Queue()
# print(f'Queue Length: {qu.__len__()}')
# qu.enqueue(1)
# qu.enqueue(2)
# qu.enqueue(3)
# qu.enqueue(4)
# qu.enqueue(5)
# print(f'Queue Length: {qu.__len__()}')


# print(f'Stack1: {qu.stack1.storage}')
# print(f'Stack2: {qu.stack2.storage}')
# print(qu.dequeue())
# print(f'Stack1: {qu.stack1.storage}')
# print(f'Stack2: {qu.stack2.storage}')

# print(qu.dequeue())
# print(f'Stack1: {qu.stack1.storage}')
# print(f'Stack2: {qu.stack2.storage}')


# print(qu.dequeue())
# print(f'Stack1: {qu.stack1.storage}')
# print(f'Stack2: {qu.stack2.storage}')

# print(qu.dequeue())
# print(f'Stack1: {qu.stack1.storage}')
# print(f'Stack2: {qu.stack2.storage}')

# print(qu.dequeue())
# print(f'Stack1: {qu.stack1.storage}')
# print(f'Stack2: {qu.stack2.storage}')

# print(qu.dequeue())
# print(f'Stack1: {qu.stack1.storage}')
# print(f'Stack2: {qu.stack2.storage}')





