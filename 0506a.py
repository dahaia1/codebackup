class Stack(object):
    def __init__(self,limit=10):
        self.stack=[]
        self.limit=limit
    def push(sele,data):
        if len(self.stack)>=self.limit:
            print('StackOverflowError')
            pass
        self.stack.append(data)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')
    def peek(self):
        if self.stack:
            return self.stack[-1]
    def is_empty(self):
        return not bool(self.stack)
    def size(self):
        return len(self.stack)
        
