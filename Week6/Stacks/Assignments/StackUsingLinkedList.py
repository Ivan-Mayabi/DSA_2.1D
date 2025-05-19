class StackNode:
    def __init__(self,data):
        self.data= data
        self.next= None

class LinkedListStack:
    def __init__(self):
        self.top= None

    def is_empty(self):
        if self.top is None:
            raise Exception("This is an empty stack")

    def push(self,data):
        new_node = StackNode(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("The stack is empty")
        else:
            a = self.top.data
            self.top = self.top.next
            return a

    def peek(self):
        if self.is_empty():
            raise Exception("The stack is empty")
        else:
            return self.top.data

    def display(self):
        current = self.top
        # while current is not None:
        #     print(current.data, end=' ')
        #     current = current.next
        values=[]
        while current is not None:
            values.append(str(current.data))
            current = current.next
        print("Stack from top to bottom", "->".join(values))

if __name__=="__main__":
    stack_ll=LinkedListStack()

    stack_ll.push(5)
    stack_ll.push(10)
    stack_ll.push(15)

    stack_ll.display()

    print("Peek top: ", stack_ll.peek())
    print("Pop: ", stack_ll.pop())

    stack_ll.display()

