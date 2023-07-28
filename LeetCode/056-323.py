#Number of Connected Components in an Undirected Graph
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        parent = [i for i in range(n)]
        components = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for u, v in edges:
            parent_u = find(u)
            parent_v = find(v)
            if parent_u != parent_v:
                parent[parent_u] = parent_v
                n-=1
        return n

# Time: O(N) Space: O(N)
# We use Union Find to create the connected components in the graph.
# Each time we connect 2 nodes, we decrease the number of components by 1.
# At the end, we return the number of components.