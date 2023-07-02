class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
        
    def dfs(self, node, visited):
        if self.node in visited: 
            return
        
        print(node.val)
        
        for n in self.neighbors:
            self.dfs(n,visited)