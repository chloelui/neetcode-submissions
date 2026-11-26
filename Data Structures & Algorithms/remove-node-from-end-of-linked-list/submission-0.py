# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length, curr = 0, head
        while curr:
            length += 1
            curr = curr.next

        prev, curr = None, head
        for i in range(length):
            if i == length - n:
                if prev:
                    prev.next = curr.next
                    return head
                else:
                    prev = curr.next
                    return prev
            prev = curr
            curr = curr.next