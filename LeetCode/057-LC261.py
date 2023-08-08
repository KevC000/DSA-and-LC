# Graph Valid Tree
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v in edges:
            parentU = find(u)
            parentV = find(v)
            if parentU == parentV:
                return False
            parent[parentU] = parentV  

        return True
# Time: O(N) Space: O(N)
# We check if the number of edges is equal to the number of nodes - 1.
# We use Union Find to find if there is a cycle in the graph.
# We use an array to store the parent of each node.
