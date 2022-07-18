# Tree to tuple

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


tree = TreeNode(2)
tree.left = TreeNode(3)
tree.left.left = TreeNode(1)
tree.right = TreeNode(5)
tree.right.left = TreeNode(3)
tree.right.left.right = TreeNode(4)
tree.right.right = TreeNode(7)
tree.right.right.left = TreeNode(6)
tree.right.right.right = TreeNode(8)


# ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))


def tree_to_tuple(node):

    if node is None:
        return None
    elif node.left is None and node.right is None:
        return node.key
    else:
        tree_tuple = tuple([tree_to_tuple(node.left), node.key, tree_to_tuple(node.right)])

    # ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))

    print(tree_tuple)
    return tree_tuple

tree_to_tuple(tree)
