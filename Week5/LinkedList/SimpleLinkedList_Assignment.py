class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self,data):
        new_node = Node(data)
        new_node.next=self.head
        self.head=new_node

    def print_list(self):
        current_node=self.head
        while current_node is not None:
            print(current_node.data, end=' ')
            current_node = current_node.next

    def add_at_end(self,data):
        new_node = Node(data)
        current_node=self.head
        if self.head is None:
            self.head = new_node
        else:
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def del_at_beginning(self):
        if self.head is None:
            print("This is an empty list")
        else:
            self.head = self.head.next

    def del_at_end(self):
        if self.head is None:
            print("This is an empty list")
        elif self.head.next is None:
            self.head = None
        else:
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next
            current_node.next = None

    def search_value(self,value):
        current_node=self.head
        count = 0
        while current_node is not None:
            if current_node.data == value:
                print(f"The value {value} is in the position{count} in the linked list")
                return
            current_node = current_node.next
            count += 1
        print(f"The value {value} is not in the linked list")

if __name__=="__main__":
    llist = LinkedList()

    llist.add_at_beginning("fox")
    llist.add_at_beginning("brown")
    llist.add_at_beginning("quick")
    llist.add_at_beginning("The")

    llist.print_list()

    llist.add_at_end("jumps")

    llist.print_list()

    llist.del_at_beginning()
    print("List after deletion: ")
    llist.print_list()

    print(llist.search_value("quick"))
    print(llist.search_value("lazy"))


