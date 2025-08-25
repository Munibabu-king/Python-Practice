'''def push():
    n=int(input("enter the number"))
    stack.append(n)
def pop():
    stack.pop()
def display():
    if len(stack)==0:
        print("stack is underflow")
    else:
        for i in reversed(stack):
            print(i)
def exit():
    print("unnon type")
    
          
stack=[]
while True:
    a=int(input("1.push\n2.pop\n3.display\n4.exit:"))
    if a==1:
        push()
    elif a==2:
        pop()
    elif a==3:
        display()
    else:
        exit()'''
#stack
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self):
        x=int(input("inserted value"))
        new=Node(x)
        if self.top==None:
            self.top=new
            self.top.next=None
        else:
            new.next=self.top
            self.top=new
    def pop(self):
        if self.top==None:
            print("empty stack")
        elif self.top.next==None:
            print("deleted elements is-- ",self.top.data)
            self.top=None
        else:
            temp=self.top
            print("deleted elemnts--",temp.data)
            self.top=temp.next
            temp=None
    def display(self):
        if self.top==None:
            print("stack is empty")
        else:
            print("elemts in stacks are:")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
            print("top of elemt-->",self.top.data)
    def exit(self):
        print("no operation")
            
            
        
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
'''
'''#queue
def inset():
    n=int(input("enter the elments"))
    queue.append(n)
def delete():
    if len(queue)==0:
        print("queue is empty")
    else:
        print("the elemt",queue[0])
        del queue[0]
def display():
    if len(queue)==0:
        print("queue is empty")
    else:
        for i in reversed(queue):
            print(i,end="--->")
            print(end='')
def exitt():
    print("no oeration")
    
    
queue=[]
while True:
    n=int(input("\n1.insert\n2.delete\n3.display\n4.exit:"))
    if n==1:
        inset()
    elif n==2:
        delete()
    elif n==3:
        display()
    else:
        exitt()  '''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.rear=None
        self.front=None
    def inset(self):
        k=int(input("insert the values:"))
        new=Node(k)
        if self.rear is None:
            self.rear=new
            self.front=new
        else:
            self.rear.next=new
            self.rear=new
    def delete(self):
        if self.rear==None:
            print("empty queue")
        elif self.front.next is None:
            print('deleted element',self.front.data)
            self.front=None
            self.rear=None
        else:
            temp=self.front
            print('deleted elment',temp.data)
            self.front=temp.next
            temp=None
    def display(self):
        if self.rear==None:
            print("empty queue")
        else:
            temp=self.front
            while temp:
                print("queue--->",temp.data)
                temp=temp.next
                temp=None
        
q=queue()
while True:
    n=int(input("\n1.insert\n2.delete\n3.display\n4.exit:"))
    if n==1:
        q.inset()
    elif n==2:
        q.delete()
    elif n==3:
        q.display()
    else:
        q.exitt()       
        


