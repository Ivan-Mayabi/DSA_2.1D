class TreeNode:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value

    def insert(self,key_value):
        if key_value < self.value:
            if self.left is None:
                self.left=TreeNode(key_value)
            else:
                self.left.insert(key_value)

        elif key_value > self.value:
            if self.right is None:
                self.right=TreeNode(key_value)
            else:
                self.right.insert(key_value)

        else:
            print("You cannot have an equal value")

    def pre_order_traversal(self):
        print(self.value,end="->")

        if self.left:
            self.left.pre_order_traversal()

        if self.right:
            self.right.pre_order_traversal()

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()

        print(self.value,end="->")

        if self.right:
            self.right.in_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()

        if self.right:
            self.right.post_order_traversal()

        print(self.value,end="->")

    def search(self,key_value):
        pass

if __name__=="__main__":
    tree_obj = TreeNode(17)

    tree_obj.insert(5)
    tree_obj.insert(3)
    tree_obj.insert(4)
    tree_obj.insert(23)
    tree_obj.insert(20)
    tree_obj.insert(18)

    print("\nPreOrder Traversal")
    tree_obj.pre_order_traversal()

    print("\nInOrder Traversal")
    tree_obj.in_order_traversal()

    print("\nPostOrder Traversal")
    tree_obj.post_order_traversal()