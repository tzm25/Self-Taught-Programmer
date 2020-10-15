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
         
 
 
stack = Stack()
 
for c in "yesterday":
    stack.push(c)
    
reversed_str = ""

for i in range(len(stack.items)):
    reversed_str += stack.pop()
    
print(reversed_str)