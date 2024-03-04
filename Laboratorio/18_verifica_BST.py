class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

# costruisce un albero binario da una lista in forma polacca inversa
def build_tree(polish_notation):
    if polish_notation[0] == 'NULL':
        polish_notation.pop(0)
        return None
    root = Node(int(polish_notation.pop(0)))
    root.left = build_tree(polish_notation)
    root.right = build_tree(polish_notation)
    return root

# controlla se un albero binario è un BST
def is_BST(node, left=float('-inf'), right=float('inf')):
    if node is None:
        return True
    if not left < node.key < right:
        return False
    return is_BST(node.left, left, node.key) and is_BST(node.right, node.key, right)

polish_notation = input().split()

root = build_tree(polish_notation)

print(1 if is_BST(root) else 0)
