# Redundant Connection
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {u: u for edge in edges for u in edge}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        for u, v in edges:
            parent_u = find(u)
            parent_v = find(v)
            if parent_u == parent_v:
                return [u, v]
            else:
                parent[parent_u] = parent_v

# Time: O(N) Space: O(N)
# We use Union Find to find if there is a cycle in the graph.
# We use a hsahmap to store the parent of each node.
# Then we iterate over the edges and find the parent of each node.
# If the parent of both the nodes is same, then there is a cycle in the graph.
