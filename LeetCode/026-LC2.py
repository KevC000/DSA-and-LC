# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prehead =  ListNode(0)
        l1_p, l2_p, result = l1, l2, prehead

        carry = 0

        while l1_p or l2_p:
            digit_one = l1_p.val if l1_p else 0
            digit_two = l2_p.val if l2_p else 0

            total = digit_one+digit_two+carry

            if total > 9: 
                total-=10
                carry = 1
            else:
                carry = 0

            new_node = ListNode(total)
            result.next = new_node

            result = result.next
            if l1_p: l1_p = l1_p.next
            if l2_p: l2_p = l2_p.next

        if carry == 1: 
            result.next = ListNode(1)
        
        return prehead.next

# Time O(N) Space O(1)/O(N) depending if the result counts toward extra space.
# Append to the resulting list the sum of the current l1 and l2 at the pointer and add 1 if there is a carry from the previous element.
# If any of them is None we use 0.
# If it is greater than 10 we subtract 10 from the total and carry will be set to 1
# If carry still remains we append to the list.