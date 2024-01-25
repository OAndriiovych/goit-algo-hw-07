from my_b_tree import *


def find_max_value(root: TreeNode):
    while root.right is not None:
        root = root.right
    return root.key


if __name__ == "__main__":
    root = TreeNode(10)

    root = add_node(root, 5)
    root = add_node(root, 15)
    root = add_node(root, 3)
    root = add_node(root, 7)
    root = add_node(root, 12)
    root = add_node(root, 20)

    max_value = find_max_value(root)
    print("Найбільше значення у дереві:", max_value)
