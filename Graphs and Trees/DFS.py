from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSHelper(self, u, visited):
        visited.add(u)
        print(u)
        for node in self.graph[u]:
            if node not in visited:
                self.DFSHelper(node, visited)
        
    def DFS(self):
        visited = set()
        for node in self.graph:
            if node not in visited:
                self.DFSHelper(node, visited)
    
    def BFS(self, s):
        visited = set()
        queue = []

        queue.append(s)
        visited.add(s)
        # print(s)
        while queue:
            p = queue.pop(0)
            print(p)
            for node in self.graph[p]:
                if node not in visited:
                    queue.append(node)
                    visited.add(node)
            


g = Graph()
g.addEdge('a','b')
g.addEdge('b','c')
g.addEdge('a','c')
g.addEdge('c','d')
g.addEdge('d','a')
g.DFS()
print(g.graph)
g.BFS('a')
    