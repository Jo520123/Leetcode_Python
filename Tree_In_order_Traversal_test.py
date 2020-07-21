class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def insert_node(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert_node(val)

            if val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert_node(val)
        else:
            self.val = val

    def In_Order(self, root):
        output =[]
        if root:
            output = self.In_Order(root.left)
            output.append(root.val)
            output = output + self.In_Order(root.right)
        return output

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()


root = TreeNode(27)
root.insert_node(10)
root.insert_node(14)
root.insert_node(19)
root.insert_node(31)
root.insert_node(35)
root.insert_node(42)
print(root.In_Order(root))
print(root.print_tree())
