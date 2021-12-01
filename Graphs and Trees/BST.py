class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
    
    # Insert function creates BST
    def insert(self, node, data):
        if node.data == data:
            return
        if data < node.data:
            if node.left:
                self.insert(node.left, data)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insert(node.right, data)
            else:
                node.right = Node(data)
    
    

def inorder( node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

root = Node(50)
root.insert(root, 30)
root.insert(root, 20)
root.insert(root, 60)
root.insert(root, 70)
root.insert(root, 55)

inorder(root)

