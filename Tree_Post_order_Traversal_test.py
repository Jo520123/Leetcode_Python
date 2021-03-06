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

            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert_node(val)
        else:
            self.val = val

    def Post_Order(self, root):
        output =[]
        if root:
            output = self.Post_Order(root.left)
            output = output + self.Post_Order(root.right)
            output.append(root.val)

        return output


root = TreeNode(27)
root.insert_node(14)
root.insert_node(35)
root.insert_node(10)
root.insert_node(19)
root.insert_node(31)
root.insert_node(42)

print(root.Post_Order(root))

