class Node:
    def __init__(self,date):
        self.data = data
        self.next = None
class Linked_Liset:
    def __init__(self):
        self.head = None
    def initlist(self,date_list):
        self.head=Node(date_list[0])
        temp=self.head
        for i in date_list[1:]:
            node=Node(i)
            temp.next=node
            temp.temp.next
    def is_empty(self):
        if self.head.next==None:
            print("Linked_list is empty")
            return True
        else:
            return False
    def get_lenght(self):
        temp=self.head
        lenght=0
        while temp!=None:
            length=length+1
            temp=temp.next
        return lenght
    def insert(self,key,value):
        if key<0 or key>self.get_length()-1:
            print("insert error")
        temp=self.head
        i=0
        while i<key:
            pre=temp
            temp=temp.next
            i=i+1
        node=Node(value)
        pre.next=temp
    def print_list(self):
        print("linked_list:")
        temp=self.head
        new_list=[]
        while temp is not None:
            new_list.append(temp.data)
            temp=temp.next
        print(new_list)
    def remove(self,key):
        if key<0 or key>self.get_length()-1:
            print("insert error")
        i=0
        temp=self.head
        while temp !=None:
            pre=temp
            temp=temp.next
            i=i+1
            if i==key:
                pre.next=temp.next
                temp=None
                return True
        pre.next=None
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current_node
        self.head = prev
