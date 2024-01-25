class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def add_node(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = add_node(root.left, key)
    elif key > root.key:
        root.right = add_node(root.right, key)
    return root
