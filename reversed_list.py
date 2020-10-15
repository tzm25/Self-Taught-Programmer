class Stack:
     def __init__(self):
         self.items = []
     def push(self,item):
         self.items.append(item)
     def pop(self):
         return self.items.pop()
     def peek(self):
         self.items[len(self.items)-1]
     def is_empty(self):
         return self.items == []
     def size(self):
         return len(self.items)

lst = [1,2,3,4,5]
li = []

stack = Stack()

for it in lst:
    stack.push(it)
    
for i in range(len(stack.items)):
    li.append(stack.pop())
    
print(li)