#Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        res = [[root.val]]
        while q:
            level = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    level.append(curr.left.val)
                    q.append(curr.left)
                if curr.right:
                    level.append(curr.right.val)
                    q.append(curr.right)
            if len(level) > 0: res.append(level)
        return res
    
# Time: O(N) Space: O(N)
# We want to visit each node in that level, after visiting that level we move on to it's children
# How can we access its children after visiting that node? We can store its children in qeueue to visit later.
# As we visit the nodes we append each level's nodes to a list.
# Before we move on to the next level we append to the resulting list.