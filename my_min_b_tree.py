from my_b_tree import *


def find_min_value(root: TreeNode):
    while root.left is not None:
        root = root.left
    return root.key


if __name__ == "__main__":
    root = TreeNode(10)

    root = add_node(root, 5)
    root = add_node(root, 15)
    root = add_node(root, 3)
    root = add_node(root, 7)
    root = add_node(root, 12)
    root = add_node(root, 20)

    min_value = find_min_value(root)
    print("Найменше значення у дереві:", min_value)
