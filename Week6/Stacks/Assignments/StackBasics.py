""""Simple method to make a stack"""
#Empty list to represent stack
stack:list = []

#Add data to stack
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after print: ", stack)

#Peek at the top
top_element = stack[-1]
print(f"Top Element is: {top_element}")

#Check if the stack is empty
if len(stack) == 0:
    print("This stack is empty")
else:
    print("Stack is not empty")

""""Custom class"""
class Stack:
    def __init__(self):
        self.data:list=[]

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def push(self,value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop on empty stack")
        else:
            return self.data.pop(-1)

    def peek(self):
        if self.is_empty():
            raise Exception("Cannot peek at an empty list")
        else:
            return self.data[-1]

    def size(self):
        return len(self.data)

    def print_stack(self):
        print(f"The stack from front to back is: {self.data}")

if __name__=="__main__":
    stack1 = Stack()

    stack1.push(1000)
    stack1.push(2000)
    stack1.push(3000)

    stack1.print_stack()

    print("Top Element: ", stack1.peek())

    print(f"Popped Element: {stack1.pop()}")
    stack1.print_stack()

    stack1.pop()
    stack1.pop()
    print("Is the stack empty after popping 3 items? ", stack1.is_empty())



