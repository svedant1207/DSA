class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


# Optional: inorder traversal to check tree
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

# Example usage
# Example usage
root = None

values = [55, 1, 22, 12, 11, 2, 50, 30, 70, 20, 40, 60, 80]

for v in values:
    root = insert(root, v)

print("Inorder traversal: ")
inorder(root)

print()
print("Preorder traversal: ")
preorder(root)