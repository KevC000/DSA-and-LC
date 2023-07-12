# Count Good Nodes in Binary Tree

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        q = deque([(root, float('-inf'))])

        while q:
            for i in range(len(q)):
                curr_node, curr_max = q.popleft()
                if curr_node.val >= curr_max:
                    total+=1
                if curr_node.left: 
                    q.append((curr_node.left, max(curr_max, curr_node.val)))
                if curr_node.right:
                    q.append((curr_node.right, max(curr_max, curr_node.val)))
        return total
    
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        stack = [(root, float('-inf'))]

        while stack:
    
            for i in range(len(stack)):
                curr_node, curr_max = stack.pop()
                if curr_node.val >= curr_max:
                    total+=1
                if curr_node.left: 
                    stack.append((curr_node.left, max(curr_max, curr_node.val)))
                if curr_node.right:
                    stack.append((curr_node.right, max(curr_max, curr_node.val)))
        return total
    
# Time: O(N) Space: O(N)
# We perform either a bfs or a dfs traversal.
# We check if the current node's value is greater than the max in that path and add to the total if it is.
# We pass down the current max to it's children to check the other nodes until we trawverse the entire tree.
# Return the count at the end.