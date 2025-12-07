class TreeNode:
    def __init__(self, value):
        self.left= None
        self.right= None
        self.value= value
    

def build_tree_node(root, value):
    if root is None:
        return TreeNode(value)
    elif value < root.value:
        root.left= build_tree_node(root.left, value)
    else:
        root.right= build_tree_node(root.right, value)
        
    return root

arr= [1,2,3,4,5,8,6,7,9]

def createBST(arr):
    root= None;
    for val in arr:
        root = build_tree_node(root, val)
        
    return root
        
    
def inorder_traversal(root):
    if root is None:  # base case
        return
    
    inorder_traversal(root.left)   # left
    print(root.value)              # root
    inorder_traversal(root.right)  # right
    

arr= [1,2,3,4,5,8,6,7,9]


root = createBST(arr)   
inorder_traversal(root) 
        
        