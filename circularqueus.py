class Queue:
     def __init__(self,size):
         self.queue=[0]*size
         self.front = 0
         self.rear = 0
         self.size=0
         self.cap=size

     def enqueue(self,data):
          if(self.size<self.cap):
               self.queue[self.rear]=data
               self.size+=1
               self.rear=(self.rear+1)%self.cap
               return
          print("Queue is full")
     def dequeue(self):
          if(self.size<=0):
               print("Queue is empty")
               return
          data=self.queue[self.front]
          self.queue[self.front]=0
          self.front+=1
          self.size-=1
          return data
     def display(self):
          if(self.size!=0):
               print(self.queue)
obj=Queue(5)
obj.enqueue(10)
obj.enqueue(7)
obj.enqueue(9)
obj.enqueue(6)
obj.enqueue(5)
obj.dequeue()
obj.display()