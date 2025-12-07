class TreeNode:
    def __init__(self, value):
        self.value= value
        self.left = None
        self.right= None
    def insert_node(self, value):
        # if self.value is None:
        #     TreeNode(value)
        if value < self.value:
            if self.left is None:
                self.left= TreeNode(value)
            else:
                self.left.insert_node(value)
        else:
            if self.right is None:
                self.right= TreeNode(value)
            else:
                self.right.insert_node(value)
                
    def inorder_traversal(self, root):
        if root.left: self.inorder_traversal(root.left)   
        print(root.value)         
        if root.right: self.inorder_traversal(root.right)            
    def pre_traversal(self, root):
        print(root.value)         
        if root.left: self.pre_traversal(root.left)   
        if root.right: self.pre_traversal(root.right)            
                
root= TreeNode(5)
root.insert_node(4)
root.insert_node(8)
root.insert_node(9)
root.insert_node(3)
root.insert_node(2)
root.insert_node(6)

root.pre_traversal(root)
