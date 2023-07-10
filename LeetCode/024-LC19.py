from tkinter.tix import ListNoteBook
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNoteBook], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next
        n_from_front = length-n
        
        prehead = ListNode(0, head)
        curr2 = prehead
        for i in range(n_from_front):
            curr2 = curr2.next
        curr2.next = curr2.next.next

        return prehead.next

# Time : O(N)  Space: O(1)
# Since it's a single linked this we don't have access to end directly.
# What we can do instead is find the length of the linked and get nth from the end's distance from the front.
# We can use a prehead or prev and and curr pointer to get the element before the nth from the front element.