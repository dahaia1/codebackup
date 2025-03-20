class ArrayStack:
    def __init__(self):
        self._data=[]
    def size(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data)==0
    def push(self,e):
        self._data.append(e)
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data.pop()
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data[-1]
araayStack=ArrayStack()
araayStack.push("Python")
araayStack.push("Learning")
araayStack.push("Hello")
print("Stack top element:",araayStack.top())
print("Stack length:",araayStack.size())
print("Stack poped item:%s"%araayStack.pop())
print("Stack is empty?",araayStack.is_empty())
araayStack.pop()
araayStack.pop()
print("Stack is empty?",araayStack.is_empty())
