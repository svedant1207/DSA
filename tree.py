class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None   # Use None instead of 0
        self.right = None

class Tree:
    def __init__(self):
        self.root = None   # Initialize as empty

    def insertion(self, val):
        new_node = Node(val)

        # Case 1: Tree is empty
        if not self.root:
            self.root = new_node
            return  # Use return to exit the function

        # Case 2: Tree is not empty, use Queue (BFS)
        q = [self.root]

        while q:
            curr = q.pop(0)

            # Check Left
            if curr.left is None:
                curr.left = new_node
                return  # STOP once inserted
            else:
                q.append(curr.left)

            # Check Right
            if curr.right is None:
                curr.right = new_node
                return  # STOP once inserted
            else:
                q.append(curr.right)

    def find(self,val):
        if self.root == val:
            return True

        q = [self.root]

        while q:
            curr = q.pop(0)

            if curr.left == val:
                return True

            if curr.right:
                q.append(curr.right)
            if curr.left:
                q.append(curr.left)



class Bst:
    def __init__(self):
        self.root = None   # Initialize as empty

    def inorder(self,r):
        # if r:
        #     self.inorder(r.left)
        #     print(r.val)
        #     self.inorder(r.right)
        #

        q = []
        curr = self.r

        while q or curr:
            while curr:
                q.append(curr)
                curr = curr.left

            curr = q.pop()
            print(curr.val,end=' ')

            




    def preorder(self, r):
        # if r:
        #     print(r.val, end=' ')
        #     self.preorder(r.left)  # Call preorder, not inorder
        #     self.preorder(r.right)

        if not r:
            return

        q = [self.r]

        while q:
            curr = q.pop(0)
            print(curr.val, end=' ')

            if curr.right:
                q.append(curr.right)

            if curr.left:
                q.append(curr.left)





    def postorder(self, r):
        # if r:
        #     self.postorder(r.left)
        #     self.postorder(r.right)
        #     print(r.val, end=' ')

        if not r:
            return

        q = [self.r]
        q2 = []

        while q:
            curr = q.pop(0)
            q2.append(curr.val)

            if curr.right:
                q.append(curr.right)

            if curr.left:
                q.append(curr.left)

        return q2[::-1]



