# Construct Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        pre_map = {value: i for i, value in enumerate(preorder)}
        in_map = {value: i for i, value in enumerate(inorder)}

        if not preorder or not inorder: return None

        root = TreeNode(preorder[0])
        mid = in_map[preorder[0]]
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root
    
# Time: O(N) Space: O(N)
# We populate a map to retrieve the index of the value in O(1) time when  we need it.
# Every 0th index we pass in from the preorder list is the parent and the next will be the left child and then the right child.
# With that corresponding value from the preorder we have an in order value where there the left value is the left child and right is right child.
# What ever is in the left subtree we grab the next value form preorder up until mid+1. Mid being that value index from the inorder tree
# Then the right subtree will be the valaues after that.