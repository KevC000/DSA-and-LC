# Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, left, right):
            if not node: return True
            if not (left < node.val < right): 
                return False

            return (validate(node.left, left, node.val)) and (validate(node.right, node.val, right))
        
        return validate(root, float('-inf'), float('inf'))



# Time: O(N) Space: O(N) 
# To validate a binary tree you check if the left subtree is less than the parent the right subtree is greater than its parent.
# How can we check as we traverse? Keep track of the maximum and minimum that would make that node valid.
# If we are checking the left node all its children will less than the parent so we update the maximum to the current root's.
# If we are checking the right node all its children will greaterthan the parent so we update the minimum to the current root's.
# We make sure both the left and right subtree are valid before we can say that that tree or subtree is a valid BST.