
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



class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prehead = ListNode(0, head)
        nth_node, end = prehead, head

        for i in range(n):
            end = end.next
        
        while end:
            nth_node = nth_node.next
            end= end.next

        nth_node.next = nth_node.next.next

        return prehead.next

# Time : O(N)  Space: O(1)
# Alternatively you can use 2 pointers maintaining a distance on n+1 between them
# One pointer at an element set before the head and one n+1 from that pointer.
# Then we traverse the linked list until the last pointer reaches the end, in which the first pointer will be just before the nth element
# We remove that element by setting the next elemenent to the next next
