class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_and_new  = {}

        def dfs(node):
            if node in old_and_new:
                return old_and_new[node]
            
            copy = Node(node.val)
            old_and_new[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        return dfs(node) if node else None

# Time: O(N) space: O(N)
# Iterate through the graph and if we have not seen the node before we create a copy of it
# and add it to the dictionary. Then we iterate through the neighbors and add them to the copy
# by calling the function recursively. We return the copy of the node
