class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        self.min = 99
        self.max = -99

    def isBSTUtil(self, root, min, max):
        print(root.data if root != None else None)
        print(min, max)
        
        if root is None:
            return True
        if root.data < min or root.data > max:
            return False
        # if root.data > min 
        return (self.isBSTUtil(root.left, min, root.data) and self.isBSTUtil(root.right, root.data, max))

    
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
    
    

root  = Node (14)
root.left = Node(10)
root.right = Node(18)
root.left.left = Node(6)
root.left.right = Node(15)
root.right.left = Node(16)
root.right.right = Node(20)

print(root.isBSTUtil(root, -99, 99))