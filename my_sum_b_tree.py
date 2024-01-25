from my_b_tree import *


def sum(root: TreeNode):
    if not root:
        return 0
    return root.key if not root.left and not root.right else root.key + sum(root.left) + sum(root.right)


if __name__ == "__main__":
    root = TreeNode(10)

    root = add_node(root, 5)
    root = add_node(root, 15)
    root = add_node(root, 3)
    root = add_node(root, 7)
    root = add_node(root, 12)
    root = add_node(root, 20)

    min_value = sum(root)
    print("Найменше значення у дереві:", min_value)
