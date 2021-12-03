class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def ZigZagTraversal(self, root):
        if root is None:
            return []
        else:
            currentLevel = []
            nextLevel = []

            ltr = True

            currentLevel.append(root)

            while len(currentLevel) > 0:
                top = currentLevel.pop()
                # for node in currentLevel:
                print(top.data)

                if ltr:
                    if top.left: 
                        nextLevel.append(top.left)
                    if top.right: 
                        nextLevel.append(top.right)
                else:
                    if top.right: 
                        nextLevel.append(top.right)
                    if top.left: 
                        nextLevel.append(top.left)

                if len(currentLevel) == 0:
                    ltr = not ltr
                    currentLevel = nextLevel
                    nextLevel = []
    

root  = Node (14)
root.left = Node(10)
root.right = Node(18)
root.left.left = Node(6)
root.left.right = Node(15)
root.right.left = Node(16)
root.right.right = Node(20)

print(root.ZigZagTraversal(root))