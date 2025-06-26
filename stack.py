class MyStack:
    def __init__(self,a):
        self.stack=[]
        self.max=a
    def is_empty(self):
        return len(self.stack)==0
    def pop(self):
        if not self.is_empty():
            item=self.stack.pop()
            print(f"{item} popped")
        else:
            return print("stack  underflow")
    def push(self,item):
        if len(self.stack)<self.max:
            self.stack.append(item)
            print(f"{item} inserted")
        else:
            print("ovwerflow")
        
    def peek(self):
        if not self.is_empty():
            return print(f"last element {self.stack[-1]}")
        else:
            print("empty stack")
    def display(self):
        if not self.is_empty():
            for i in reversed(self.stack):
                print(f"elements {i}")
        else:
            print("display empty stack message")
def mun():
    s=MyStack(2)
    while True:
        print("\n \n1.push \n2.pop \n3.peek \n4.display \n5.exit ")
        #print("ener ur choice")
        n=int(input("enter choice "))
        if n ==1:
            item=int(input("enter no to add "))
            s.push(item)
        elif n == 2:
            s.pop()
        elif n == 3:
            s.peek()
        elif n == 4:
            s.display()
        elif n == 5:
            print("exiting...")
            break
        else:
            print("invalid choice")
mun():       


