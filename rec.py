import array as ary
class MyStack:
    stack = ary.array('i', [])
    top=0
    
    def __init__(self):
        self.top=-1
    
    #Function to push an integer into the stack.
    def __Isempty(self):
        if(self.top == -1):
            print("false hu ")
            return True
        return False

    def push(self, element):
        self.stack.append(element)
        self.top=self.top+1
        return self.stack
        
    def pop(self):
        if(not self.__Isempty()):
            self.stack.pop()
            self.top-=1
            return self.stack
        else:
            print("Stack is Empty")
object=MyStack()
print(object.push(8))
print(object.push(7))
print(object.pop())