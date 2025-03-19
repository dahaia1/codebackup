class SqList:
    def __init__(self,MaxSize):
        self.MaxSize = MaxSize
        self.size = 0
        self.data = [None] * self.MaxSize
    def load(self,Elem):
        if len(Elem) > self.MaxSize:
            return -1
        for i in range(len(Elem)):
            self.data[self.size] = Elem[i]
            self.size += 1

    def add(self,pos,e):
        if self.size == self.MaxSize:
            return -1
        i = self.size
        while i > pos:
            self.data[i] = self.data[i - 1]
            i -= 1
        self.data[pos] = e
        self.size += 1

    def delete(self,pos):
        if self.size == 0:
            return -1
        for i in range(pos,self.size - 1):
            self.data[i] = self.data[i +1]
        self.data[self.size - 1] = None
        self.size -= 1

    def judge(self):
        if self.size == self.MaxSize:
            print('The list is full!')
        elif self.size == 0:
            print('the list is empty!')
        else:
            vac = self.MaxSize - self.size
            print('There are only %d vacancies left!' %vac)
    def search(self,e):
        for i in range(len(self.data)):
            if self.data[i] == e:
                print("The position of the data you are searching is:%d" % i)
                break
    def allocate(self,new_size):
        self.data += [None] * new_size
        self.MaxSize += new_size

a = [1,2,3,4,5]
sqlist = SqList(6)
print('The list you have created:')
print(sqlist.data)
sqlist.load(a)
print('The list after you put datas in:')
print(sqlist.data)
sqlist.add(5,6)
print('Add the data 6 on position 5:')
print(sqlist.data)
sqlist.delete(0)
print('Delete the data on position 0:')
print(sqlist.data)
print('Search the position of data 6------------------')
sqlist.search(6)
print('Judge the rest places of the list-------------------')
sqlist.judge()
sqlist.allocate(3)
print('The rest places of the list after allocating new places---------------')
sqlist.judge()
