#Binary Tree Right Side View

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root])
        res = [root.val]
        while q:
            right_most = None
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    right_most = curr.left.val
                    q.append(curr.left)
                if curr.right:
                    right_most = curr.right.val
                    q.append(curr.right)
            if right_most is not None: res.append(right_most)
        return res


# Time: O(N) Sapce: O(N)
# We want the right most element of each level. The right most element can be the left children of it's parent's children, so we need to take that into account.
# We can use a queue and update the most right element as we traverse that level. 
# At the end of the traversal of that level. We append the right most value to the resulting list. If None we skip appending.
# Once we traverse each level of the tree we return the resulting list.