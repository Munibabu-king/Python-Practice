class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self):
        n=int(input("enter elemnt"))
        new=Node(n)
        if self.top==None:
            self.top=new
            self.top.next=None
        else:
            new.next=self.top
            self.top=new
    def pop(self):
        if self.top==None:
            print("no elemts are there")
        elif self.top.next==None:
            print("elemated data--->",self.top.data)
            self.top=None
        else:
            temp=self.top
            print("elemnated data-->",self.top.data)
            self.top=temp.next
            temp=None
    def display(self):
        if self.top==None:
            print("stack is empty")
        else:
            temp=self.top
            while temp:
                print("the stack is ",temp.data)
                temp=temp.next
        print("top of the stack is",self.top.data)
            
            
            
            
s=Stack()
while True:
    n=int(input("1.push\n2.pop\n3.display\n4.exit:"))
    if n==1:
        s.push()
    elif n==2:
        s.pop()
    elif n==3:
        s.display()
    else:
        s.exit()
        
