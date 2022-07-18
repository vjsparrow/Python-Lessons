# InOrder Traversal of a binary Tree
class BinaryTree:

    def __init__(self, node):
        self.key = node
        self.right = None
        self.left = None

tree = TreeNode(2)
tree.left = TreeNode(3)
tree.left.left = TreeNode(1)
tree.right = TreeNode(5)
tree.right.left = TreeNode(3)
tree.right.left.right = TreeNode(4)
tree.right.right = TreeNode(7)
tree.right.right.left = TreeNode(6)
tree.right.right.right = TreeNode(8)

def inorder(tree):

    traversal_list = []
    if tree.left:
        inorder(tree.left)
    else:
        traversal_list.append(tree)
        if tree.right:
            inorder(tree.right)
    return traversal_list
