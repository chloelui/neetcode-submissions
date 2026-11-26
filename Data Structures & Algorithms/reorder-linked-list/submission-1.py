# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(h):
            prev = None
            while h:
                swap = h.next
                h.next = prev
                prev = h
                h = swap
            return prev

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None

        head2 = reverseList(temp)

        curr = head
        while curr and head2:
            next_node = head2.next
            head2.next = curr.next
            curr.next = head2
            curr = curr.next.next
            head2 = next_node