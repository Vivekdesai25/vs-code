class MyStack:
    def __init__(self):
        self.stack=[]
    def is_empty(self):
        return len(self.stack)==0
    def pop(self):
        if not self.is_empty():
            item=self.stack.pop()
            print(f"{item} popped")
        else:
            return print("stack  underflow")
    def push(self,item):
        self.stack.append(item)
        print(f"{item} inserted")
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
s=MyStack()
s.push(100)
s.push(200)
s.push(300)
s.push(400)
s.push(500)
s.pop()
s.pop()
s.peek()
s.display()
s.pop()
s.pop()
s.pop()
s.peek()
s.display()