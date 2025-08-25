class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Line:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head==None:
            print("list is empty")  #we check temp has value or not
        else:
            temp=self.head
            while temp:
                print(temp.data)
                temp=temp.next
    def insertBig(self,data):
        ni=Node(data)
        ni.next=self.head
        self.head=ni
    def insertEnd(self,data):
        nt=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next   #we check we is none
        temp.next=nt
    def insertPos(self,pos,data):
        nx=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        nx.next=temp.next
        temp.next=nx
    def delet(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delets(self):
        temp=self.head.next
        prev=self.head
        while temp.next:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def deletsw(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    def countOf(self):
        temp=self.head
        count=0
        while temp:
            count=count+1
            temp=temp.next
        print(count)
        
        
n1=Node(20)
l=Line()
l.head=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
l.insertBig(50)
l.insertPos(1,67)

l.display()
print("...........")
l.countOf()

