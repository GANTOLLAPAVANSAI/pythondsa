class Queue:
     def __init__(self):
         self.queue = [6]
         self.front = -1
         self.rear = -1
         self.n=6
         self.size=0
     def enqueue(self, data):
         if(self.n==self.size):
             return "Queue is full"
         elif(self.size==0 or self.rear==-1):
             self.rear+=1
             self.queue[self.rear]=data
             #self.rear+=1
             self.front+=1
             self.size+=1
         else:
             self.rear=+1
             self.queue[self.rear]=data
             #self.rear=+1
             self.size+=1
             
         

     '''def dequeue(self):
         if len(self.queue) == 0 :
             print("Queue is empty")
             return -1
         if(len(self.queue) > 1):
             item = self.queue[self.front]
         else:
             item = self.queue[self.front+1]
         self.queue.pop(0)
         print("Deleted item:", item)
         if(len(self.queue) == 0):
             self.rear = -1
             self.front = -1
         else:
             self.rear-=1'''


     

     '''def isEmpty(self):
         if(self.size==0):
             return False
         else:
             return True'''
        
     

     def display(self):
         if self.size==0:
             print("Queue is empty")
         else:
             print("Elements ",self.queue)


ob = Queue()
#ob.enqueue(7)
#ob.enqueue(8)
#ob.enqueue(6)
#ob.dequeue()
#ob.dequeue()
ob.enqueue(2)
ob.display()