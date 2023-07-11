"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {None:None}

        curr = head
        while curr:
            copy = Node(curr.val)
            nodes[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = nodes[curr]
            copy.next = nodes[curr.next]
            copy.random = nodes[curr.random]
            curr = curr.next
        
        return nodes[head]

# Time: O(N) Space: O(N)
# We are making copies of the first linked list and we cannot reuse the previous list in the copy.
# We need a way to match the copied node with the original since we cannot reuse the old node.
# We can use a hashmap where the key is the original node and the value is the copied node.
# If we have a pointer to a certain node we can access the copied node using the hashmap.
# First iteration copy the nodes and populate the hashmap
# Second iteration set the pointers to the copied version of the nodes.