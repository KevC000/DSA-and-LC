#Reorder List

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def findMiddle(head):
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse(head):
            previous, current, next = None, head, None

            while current:
                next = current.next
                current.next = previous
                previous = current
                current = next
            return previous

        middle = findMiddle(head)
        reversed_head = reverse(middle.next)
        middle.next = None
        
        prehead = ListNode(0)
        new_list, odd, even = prehead, head, reversed_head

        while odd or even:
            if odd:
                new_list.next = odd
                odd = odd.next
                new_list = new_list.next
            if even:
                new_list.next = even
                even = even.next
                new_list = new_list.next

        new_list.next = odd

        return prehead.next

# Time : O(N)  Space: O(1)
# The new list is essentially appending alternating between the first half of the list then the second half starting form the end
# It's a singly linked list we need a way to iterate from the second half starting from the front to the middle
# To do that we need to reverse the second half and iterate from there.
# How do we get the second half? We find the middle and reverse the econd half. 
# We also need to set the last element of the first half's next element to None so we don't get a cycle..       