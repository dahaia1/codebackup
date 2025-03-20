class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkList:
    def __init__(self,n):
        self.head=Node(None)
        self.n=n
    def listCreateForward(self):
        if self.n==0:
            return False
        else:
            temp=self.head
            for i in range(1,self.n+1):
                print('请输入第{0}个节点:'.format(i))
                num = input()
                node = Node(num)
                node.next=temp.next
                temp.next = node
    def listCreateBackward(self):
        if self.n==0:
            return False
        else:
            temp=self.head
            for i in range(1,self.n+1):
                print('请输入第{0}个节点:'.format(i))
                num = input()
                node = Node(num)
                temp.next=node
                temp=node
    def readList(self):
        if self.n==0:
            print("空链表！")
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
                print(temp.data,end=' ')
    def Length(self):
        i=0
        temp=self.head
        while temp.next!=None:
            temp=temp.next
            i+=1
        return i
    def locateElem(self,num):
        i = 0
        temp = self.head
        while temp.next != None:
            temp = temp.next
            i += 1
            if int(temp.data)==num:
                return i
        return None
    def getElem(self,j):
        i = 0
        temp =self.head
        while temp.next != None:
            temp = temp.next
            i += 1
            if int(j)==1:
                return temp.data
        return None
    def listInsert(self,j,num):
        if int(j)<0:
            return None
        elif self.Length()<j:
            return None
        else:
            i = 0
            temp = self.head
            while temp.next != None:
                i += 1
                if int(j) == i:
                    node=Node(num)
                    node.next=temp.next
                    temp.next=node
                temp = temp.next
    def deleteData(self,num):
        temp=self.head
        while True:
            if temp.next==None:
                break
            if int(temp.next.data)==num and temp.next.next==None:
                temp.next=None
                break
            elif int(temp.next.data)==num:
                temp.next=temp.next.next
            temp=temp.next
    def deleteElem(self,j):
        if j==1:
            self.head.next=self.head.next.next
        elif j==self.Length() :
            temp=self.head.next
            while True:
                if temp.next.next==None:
                    temp.next=None
                    break
                temp=temp.next
        elif j<self.Length():
            i=2
            temp=self.head.next
            while True:
                if i==j:
                    temp.next=temp.next.next
        else:
            print('erro!!!!')
            return None
linklist1=linkList(5)
linklist1.listCreateBackward()
linklist1.readList
length=linklist1.Length()
print('Length={0}'.format(length))
locate=linklist1.locateElem(5)
print('5在位置{0}'.format(locate))
data=linklist1.getElem(3)
print('第3个位置{0}'.format(data))
linklist1.listInsert(1,111)
linklist1.readList()
print('\n删除111(第一个元素):')
linklist1.deleteData(111)
linklist1.readList()
print('\n删除5(末尾的元素)')
linklist1.deleteData(5)
linklist1.readList()
print('\n删除第一个元素:')
linklist1.deleteElem(1)
linklist1.readList()
print('\n删除末尾的元素')
linklist1.deleteElem(3)
linklist1.readList()
