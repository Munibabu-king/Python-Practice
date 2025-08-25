class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SSL:
    def __init__(self):
        self.head=None     
    def display(self):
        if self.head==None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data)
                temp=temp.next
    def Insert_beg(self,data):
        ni=Node(data)
        ni.next=self.head
        self.head=ni
    def Insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def Insert_pos(self,pos,data):
        nx=Node(data)
        temp=self.head
        for i in (pos-1):
            temp=temp.next
        nx.data=data
        nx.next=temp.next
        temp.next=nx
    def Delet(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def deletEnd(self):
        temp=self.head.next
        prev=self.head
        while temp:
            temp=temp.next
            prev=prev.next
        prev.next=None
        
        
n1=Node(20)
l=SSL()
l.head=n1
n2=Node(25)
n1.next=n2
n3=Node(45)
n2.next=n3
l.Delet()
l.deletEnd()
l.display()
                
        
