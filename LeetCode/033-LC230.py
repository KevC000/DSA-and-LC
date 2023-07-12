#Kth Smallest Element in a BST

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
            
# Time: O(N) Space: O(N)
# We peform an in order traversal because the left child < parent < right child.
# Each time we reach the value via popping from the stack reduce k and when k is 0 we've reached that value.